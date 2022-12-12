import logging

import WeatherStationProperties

properties = WeatherStationProperties.WeatherStationProperties()

class GroundStationHandler:
	
	def __init__(self, SerialConnectionHandler):
		
		# Initialize logger
		logging.basicConfig(filename=str(properties.getLoggingFolder()) + "DataStorageHandler.log", format='%(asctime)s %(module)s %(levelname)s - %(message)s', filemode='w')
		self.logger = logging.getLogger(__name__)
		self.logger.setLevel(logging.DEBUG)
		
		self.logger.info("Initializing Ground Station Handler...")
		
		self.serialConnection = SerialConnectionHandler
		self.initialized = False
		
	def initializeGroundStation(self):
		
		# Initialize UV sensor if it has not been initialized
		if (self.initialized == False):
			self.initialized = True
			return self.serialConnection.initialized
		
	def startRotation(self):
		self.logger.info("Start Rotating Ground Station...")
		self.serialConnection.write(b'A')

	def stopRotation(self):
		self.logger.info("Stop Rotating Ground Station...")
		self.serialConnection.write(b'O')

	def shutdown(self):
		self.stopRotation()
