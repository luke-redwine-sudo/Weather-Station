from jproperties import Properties

class WeatherStationProperties:
	
	def __init__(self):
		self.configs = Properties()
		with open('WeatherStation.properties', 'rb') as config_file:
			self.configs.load(config_file)
	
	def getLoggingFolder(self):
		return self.configs.get("weatherstation.logging_folder").data
		
	def getDataFolder(self):
		return self.configs.get("weatherstation.data_folder").data
		
	def getCollectionFrequency(self):
		return self.configs.get("weatherstation.collection_frequency").data
		
	def getDataFileSize(self):
		return self.configs.get("weatherstation.data_file_size").data
		
	def getDataFilePrefix(self):
		return self.configs.get("weatherstation.data_file_prefix").data
		
