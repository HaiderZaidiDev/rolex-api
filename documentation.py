#-----------------------------------------------------------------------------
# Name:        documentation.py
# Purpose:     To provide an exemplar of documentation stantards in Python.
#
# References: 	This script uses the PEP-8 style guide
#				here: https://www.python.org/dev/peps/pep-0008/
#
# Author:      Haider Zaidi
# Created:     03-Feb-2020
# Updated:
#-----------------------------------------------------------------------------

## Watches
import os
from tkinter import *
from PIL import ImageTk, Image
revenue = 0
expenses = 0
netIncome = revenue - expenses


inventory = {}
def error(errorMessage):
  print("Error: {}.".format(errorMessage))
  os.system('cls')

def priceApi(collection, modelNumber):
  import requests
  masterAPI = "http://www.rolex.com/watches/{0}.api.price.{1}.CA.json".format(collection, modelNumber)
  pageData = requests.get(masterAPI).json()
  return pageData

def menu(username):
  print("Welcome, {}.".format(username))
  try:
    print("1. Process Transaction\n2. Inventory Management")
    print("3. Sales Reports\n4. Financial Records \n")
    optionSelect = int(input('Please select an option above: '))
  except ValueError:
    error("Only integer values are accepted, please try again")
    menu("Yeet-Master")

  if optionSelect == 1:
    transactions()
  #elif optionSelect = 2:
    #inventory()
  #elif optionSelect = 3:
    #reports()
  else:
    error("Invalid option selected, please try again")
    menu()

def sale():
    collection = input('Collection (e.g Submariner): ')
    modelNumber = input('Model Number, as seen on website links (e.g m116610lv-0002): ')
    try:
        price = priceApi(collection, modelNumber)
        print("The {0} {1} costs ${2}".format(collection.title(),modelNumber, price['formattedPrice']))
        confirmSale = input("""Press the "ENTER" key to confirm the sale. """)

    except ValueError:
        error("Invalid collection or model number entered, please try again.")
        sale()

def transactions():
  print("1. Sale\n2. Return")
  try:
      subMenuSelect = int(input('Please select an option above: '))
  except ValueError:
      error("Only integer values are accepted, please try again")
      menu("Yeet-Master")

  if subMenuSelect == 1:
    sale()


#--- Login GUI
gui = Tk() # Assigns Tk() to variable gui.
gui.title('Rolex: Employee Terminal') # Sets title of gui.
gui.geometry('350x400') # Sets size of gui.

logoLoad = ImageTk.PhotoImage(Image.open("rolex-logo.png").resize((300,225))) # Loads FBI-Command-Terminal logo.
logo = Label(gui, image = logoLoad) # Displays FBI-Command-Terminal logo.
logo.place(x = 23, y = -25) # Alignment of logo in pixels.



employeeNumEntry = StringVar() # Variable to get user input of agent number.
employeeNumText = Label(gui, text = "Employee Number") # Displays agent number label.
employeeNumText.place(x = 27, y = 155 ) # Aligns agent number label in pixels.

employeeNumAsk = Entry(gui, textvariable = employeeNumEntry, width = 47) # Creates input field for agent number.
employeeNumAsk.place(x = 30, y = 175) # Aligns agent number input field in pixels


employeePassEntry = StringVar() # Variable to get user input of dept. passwords
employeePassText = Label(gui, text = "Employee Password") # Displays dept. pass label.
employeePassText.place(x = 27, y = 210) # Aligns dept. pass label in pixels.

employeePassAsk = Entry(gui, textvariable = employeePassEntry, show='*', width = 47) # Creates input field for dept. pass, hides input with asteriks.
employeePassAsk.place(x = 30, y = 230) # Aligns dept. pass input field in pixels.

def loginPage(): # Defines function loginPage()
    employeeNum = employeeNumEntry.get().lstrip(' ') # Gets employeeNum from employeeNumEntry.
    employeePass = employeePassEntry.get().lstrip(' ') # Gets employeePass from employeePassEntry.
    hash = "{0}:{1}".format(employeeNum, employeePass)
    userData = open('C:/Users/ferre/Desktop/ICS4U-master/userdata.txt', 'r') # Opens userdata.txt (location of usernames and passwords)
    userDataContent = userData.read() # Reads userdata.txt
    userData.close() # Closes all operations on userdata.txtdocu


    if hash in userDataContent: # If the user's login information is located in the userdata file, the following code is executed.
      gui.destroy() # Closes the gui.
      print('Access granted.') # Prints access granted message in bright green.
      menu("Yeet Master") # Calls the menu function.


    else: # If the user's login information isn't located in the userdata file, the following code is executed.
      failedAttempts['failed'] += 1 # Adds 1 to the key value of dictionary failedAttempts (counts how many times the user inputted invalid credentials)
      attemptsRemaining = 3 - failedAttempts['failed'] # Variable for amount of attempts the user has left before their locked out the system.
      print() # Prints blank space.

      if failedAttempts['failed'] == 3: # If the user has entered invalid credentials 3 times, the following code is executed.
        print('Maximum failed attempts reached, you have been locked out of the terminal.') # Notifies user that they've been locked out of the terminal.
        time.sleep(2) #  Adds a 2 second delay before the next line of code is executed.
        sys.exit() # Exits terminal.

      if employeeNum.isupper() or employeePass.isupper(): # If the user's agent number or password is in all uppercase chars the following code is executed.
          print('Incorrect agent number/password entered, try again. You have ' + str(attemptsRemaining) + ' attempts remaining.' + '\nNote: ' + 'It appears that your capslock is on, if this is a mistake make sure to disable it!') # Notifies the user of remaining login attempts and that they may have capslock on.
          time.sleep(2) # Adds a 2 second delay before the next line of code is executed.
          os.system('cls') # Clears the console.
      print() # Prints a blank space.
      print('Incorrect agent number/password entered, try again. You have ' + str(attemptsRemaining) + ' attempts remaining.') # Prints an error message and remaining login attempts.
      time.sleep(3) # Adds a 3 second delay before the next line of code is executed.
      os.system('cls') # Clears the console.
loginButton = Button(gui, text="Login", command = loginPage, width = 40) # Login button for the gui, when clicked, the function loginPage is ran.
loginButton.place(x = 28, y = 270) # Alignment of loginButton in pixels.




gui.mainloop() # Runs gui.

#--- End of code.
