#REPLex Deliveries system
import time, os

deliveries = []

try:
  f = open("deliveries.txt", "r")
  deliveries = eval(f.readline())
  f.close()
except:
  pass

def addDelivery():

  customerName = input("Customer Name: ")
  contactTel = input("Contact telephone: ")
  address = input("Address: ")
  delivered = False

  row = [customerName, contactTel, address, delivered]
  deliveries.append(row)

  print("Added Successfully")
  time.sleep(1)

def showDeliveries():

  print()
  print("-=   D E L I V E R I E S    =-")
  for row in deliveries:
    for item in row:
      print(item, end="\t")
    print()
  time.sleep(1)

#Splash Screen
print('''
▒█▀▀█ ▒█▀▀▀ ▒█▀▀█ ▒█░░░ █▀▀ █░█ 
▒█▄▄▀ ▒█▀▀▀ ▒█▄▄█ ▒█░░░ █▀▀ ▄▀▄ 
▒█░▒█ ▒█▄▄▄ ▒█░░░ ▒█▄▄█ ▀▀▀ ▀░▀

Some deliveries on time, others lost forever…''')
time.sleep(1)
os.system('clear')

while(True):

  print("🅁🄴🄿🄻🄴🅇")
  print("Press a number to select an option")
  print("1: Add Delivery")
  print("2: View Deliveries")
  #You probably want to start here

  menuChoice = input("> ")

  if(menuChoice=="1"):
    addDelivery()
  elif(menuChoice=="2"):
    showDeliveries()
  else:
    print("ERROR: Not a valid selection")

  time.sleep(1)
  os.system('clear')

  f = open("deliveries.txt", "w")
  f.write(str(deliveries))
  f.close()