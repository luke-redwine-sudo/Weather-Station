from random import randint
import board
import adafruit_bme280.basic as adafruit_bme280
import logging
import sys

import WeatherStationProperties

properties = WeatherStationProperties.WeatherStationProperties()

class BME280Handler:
	
	def __init__(self):
		# Initialize self variables
		self.initialized = False
		self.bme280Address = 0x76
		self.i2c = None
		self.sensor = None
		
		# Initialize logger
		logging.basicConfig(filename=str(properties.getLoggingFolder()) + "BME280Handler.log", disable_existing_loggers=False, format='%(asctime)s %(module)s %(levelname)s - %(message)s', filemode='w')
		self.logger = logging.getLogger()
		self.logger.setLevel(logging.DEBUG)
		
		self.logger.info("Initializing BME280 Handler...")
		
	def initializeBME(self):
		self.logger.info("Initializing BME280 Sensor...")
		
		# Initialize BME280 if it has not been initialized
		if (self.initialized == False):
			try:
				self.i2c = board.I2C()
				self.sensor = adafruit_bme280.Adafruit_BME280_I2C(self.i2c, address=self.bme280Address)
				self.initialized = True
			except:
				self.logger.error("Sensor could not be contacted")
	
	def readTemperature(self):
				
		# Read the temperature from the sensor if it is initialized
		if (self.initialized == True):
			return round(self.celsiusToFahrenheit(self.sensor.temperature),1)

		return 0
		
	def readHumidity(self):
		
		# Read the humidity from the sensor if it is initialized
		if (self.initialized == True):
			return round(self.sensor.humidity,1)

		return 0
	
	def readPressure(self):
		
		# Read the pressure from the sensor if it is initialized
		if (self.initialized == True):
			return round(self.sensor.pressure,1)

		return 0
	
	def celsiusToFahrenheit(self, celsiusTemperature):
		fahrenheitTemperature = (celsiusTemperature * 1.8) + 32.0
		return fahrenheitTemperature
	
	def shutdown(self):
		self.logger.info("Shutdown BME280 Handler...")
		
		# Shutdown the sensor
		if (self.initialized == True):
			self.initialized = False
