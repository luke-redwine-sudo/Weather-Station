from random import randint
import logging
import numpy
import sys
import time
import math
from gpiozero import Button

import WeatherStationProperties

properties = WeatherStationProperties.WeatherStationProperties()

class WindSensorHandler:
	
	def __init__(self, SerialConnectionHandler):
		# Initialize self variables
		self.initialized = False
		
		# Initialize logger
		logging.basicConfig(filename=str(properties.getLoggingFolder()) + "WindSensorHandler.log", disable_existing_loggers=False, format='%(asctime)s %(module)s %(levelname)s - %(message)s', filemode='w')
		self.logger = logging.getLogger()
		self.logger.setLevel(logging.DEBUG)
		
		self.logger.info("Initializing Wind Sensor Handler...")
		
		self.serialConnection = SerialConnectionHandler
		
		
	def initializeWindSensor(self):
		self.logger.info("Initializing Wind Sensor...")
		
		# Initialize UV sensor if it has not been initialized
		if (self.initialized == False):
			self.windSpeedSensor = Button(5)
			self.windCount = 0
			self.windSpeedSensor.when_pressed = self.spin
			self.initialized = True
			return self.serialConnection.initialized
	
	def spin(self):
		self.windCount += 1
	
	def readWindDirection(self):
		
		# Read the wind direction from the sensor if it is initialized
		if (self.initialized and self.serialConnection.initialized):
			self.serialConnection.write(b'D')
			
			direction = self.serialConnection.read()
			
			if (direction == 34):
				direction = 270.0
			elif (direction == 56):
				direction = 292.0
			elif (direction == 69):
				direction = 315.0
			elif (direction == 91):
				direction = 337.0
			
			return direction

		return 0
	
	def readWindSpeed(self):
		
		circumference_cm = (2.0 * math.pi) * 9.0
		rotations = self.windCount / 2.0

		dist_cm = circumference_cm * rotations

		speed = (dist_cm / (int(properties.getCollectionFrequency()) / 1000)) * 0.036
		
		speed = round((speed * 1.18) / 1.609,1)
		
		self.windCount = 0

		return speed
		
		
	def shutdown(self):
		self.logger.info("Shutdown Wind Sensor Handler...")
		
		# Shutdown the sensor
		if (self.initialized == True):
			self.initialized = False

