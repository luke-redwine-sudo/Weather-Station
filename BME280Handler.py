from random import randint
import logging
import sys

import WeatherStationProperties

properties = WeatherStationProperties.WeatherStationProperties()

class BME280Handler:
	
	def __init__(self):
		# Initialize self variables
		self.initialized = False
		
		# Initialize logger
		logging.basicConfig(filename=str(properties.getLoggingFolder()) + "BME280Handler.log", disable_existing_loggers=False, format='%(asctime)s %(module)s %(levelname)s - %(message)s', filemode='w')
		self.logger = logging.getLogger()
		self.logger.setLevel(logging.DEBUG)
		
		self.logger.info("Initializing BME280 Handler...")
		
	def initializeBME(self):
		self.logger.info("Initializing BME280 Sensor...")
		
		# Initialize BME280 if it has not been initialized
		if (self.initialized == False):
			self.initialized = True
			
	def readTemperature(self):
				
		# Read the temperature from the sensor if it is initialized
		if (self.initialized == True):
			return randint(0,100)

		return 0
		
	def readHumidity(self):
		
		# Read the humidity from the sensor if it is initialized
		if (self.initialized == True):
			return randint(0,100)

		return 0
	
	def readPressure(self):
		
		# Read the pressure from the sensor if it is initialized
		if (self.initialized == True):
			return randint(0,100)

		return 0
		
	def shutdown(self):
		self.logger.info("Shutdown BME280 Handler...")
		
		# Shutdown the sensor
		if (self.initialized == True):
			self.initialized = False
