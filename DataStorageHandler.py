import pandas as pd
import os
import logging

import WeatherStationProperties

properties = WeatherStationProperties.WeatherStationProperties()

class DataStorageHandler:
	
	def __init__(self):
		
		self.columns = ["DateTime", "Temperature", "Humidity", "Pressure", "UV", "Wind_Speed", "Wind_Direction"]
		
		# Initialize logger
		logging.basicConfig(filename=str(properties.getLoggingFolder()) + "DataStorageHandler.log", disable_existing_loggers=False, format='%(asctime)s %(module)s %(levelname)s - %(message)s', filemode='w')
		self.logger = logging.getLogger(__name__)
		self.logger.setLevel(logging.DEBUG)
		
		self.logger.info("Initializing Data Storage Handler...")
		
		self.initialized = False
		
		
	def initializeDataStorage(self):
		
		if (self.initialized == False):
			self.folder = str(properties.getDataFolder())
			self.max_csv_number = 1
			
			if (os.path.isdir(self.folder)):
				dir_list = os.listdir(self.folder)
				
				for f in dir_list:
					self.logger.info(f)
					if (str(properties.getDataFilePrefix()) in f and int(f.split("_")[1].split(".")[0]) >= self.max_csv_number):
						self.logger.info("Increasing Log Level...")
						self.max_csv_number = int(f.split("_")[1].split(".")[0]) + 1
				
			else:
				os.makedirs(self.folder)
			
			self.filename = self.folder + str(properties.getDataFilePrefix()) + "_{0:0=2d}".format(self.max_csv_number) + ".csv"
			self.dataframe = pd.DataFrame(columns=self.columns)
			
			self.initialized = True
	
	
	def isDataFrameOversized(self):
		if ((self.dataframe.memory_usage(deep=True).sum() / 1000000) > float(properties.getDataFileSize())):
			return True
		else:
			return False
	
	def write(self, temperature, humidity, pressure, UV, windDirection, windSpeed):
		datetime = pd.datetime.now()
		dataRow = [datetime, temperature, humidity, pressure, UV, windDirection, windSpeed]
		
		if (self.isDataFrameOversized()):
			self.logger.info("Dumping Data, Creating new log...")
			self.writeToCsv()
			self.max_csv_number = self.max_csv_number + 1
			self.filename = self.folder + str(properties.getDataFilePrefix()) + "_{0:0=2d}".format(self.max_csv_number) + ".csv"
			self.dataframe = pd.DataFrame(columns=self.columns)
		
		self.dataframe.loc[len(self.dataframe.index)] = dataRow
	
	def writeToCsv(self):
		self.dataframe.to_csv(self.filename)

	def shutdown(self):
		
		self.logger.info("Shutdown Data Storage Handler...")
		
		if (self.initialized == True):
			self.writeToCsv()
			
