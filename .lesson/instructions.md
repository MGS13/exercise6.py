# Exercise 06: Manipulating Data in a List
With the core functionality out of the way the NEAs often then ask you to extend the program with an ability to change or delete records, this could be anything from amending an order to deleting customers; regardless we need to develop a strategy to look for records in our 2D `list` because `if this in that` isn't going to work when the data structure is in 2D!

## Back to the Games Rentals
It's our old friend, the games rental store, back in new and improved code form. It uses nearly all the features we've looked at so far including menus, a 2D `list`, autosave and autoload and even has an emoji chucked in for added value.

Take a look at the code below, but it should be quite familiar to you.

```python
import time, os

gameRentals = []

try:
  f = open("rentals.txt", "r")
  gameRentals = eval(f.readline())
  f.close()
except:
  pass

def addRental():
  customer = input("Customer: ")
  item = input("Game: ")
  price = float(input("Price per night: "))
  nights = int(input("Nights: "))
  total = round(price*nights,2)
  returned = False

  row = [customer, item, price, nights, total, returned]
  gameRentals.append(row)

  print("Added successfully")
  time.sleep(1)

def viewRentals():
  print("RENTAL HISTORY")
  for row in gameRentals:
    for item in row:
      print(item, end="\t")
    print()
  time.sleep(1)

while(True):
  print("🎮 GAME RENTALS 🎮")
  print("   ===========")
  print("Press 1 to add new Rental")
  print("Press 2 to view Rentals")
  menuChoice = input("> ")

  if(menuChoice=="1"):
    addRental()
  elif(menuChoice=="2"):
    viewRentals()
  else:
    print("ERROR: Unknown Option")
    time.sleep(1)
  
  time.sleep(1)
  os.system('clear')

  f = open("rentals.txt", "w")
  f.write(str(gameRentals))
  f.close()

```

When the program is run it greets us with this lovely emoji laden menu.

```
🎮 GAME RENTALS 🎮
   ===========
Press 1 to add new Rental
Press 2 to view Rentals
> 
```

If a user decides to add a rental to the system they are asked a series of questions where the total cost is worked out and then stored in a 2D `list`.

```
🎮 GAME RENTALS 🎮
   ===========
Press 1 to add new Rental
Press 2 to view Rentals
> 1
Customer: Sian Jones
Game: Sea of Thieves
Price per night: 0.99
Nights: 14
Added successfully
```

Autosave and autoload have been implemented such that the file `rental.txt` looks like this after adding one more enty.

```python
[['Yana Pepperidge', 'Super Mario 3D All Stars', 1.99, 5, 9.95, False], ['Eric Magnusson', 'Spider-Man: Miles Morales', 2.99, 3, 8.97, False], ['Sian Jones', 'Sea of Thieves', 0.99, 14, 13.86, False]]
```

As you can see there are three records for rentals, all including all the information taken in or calculated when the rental was added, and if we go back to the menu and select option 2 to view the rentals we get:

```
🎮 GAME RENTALS 🎮
   ===========
Press 1 to add new Rental
Press 2 to view Rentals
> 2
RENTAL HISTORY
Yana Pepperidge  	Super Mario 3D All Stars     	1.99    5   9.95    False
Eric Magnusson   	Spider-Man: Miles Morales    	2.99    3   8.97    False
Sian Jones  	   	Sea of Thieves  			  	0.99    14  13.86   False
```

This wonderful pretty print which includes an interesting value at the end, what's that `False` doing there? Well turns out we've set it when we were taking in the user data, in the code you'll see the line `returned = False` which lets us know if the game has been returned, we're setting it to `False` by default because we know that when we're doing the data entry we are starting the rental so it won't be returned for a while.

A common question then might be

```
Add a function to allow a member of staff to mark a rental as 'returned' when it is brought back to the shop
```

How exactly do we go about doing that? 

## Changing the Menu

Well before we panic about it the first thing to do is to go into the menu code and add an option to allow us to mark the item as 'returned', this can be done quite easily by adding a new `print` command to the menu, and adding one more `elif`.

