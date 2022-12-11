from random import randint
import logging
import sys
import serial
import chardet
import time
import serial.tools.list_ports

import WeatherStationProperties

properties = WeatherStationProperties.WeatherStationProperties()

class SerialConnectionHandler:
	
	def __init__(self):
		# Initialize self variables
		self.initialized = False
		
		# Initialize logger
		logging.basicConfig(filename=str(properties.getLoggingFolder()) + "SerialConnectionHandler.log", disable_existing_loggers=False, format='%(asctime)s %(module)s %(levelname)s - %(message)s', filemode='w')
		self.logger = logging.getLogger()
		self.logger.setLevel(logging.DEBUG)
		
		self.commport = None
		self.serialPort = None
		
		self.logger.info("Initializing UV Sensor Handler...")

	def initializeSerialConnection(self):
		
		if (self.initialized == False):
			
			ports = self.findAvailablePorts()
						
			for port in ports:
				
				self.commport = "/dev/"+port.description
				self.serialPort = serial.Serial(self.commport, 9600, timeout=3)
				
				time.sleep(2)
				
				if (self.handshakeProtocol()):
					self.initialized = True
					break
				
				self.commport = None			
				self.serialPort = None


	def findAvailablePorts(self):
		return list(serial.tools.list_ports.comports())
		
	def handshakeProtocol(self):
		
		self.serialPort.write(b'T')
		
		if (self.serialPort.readline() == b'L'):
			return True
		
		return False
	
	def read(self):
		return float(ord(self.serialPort.read(1)))
		
	def write(self, message):
		return self.serialPort.write(message)
		
	def shutdown(self):
		self.logger.info("Shutdown Serial Connection Handler...")
		
		# Shutdown the sensor
		if (self.initialized == True):
			self.serialPort.close()
			self.initialized = False
