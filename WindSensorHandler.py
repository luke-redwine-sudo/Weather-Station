from random import randint
import logging
import sys

import WeatherStationProperties

properties = WeatherStationProperties.WeatherStationProperties()

class WindSensorHandler:
	
	def __init__(self):
		# Initialize self variables
		self.initialized = False
		
		# Initialize logger
		logging.basicConfig(filename=str(properties.getLoggingFolder()) + "WindSensorHandler.log", disable_existing_loggers=False, format='%(asctime)s %(module)s %(levelname)s - %(message)s', filemode='w')
		self.logger = logging.getLogger()
		self.logger.setLevel(logging.DEBUG)
		
		self.logger.info("Initializing Wind Sensor Handler...")
		
	def initializeWindSensor(self):
		self.logger.info("Initializing Wind Sensor...")
		
		# Initialize UV sensor if it has not been initialized
		if (self.initialized == False):
			self.initialized = True
			
	def readWindDirection(self):
		
		# Read the wind direction from the sensor if it is initialized
		if (self.initialized == True):
			return randint(0,360)

		return 0
	
	def readWindSpeed(self):
		
		# Read the wind speed from the sensor if it is initialized
		if (self.initialized == True):
			return randint(0,100)

		return 0
		
		
	def shutdown(self):
		self.logger.info("Shutdown Wind Sensor Handler...")
		
		# Shutdown the sensor
		if (self.initialized == True):
			self.initialized = False

