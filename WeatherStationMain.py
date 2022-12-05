from tkinter import *
import customtkinter
from threading import Thread
from PIL import ImageTk, Image
import GUIHandler
import logging
import sys
import WeatherStationProperties

properties = WeatherStationProperties.WeatherStationProperties()

customtkinter.set_appearance_mode("dark")

logging.basicConfig(filename=str(properties.getLoggingFolder()) + "WeatherStation.log",
                    format='%(asctime)s %(module)s %(levelname)s - %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)  
handler.setFormatter(logging.Formatter('%(asctime)s %(module)s %(levelname)s - %(message)s'))                                  
logger.addHandler(handler)   

# Create Tkinter Object
root = customtkinter.CTk()
root.attributes('-fullscreen',True)

logger.info("Creating Tkinter Object...")
 
# Specify Grid
Grid.columnconfigure(root,0,weight=2)
Grid.columnconfigure(root,1,weight=1)
Grid.columnconfigure(root,3,weight=2)
Grid.rowconfigure(root,0,weight=10)
Grid.rowconfigure(root,1,weight=1)
Grid.rowconfigure(root,2,weight=25)
Grid.rowconfigure(root,3,weight=1)
Grid.rowconfigure(root,4,weight=1)
Grid.rowconfigure(root,5,weight=1)

logger.info("Specifying Grid...")

# Create Buttons
startButton = customtkinter.CTkButton(root,text="Start Data Collection", fg_color='green',
	command = lambda: guiHandler.startDataCollection(), text_color="black",
	font=("Calibria", 15))
endButton = customtkinter.CTkButton(root,text="End Data Collection", fg_color='yellow',
	command = lambda: guiHandler.endDataCollection(), text_color="black",
	font=("Calibria", 15))
exitButton = customtkinter.CTkButton(root,text="Exit", fg_color='red',
	command = lambda: guiHandler.shutdown(), text_color="black",
	font=("Calibria", 15))
groundStationButton = customtkinter.CTkButton(root,text="Start Rotation",
	fg_color='orange', command = lambda: guiHandler.toggleGroundStationRotation(),
	text_color="black", font=("Calibria", 15))

logger.info("Creating Buttons...")

# Create Labels
temperatureLabel = customtkinter.CTkLabel(root, text="Temperature: ", font=("Calibria", 15))
humidityLabel = customtkinter.CTkLabel(root, text="Humidity: ", font=("Calibria", 15))
pressureLabel = customtkinter.CTkLabel(root, text="Pressure: ", font=("Calibria", 15))
uvLabel = customtkinter.CTkLabel(root, text="UV: ", font=("Calibria", 15))
windDirectionLabel = customtkinter.CTkLabel(root, text="Wind Direction: ", font=("Calibria", 15))
windSpeedLabel = customtkinter.CTkLabel(root, text="Wind Speed: ", font=("Calibria", 15))

logger.info("Creating Labels...")

# Create Image
logo = ImageTk.PhotoImage(file="assets/logo.png")
logoLabel = customtkinter.CTkLabel(root, text="", image=logo)
logoLabel.image = logo
weatherStationLabel = customtkinter.CTkLabel(root, text="Weather Station GUI", font=("Calibria", 25))

logging.info("Creating Image...")

# Set Image grid
logoLabel.grid(row=0,column=1,sticky="NSEW", padx=(20, 20), pady=(20, 1))
weatherStationLabel.grid(row=1,column=1,sticky="NSEW", padx=(20, 20), pady=(1, 20))

# Set Button grid
startButton.grid(row=2,column=0,sticky="NSEW", padx=(20, 20), pady=(20, 20))
endButton.grid(row=2,column=1,sticky="NSEW", padx=(20, 20), pady=(20, 20))
exitButton.grid(row=5,column=2,sticky="NSEW", padx=(20, 20), pady=(20, 20))
groundStationButton.grid(row=2,column=2,sticky="NSEW", padx=(20, 20), pady=(20, 20))

# Set Label grid
temperatureLabel.grid(row=3,column=0,sticky="NSEW", padx=(20, 20), pady=(20, 20))
humidityLabel.grid(row=4,column=0,sticky="NSEW", padx=(20, 20), pady=(20, 20))
pressureLabel.grid(row=5,column=0,sticky="NSEW", padx=(20, 20), pady=(20, 20))
uvLabel.grid(row=3,column=1,sticky="NSEW", padx=(20, 20), pady=(20, 20))
windDirectionLabel .grid(row=4,column=1,sticky="NSEW", padx=(20, 20), pady=(20, 20))
windSpeedLabel.grid(row=5,column=1,sticky="NSEW", padx=(20, 20), pady=(20, 20))

logger.info("Setting grids...")

# Start GUI Handler
guiHandler = GUIHandler.GUIHandler(root, temperatureLabel, humidityLabel, pressureLabel,uvLabel,windDirectionLabel,windSpeedLabel,groundStationButton)

logger.info("Enabling GUIHandler...")

guiHandler.update()

# Execute tkinter
root.mainloop()

logger.info("Ending TKinter Mainloop...")
