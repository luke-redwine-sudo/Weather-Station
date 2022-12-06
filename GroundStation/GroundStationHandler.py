import logging

import WeatherStationProperties

properties = WeatherStationProperties.WeatherStationProperties()

class GroundStationHandler:
	
	def __init__(self):
		
		# Initialize logger
		logging.basicConfig(filename=str(properties.getLoggingFolder()) + "DataStorageHandler.log", format='%(asctime)s %(module)s %(levelname)s - %(message)s', filemode='w')
		self.logger = logging.getLogger(__name__)
		self.logger.setLevel(logging.DEBUG)
		
		self.logger.info("Initializing Ground Station Handler...")
		
	def startRotation(self):
		self.logger.info("Start Rotating Ground Station...")

	def stopRotation(self):
		self.logger.info("Stop Rotating Ground Station...")

	def shutdown(self):
		self.stopRotation()
