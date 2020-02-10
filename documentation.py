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

import os
from tkinter import * # GUI Library
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

def menu():
  try:
    print("1. Process Transaction\n2. Inventory Management")
    print("3. Sales Reports\n4. Financial Records \n")
    optionSelect = int(input('Please select an option above: '))
  except ValueError:
    error("Only integer values are accepted, please try again")
    menu(" ") # Fetch from SQL. 

  if optionSelect == 1:
    transactionMenu()
  #elif optionSelect = 2:
    #inventory()
  elif optionSelect = 3:
     reports()
  else:
    error("Invalid option selected, please try again")
    menu()
   
def reports():
  print("Revenue: {0}\nExpenses: {1}\nNet income: {2}".format(revenue, expenses, netincome))
  menuReturn = input("Press enter to return to the menu.")
  if menuReturn == '':
    menu()
  

def transaction(process):
    collection = input('Collection (e.g Submariner): ')
    modelNumber = input('Model Number, as seen on website links (e.g m116610lv-0002): ')
    try:
        price = priceApi(collection, modelNumber)
        print("The {0} {1} costs ${2}".format(collection.title(),modelNumber, price['formattedPrice']))
        confirmSale = input("""Press the "ENTER" key to confirm the {}. """.format(process))

    except ValueError:
        error("Invalid collection or model number entered, please try again.")
        sale()

def transactionMenu():
  print("1. Sale\n2. Return\n 3. Menu")
  try:
      subMenuSelect = int(input('Please select an option above: '))
  except ValueError:
      error("Only integer values are accepted, please try again")
      menu() 

  if subMenuSelect == 1:
    transaction("sale")
  if subMenuSelect == 2:
    transaction("return")
  if subMenuSelect == 3:
    menu()


#--- Login GUI
gui = Tk() 
gui.title('Rolex: Employee Terminal') #
gui.geometry('350x400') 

logoLoad = ImageTk.PhotoImage(Image.open("rolex-logo.png").resize((300,225))) 
logo = Label(gui, image = logoLoad) 
logo.place(x = 23, y = -25) 



employeeNumEntry = StringVar()
employeeNumText = Label(gui, text = "Employee Number") 
employeeNumText.place(x = 27, y = 155 ) 

employeeNumAsk = Entry(gui, textvariable = employeeNumEntry, width = 47) 
employeeNumAsk.place(x = 30, y = 175) 


employeePassEntry = StringVar() 
employeePassText = Label(gui, text = "Employee Password") 
employeePassText.place(x = 27, y = 210) 

employeePassAsk = Entry(gui, textvariable = employeePassEntry, show='*', width = 47) 
employeePassAsk.place(x = 30, y = 230) 

def loginPage(): 
    employeeNum = employeeNumEntry.get().lstrip(' ') 
    employeePass = employeePassEntry.get().lstrip(' ') 
    hash = "{0}:{1}".format(employeeNum, employeePass)
    userData = open('C:/Users/ferre/Desktop/ICS4U-master/userdata.txt', 'r') 
    userDataContent = userData.read() 
    userData.close() 


    if hash in userDataContent: 
      gui.destroy() 
      print('Access granted.') 
      print("Welcome, {}.".format(username))
      menu() 


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
        
loginButton = Button(gui, text="Login", command = loginPage, width = 40) 
loginButton.place(x = 28, y = 270) 




gui.mainloop() # Runs gui.

#--- End of code.
