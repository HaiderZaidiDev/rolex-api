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

def error(errorMessage):
  print("Error: {}.".format(errorMessage))
  os.system('cls')

def menu(str(username)):
  print("Welcome, {].".format(username))
  try:
    optionSelect = int(input('Please select an option below: '))
  except valueError:
    error(Only integer values are accepted, please try again)
    menu()
    
  print("""
  1. Process Transaction \n
  2. Inventory Management \n
  3. Sales Reports
  """)
  
  if optionSelect = 1:
    transactions()
  elif optionSelect = 2:
    inventory()
  elif optionSelect = 3:
    reports()
  else:
    error("Invalid option selected, please try again")
    menu()

def transactions():
  subMenuSelect = input('Please select an option below: ')
  print("""
  1. Sale \n
  2. Return
  """)
  
  if subMenuSelect = 1:
    sale()
  elif subMenuSelect = 2:
    refund()
  
  def sale():
    
    
  
  
def login():
  username = input('Username: ')
  password = input('Password: ')
  hash = '{}:{}'.format(username, password) # Format for verificiation.
  failedAttempts = 0
  userData = open('userdata.txt', 'r')
  userDataContent = userData.read()
  userdata.close()
  
  if hash in userDataContent:
    menu(username)
  
  else:
    failedAttempts +=1
    attemptsRemaining = 3 - failedAttempts
    if failedAttempts = 3:
      error(Access denied, 
     exit()
login()
     
    