```python
…
while(True):
  print("🎮 GAME RENTALS 🎮")
  print("   ===========")
  print("Press 1 to add new Rental")
  print("Press 2 to view Rentals")
  print("Press 3 to mark item as returned")
  menuChoice = input("> ")

  if(menuChoice=="1"):
    addRental()
  elif(menuChoice=="2"):
    viewRentals()
  elif(menuChoice=="3"):
    markReturned()
  else:
    print("ERROR: Unknown Option")
    time.sleep(1)
  …
```

So, we've added another print statements `print("Press 3 to mark item as returned")` to increase the menu options, then we had to deal with the selection of option three with a simple `elif(menuChoice=="3"):` and pointed that at a subroutine that we haven't written yet `markReturned()`.

We can also pop up to the top of the code and produce a blank definition for the `markReturned()` subroutine by using the `pass` command as a filler.

```python
def markReturned():
  pass
```

## Building the Search
At this point you need to ask yourself "What do I need to search for to find the record I'm changing?", this is absolutely key because you need to be able to reliably find what you're looking for. 

```python
def markReturned():
  customer = input("Customer: ")
  item = input("Game: ")
```

In our code we'll be needing the customer name and the item name, at the very least, to find the record so we'll pull those in as variables using bog-standard `input()` commands.

The next step will be to use a loop to go through each row of the 2D `list` so that we can look at the values of the fields, and at this point it's a good idea to go back to your original designs for the `list`. When we want to access any of the fields we will need to use the **index number** of the field - if you've done your design you can just add that from left-to-right, starting at 0.

```python
def markReturned():
  customer = input("Customer: ")
  item = input("Game: ")
  for row in gameRentals:
    if(row[5]==False):
      pass
```

The loop we've used is pretty standard, `for row in gameRentals:` just iterated through the `list` and pulls out each row as the variable `row`. The `if` statement if the first of the very clever things, now since we've been asked to look for a record to change the 'returned' value, we should really only be looking for those that are *not* returned. In our diagram we've said that 'returned' was index **5**, so `if(row[5]==False):` will only select those rentals that haven't yet been returned.

The `pass` command is a placeholder for the next stage, so let's start matching up the fields we've asked the user to type in: starting with customer, again checking our original diagram we'll see that we've placed the customer name in index **0**.

```python
def markReturned():
  customer = input("Customer: ")
  item = input("Game: ")
  for row in gameRentals:
    if(row[5]==False):
      if(row[0].lower()==customer.lower()):
        pass
```

We've got a nice nested `if` statement here with a few different parts, firstly `row[0].lower()` will give us the lowercase version of the customer name in this record, that's being compared with `==` to the lowercase version of the customer we're searching for `customer.lower()`. If this `if` statement activates it's because this record contains the customer we're searching for.

So that's two out of three search terms completed, let's replace the `pass` placeholder with the next search term, the name of the game. 

```python
def markReturned():
  customer = input("Customer: ")
  item = input("Game: ")
  for row in gameRentals:
    if(row[5]==False):
      if(row[0].lower()==customer.lower()):
        if(row[1].lower()==item.lower()):
          pass
```

Another `if` statement here that works much the same as the last one, `row[1].lower()` is the index of the game name in the record, converted to lowercase, and it's being compared to `item.lower()` the lowercase version of the item variable we're searching for. If this condition is matched then that means that the name of the game in this record is the one we're searching for.

Okay, that means that the three search criteria we've decided upon are matched, that must mean this is the record we want to change… how do we do that?

```python
def markReturned():
  customer = input("Customer: ")
  item = input("Game: ")
  for row in gameRentals:
    if(row[5]==False):
      if(row[0].lower()==customer.lower()):
        if(row[1].lower()==item.lower()):
          row[5]=True
          print("Updated successfully")
			time.sleep(1)
```

Turns out it was quite straight forward, we're just setting the index of the 'returned' field to `True` instead of `False` and that's what `row[5]=True` is all about.  The rest of the code is just to make the user experience (UX) better. 

