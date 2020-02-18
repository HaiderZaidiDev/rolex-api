#-----------------------------------------------------------------------------
# Name:        documentation.py
# Purpose:     To provide an exemplar of documentation stantards in Python.
#
# References: 	This script uses PEP-257 Docstring conventions
#				here: https://www.python.org/dev/peps/pep-0257/
#
# Author:      Haider Zaidi
# Created:     03-Feb-2020
# Updated: 2/18/2020
#-----------------------------------------------------------------------------

import os
from tkinter import * # GUI Library
from PIL import ImageTk, Image
import requests
import time

filepath = '' # Filepath of document folder, needed for database. 

def error(errorMessage):
  """Prints a customized error message on call.
  
  Keyword arguments:
  errorMessage -- The error message to be printed.
  """
  print("Error: {}.".format(errorMessage))
  time.sleep(2) # Delay to ensure error message can be read.
  os.system('cls') # Clears terminal.

def priceApi(collection, modelNumber):
  """Accesses the Rolex API to return data on a specific watch.
  
  Keyword arguments:
  collection -- The collection the Rolex belongs to.
  modelNumber -- the modelNumber of the Rolex.
  """
  masterAPI = "http://www.rolex.com/watches/{0}.api.price.{1}.CA.json".format(collection,
                                                                              modelNumber) # Inserts user input into API link.
  pageData = requests.get(masterAPI).json() 
  return pageData

def priceCheck():
  """Returns the price of a Rolex given its collection and model number."""
    collection = input('Collection (e.g Submariner): ')
    modelNumber = input('Model Number, as seen on website links (e.g m116610lv-0002): ')
    price = priceApi(collection, modelNumber)
    print("The {0} {1} costs ${2}".format(collection.title(),
                                          modelNumber, 
                                          price['formattedPrice'])) # Outputs the formatted price of the Rolex.
        
# Login GUI. 
gui = Tk() 
gui.title('Rolex: Employee Terminal') 
gui.geometry('350x400') # Sets size of terminal, pixel dimensions.

logoLoad = ImageTk.PhotoImage(Image.open("rolex-logo.png").resize((300,225))) 
logo = Label(gui, image = logoLoad) 
logo.place(x = 23, y = -25) # Aligns logo to top center. 

employeeNumAsk = Entry(gui, textvariable = employeeNumEntry, width = 47) # Employee number input box. 
employeeNumAsk.place(x = 30, y = 175) # Aligns input box to middle center.

employeeNumEntry = StringVar()
employeeNumText = Label(gui, text = "Employee Number") # Employee number label.
employeeNumText.place(x = 27, y = 155 ) # Aligns text to middle center, above input box. 

employeePassAsk = Entry(gui, textvariable = employeePassEntry, show='*', width = 47) # Employee password input box.
employeePassAsk.place(x = 30, y = 230) # Aligns middle center, below employee number input box. 

employeePassEntry = StringVar() 
employeePassText = Label(gui, text = "Employee Password")  # Employee password label.
employeePassText.place(x = 27, y = 210)  # Aligns middle center, above employee password input box. 


def loginPage(): 
  """Verifies credentials inputted through the GUI.
  
  Keyword arguments:
  hash -- Formatted login credentials provided by the user.
  userData -- Database of login credentials (plain text).
  failedAttempts -- Count of invalid login attempts. 
  """
    employeeNum = employeeNumEntry.get().lstrip(' ') 
    employeePass = employeePassEntry.get().lstrip(' ') 
    hash = "{0}:{1}".format(employeeNum, 
                            employeePass) # Formats input to match database.
    userData = open('{}/userdata.txt'.format(filepath), 'r') 
    userDataContent = userData.read() 
    userData.close() 

    if hash in userDataContent: 
      gui.destroy() # Closes GUI window. 
      print('Access granted.') 
      print("Welcome, {}.".format(username))
      priceCheck() 

    else: 
      failedAttempts['failed'] += 1 
      attemptsRemaining = 3 - failedAttempts['failed'] 
      
      if failedAttempts['failed'] == 3: 
        print('Maximum failed attempts reached, you have been locked out of the terminal.') 
        time.sleep(2)
        sys.exit() 
      else:
        print('Incorrect agent number/password entered, try again. You have ' + str(attemptsRemaining) + ' attempts remaining.')
        os.system('cls') 
        
loginButton = Button(gui, text="Login", command = loginPage, width = 40) # Login button.
loginButton.place(x = 28, y = 270) 

gui.mainloop() # Runs gui.

#--- End of code.
