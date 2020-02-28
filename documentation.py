#-----------------------------------------------------------------------------
# Name:        documentation.py
# Purpose:     To provide an exemplar of documentation stantards in Python.
#
# References: 	This script uses PEP-257 Docstring conventions found
#               here: https://www.python.org/dev/peps/pep-0257/
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
failedAttempts = {'failed': 0} # Count of failed login attempts. 

def error(errorMessage):
  """Outputs a customized fail message.

  Parameters
  ----------
  errorMessage: str
                The error message to be printed.

  """
  print("Error: {}.".format(errorMessage))
  time.sleep(2) # Delay to ensure error message can be read.
  os.system('cls') # Clears terminal.

def priceApi(collection, modelNumber):
  """Returns data from the Rolex API on a given watch.

  Fetches data, primarily concerning the price, of a
  Rolex watch given the collection and model number
  gathered in priceCheck().

  Parameters
  ----------
  collection: str
            The collection which the Rolex belongs to (e.g Submariner).
  modelNumber: str
            The model number of the specified Rolex.
  Returns
  -------
  pageData: dict
            API data containing information regarding the price
            of the watch specified.

  Raises
  ------
  JSONDecodeError
        If the collection or model number is invalid.

  """
  masterAPI = "http://www.rolex.com/watches/{0}.api.price.{1}.CA.json".format(collection,
                                                                              modelNumber) # Inserts user input into API link.
  pageData = requests.get(masterAPI).json()
  return pageData

def priceCheck():
  """Outputs the price of a Rolex given its collection and model number.
  """
  collection = input('Collection (e.g Submariner): ')
  modelNumber = input('Model Number, as seen on website links (e.g m116610lv-0002): ')
  price = priceApi(collection, modelNumber)
  print("The {0} {1} costs ${2}".format(collection.title(), modelNumber,
                                            price['formattedPrice'])) # Outputs the formatted price of the Rolex.

# Login GUI.
gui = Tk()
gui.title('Rolex: Employee Terminal')
gui.geometry('350x400') # Sets size of terminal, pixel dimensions.

logoLoad = ImageTk.PhotoImage(Image.open("rolex-logo.png").resize((300,225))) #Resizes logo to fit terminal.
logo = Label(gui, image = logoLoad)
logo.place(x = 23, y = -25) # Aligns logo to top center.

employeeNumEntry = StringVar()
employeeNumText = Label(gui, text = "Employee Number") # Employee number label.
employeeNumText.place(x = 27, y = 155 ) # Aligns text to middle center, above input box.

employeeNumAsk = Entry(gui, textvariable = employeeNumEntry, width = 47) # Employee number input box.
employeeNumAsk.place(x = 30, y = 175) # Aligns input box to middle center.

employeePassEntry = StringVar()
employeePassText = Label(gui, text = "Employee Password")  # Employee password label.
employeePassText.place(x = 27, y = 210)  # Aligns middle center, above employee password input box.

employeePassAsk = Entry(gui, textvariable = employeePassEntry, show='*', width = 47) # Employee password input box.
employeePassAsk.place(x = 30, y = 230) # Aligns middle center, below employee number input box.


def loginPage():
  """Verifies credentials inputted through the GUI.

  Fetches the user's credentials from the GUI (Tkinter),
  formats the data and then authenticates it by scanning
  against a database of all user credentials. Exits script
  if the user's credentials could not be authenticated
  after 3 attempts.

  Warnings
  --------
  The database system stores user credentials in plain text,
  using essentially zero information security measures.

  Notes
  -----
  It would be beneficial to migrate the database system from
  a text a file to an SQL database (e.g SQLite 3); allowing for a more
  efficient and professional method of storing data.

  """
  employeeNum = employeeNumEntry.get().lstrip(' ')
  employeePass = employeePassEntry.get().lstrip(' ')
  # Formats input to match database.
  hash = "{0}:{1}".format(employeeNum,employeePass)
  userData = open('{}/userdata.txt'.format(filepath), 'r')
  userDataContent = userData.read()
  userData.close()

  if hash in userDataContent:
    gui.destroy() # Closes GUI window.
    print('Access granted.')
    print("Welcome, {}. \n".format(employeeNum))
    priceCheck()

  else:
      failedAttempts['failed'] += 1
      attemptsRemaining = 3 - failedAttempts['failed'] # Counts number of remaining login attempts.

      if failedAttempts['failed'] == 3:
          print('Maximum failed attempts reached, you have been locked out of the terminal.')
          time.sleep(2)
          sys.exit()

      print('Incorrect agent number/password entered, try again. You have ' + str(attemptsRemaining) + ' attempts remaining.')
      time.sleep(2)
      os.system('cls')

loginButton = Button(gui, text="Login", command = loginPage, width = 40) # Login button.
loginButton.place(x = 28, y = 270) # Aligns login button middle bottom.

gui.mainloop() # Runs gui.

#--- End of code.