So, if the program is executed and we select the new option we're asked to enter a customer and a game. The search function runs and, if it finds a record, it tells us and makes the changes.

```
🎮 GAME RENTALS 🎮
   ===========
Press 1 to add new Rental
Press 2 to view Rentals
Press 3 to mark item as returned
> 3
Customer: Sian Jones
Game: Sea of Thieves
Updated successfully
```

Now here's the fun bit - all these changes are *automatically* pushed into the save file by our autosave code. That was definitely worth doing then, wasn't it?

If we then try and  run the program and selection option 2 you can see that the 'returned' column has been amended as we tried.

```
🎮 GAME RENTALS 🎮
   ===========
Press 1 to add new Rental
Press 2 to view Rentals
Press 3 to mark item as returned
> 2
RENTAL HISTORY
Yana Pepperidge  	Super Mario 3D All Stars     	1.99    5   9.95    False
Eric Magnusson   	Spider-Man: Miles Morales    	2.99    3   8.97    False
Sian Jones  	   	Sea of Thieves  			  	0.99    14  13.86   True
```

The changes that you are asked to make are usually very simple, they might even require you to recalculate a cost but come on - you've got this - just take you time and think through what you need to ask the user for to find the record, and what do you need to make the changes.

The complete code for this working program is below, get it running, fiddle with it, prod it, see what it does.

```python
import time, os

gameRentals = []

try:
  f = open("rentals.txt", "r")
  gameRentals = eval(f.readline())
  f.close()
except:
  pass

def addRental():
  customer = input("Customer: ")
  item = input("Game: ")
  price = float(input("Price per night: "))
  nights = int(input("Nights: "))
  total = round(price*nights,2)
  returned = False

  row = [customer, item, price, nights, total, returned]
  gameRentals.append(row)

  print("Added successfully")
  time.sleep(1)

def viewRentals():
  print("RENTAL HISTORY")
  for row in gameRentals:
    if(row[5]==False):
      for item in row:
        print(item, end="\t")
    print()
  time.sleep(1)

def markReturned():
  customer = input("Customer: ")
  item = input("Game: ")
  for row in gameRentals:
    if(row[5]==False):
      if(row[0].lower()==customer.lower()):
        if(row[1].lower()==item.lower()):
          row[5]=True
          print("Updated successfully")
          time.sleep(1)

while(True):
  print("🎮 GAME RENTALS 🎮")
  print("   ===========")
  print("Press 1 to add new Rental")
  print("Press 2 to view Rentals")
  print("Press 3 to mark item as returned")
  menuChoice = input("> ")

  if(menuChoice=="1"):
    addRental()
  elif(menuChoice=="2"):
    viewRentals()
  elif(menuChoice=="3"):
    markReturned()
  else:
    print("ERROR: Unknown Option")
    time.sleep(1)
  
  time.sleep(1)
  os.system('clear')

  f = open("rentals.txt", "w")
  f.write(str(gameRentals))
  f.close()

```


## Your Task
Use the starting code in `main.py` which forms the basis of a program for a parcel delivery company. You will need to extend the program in the following ways:

1. Add an option to the menu that searches through the deliveries and displays any parcels that have not yet been delivered

2. Add an option to the menu that searches for a particular parcel to update it to mark it as delivered

3. Add an option to the menu to change the contact telephone number for a parcel delivery

### Extensions

4. Copy the final version of the Games Rental program from above and extend it so that it includes a function that *only* displays rentals that *have* been returned. An example of how the program should work is below.

```
🎮 GAME RENTALS 🎮
   ===========
Press 1 to add new Rental
Press 2 to view Rentals
Press 3 to mark item as returned
Press 4 to view Rentals that have been returned
> 4
RENTAL HISTORY (NOT RETURNED)
Yana Pepperidge  	Super Mario 3D All Stars     	1.99    5   9.95    False
Eric Magnusson   	Spider-Man: Miles Morales    	2.99    3   8.97    False
```

  