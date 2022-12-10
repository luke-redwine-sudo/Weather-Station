from random import randint
import logging
import sys
import serial
import chardet
import time
import serial.tools.list_ports

import WeatherStationProperties

properties = WeatherStationProperties.WeatherStationProperties()

class UVSensorHandler:
	
	def __init__(self):
		# Initialize self variables
		self.initialized = False
		
		# Initialize logger
		logging.basicConfig(filename=str(properties.getLoggingFolder()) + "UVSensorHandler.log", disable_existing_loggers=False, format='%(asctime)s %(module)s %(levelname)s - %(message)s', filemode='w')
		self.logger = logging.getLogger()
		self.logger.setLevel(logging.DEBUG)
		
		self.commport = None
		self.serialPort = None
		
		self.logger.info("Initializing UV Sensor Handler...")
		
	def initializeUV(self):
		self.logger.info("Initializing UV Sensor...")
		
		# Initialize UV sensor if it has not been initialized
		if (self.initialized == False):
			
			ports = list(serial.tools.list_ports.comports())
						
			for port in ports:
				
				self.commport = "/dev/"+port.description
				self.serialPort = serial.Serial(self.commport, 9600, timeout=3)
				
				time.sleep(2)
				
				self.serialPort.write(b'T')
				
				if (self.serialPort.readline() == b'L'):
					self.initialized = True
					break
				
				self.commport = None			
				self.serialPort = None
			
	def readUV(self):
		
		# Read the UV from the sensor if it is initialized
		if (self.initialized == True):
			self.requestUVReading()
			
			return float(ord(self.serialPort.read(1)))

		return 0

	def requestUVReading(self):
		if (self.serialPort is not None):
			self.serialPort.write(b"U")

	def shutdown(self):
		self.logger.info("Shutdown UV Sensor Handler...")
		
		# Shutdown the sensor
		if (self.initialized == True):
			self.serialPort.close()
			self.initialized = False
