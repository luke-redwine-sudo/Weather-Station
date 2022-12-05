from random import randint
import logging
import sys

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
		
		self.logger.info("Initializing UV Sensor Handler...")
		
	def initializeUV(self):
		self.logger.info("Initializing UV Sensor...")
		
		# Initialize UV sensor if it has not been initialized
		if (self.initialized == False):
			self.initialized = True
			
	def readUV(self):
		
		# Read the UV from the sensor if it is initialized
		if (self.initialized == True):
			return randint(0,10)

		return 0

	def shutdown(self):
		self.logger.info("Shutdown UV Sensor Handler...")
		
		# Shutdown the sensor
		if (self.initialized == True):
			self.initialized = False
