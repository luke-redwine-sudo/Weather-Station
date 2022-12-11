from random import randint
import logging
import sys

import pandas as pd

import BME280Handler
import UVSensorHandler
import WindSensorHandler
import DataStorageHandler
import SerialConnectionHandler
import GroundStationHandler
import WeatherStationProperties

properties = WeatherStationProperties.WeatherStationProperties()

class GUIHandler:
	
	def __init__(self, root, temperatureLabel, humidityLabel, pressureLabel, uvLabel, windDirectionLabel, windSpeedLabel, groundStationButton):
		
		# Initialize self variables
		self.root = root
		self.temperatureLabel = temperatureLabel
		self.humidityLabel = humidityLabel
		self.pressureLabel = pressureLabel
		self.uvLabel = uvLabel
		self.windDirectionLabel = windDirectionLabel
		self.windSpeedLabel = windSpeedLabel
		self.groundStationButton = groundStationButton
		self.collectData = False
		self.isRotation = False
		
		# Initialize logger
		logging.basicConfig(filename=str(properties.getLoggingFolder()) + "GUIHandler.log", disable_existing_loggers=False, format='%(asctime)s %(module)s %(levelname)s - %(message)s', filemode='w')
		self.logger = logging.getLogger(__name__)
		self.logger.setLevel(logging.DEBUG)
		
		self.logger.info("Initializing GUI Handler...")
		
		# Initialize Serial Communications Handler
		self.SerialConnectionHandler = SerialConnectionHandler.SerialConnectionHandler()
		
		# Initialize sensor Handlers
		self.BME280Handler = BME280Handler.BME280Handler()
		self.UVSensorHandler = UVSensorHandler.UVSensorHandler(self.SerialConnectionHandler)
		self.WindSensorHandler = WindSensorHandler.WindSensorHandler(self.SerialConnectionHandler)
		self.GroundStationHandler = GroundStationHandler.GroundStationHandler()
		
		# Initialize Data Handler
		self.DataStorageHandler = DataStorageHandler.DataStorageHandler()
		
		
	def startDataCollection(self):
		# Initialize Sensors
		self.logger.info("Starting Data Collection...")
		self.setCollectData(True)
		self.SerialConnectionHandler.initializeSerialConnection()
		self.BME280Handler.initializeBME()
		self.UVSensorHandler.initializeUV()
		self.WindSensorHandler.initializeWindSensor()
		
	def endDataCollection(self):
		# Shutdown sensors
		self.logger.info("Ending Data Collection...")
		self.setCollectData(False)

	def update(self):
		# Poll the sensors and update the read outs
		self.logger.debug("Updating Read outs...")
		
		# Only poll the sensors if data collection has started
		if (self.collectData == True):
			temperature, humidity, pressure = self.updateBMESensor()
			UV = self.updateUVSensor()
			windDirection, windSpeed = self.updateWindSensor()
			self.DataStorageHandler.write(temperature, humidity, pressure, UV, windDirection, windSpeed)
			
		self.root.after(properties.getCollectionFrequency(), self.update)
		
	def setCollectData(self, collect):
		# Set collect data
		self.collectData = collect
		self.DataStorageHandler.initializeDataStorage()
		
	def getCollectData(self):
		# Return the current collection status
		return self.CollectData
		
	def updateBMESensor(self):
		self.logger.debug("Update BME Sensor...")
		
		temperature = 0
		humidity = 0
		pressure = 0
		
		# Poll the BME280 sensor if it is initialized
		if (self.BME280Handler.initialized):
			temperature = self.BME280Handler.readTemperature()
			humidity = self.BME280Handler.readHumidity()
			pressure = self.BME280Handler.readPressure()
		else:
			self.BME280Handler = BME280Handler.BME280Handler()
			temperature = 0.0
			humidity = 0.0
			pressure = 0.0
		
		self.temperatureLabel.configure(text="Temperature: %.1f F" % temperature)
		self.humidityLabel.configure(text="Humidity:       %.1f" % humidity + "%")
		self.pressureLabel.configure(text="Pressure:       %.1f Pa" % pressure)
		
		return temperature, humidity, pressure

	def updateUVSensor(self):
		self.logger.debug("Update UV Sensor...")
		
		UV = 0
		
		# Poll the UV sensor if it is initialized
		if (self.UVSensorHandler.initialized):
			UV = self.UVSensorHandler.readUV()
			self.uvLabel.configure(text="UV:                   %.1f" % UV)
		
		return UV
		
	def updateWindSensor(self):
		self.logger.debug("Update Wind Sensor...")
		
		windDirection = 0
		windSpeed = 0
		
		# Poll the Wind Sensor if it is initialized
		if (self.WindSensorHandler.initialized):
			windDirection = self.WindSensorHandler.readWindDirection()
			windSpeed = self.WindSensorHandler.readWindSpeed()
			self.windDirectionLabel.configure(text="Wind Direction: " + str(windDirection))
			self.windSpeedLabel.configure(text="Wind Speed:     %.1f mph" % windSpeed)
			
		return windDirection, windSpeed
		
	def toggleGroundStationRotation(self):
		if (self.isRotation):
			self.stopRotateGroundStation()
			self.groundStationButton.configure(text="Start Rotation", fg_color='orange')
		else:
			self.startRotateGroundStation()
			self.groundStationButton.configure(text="Stop Rotation", fg_color='red')
			
		self.isRotation = not self.isRotation
	
	def startRotateGroundStation(self):
		self.GroundStationHandler.startRotation()
		
	def stopRotateGroundStation(self):
		self.GroundStationHandler.stopRotation()
		
	def shutdown(self):
		self.logger.info("Commense Shutdown...")
		
		# Shutdown sensors and close window
		self.BME280Handler.shutdown()
		self.UVSensorHandler.shutdown()
		self.WindSensorHandler.shutdown()
		self.GroundStationHandler.shutdown()
		self.SerialConnectionHandler.shutdown()
		
		if (self.DataStorageHandler != None):
			self.DataStorageHandler.writeToCsv()
		
		self.DataStorageHandler.shutdown()
		
		self.root.quit()
