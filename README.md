# HackItAll Elimination Round

This is a code implementation of a vending machine designed to allow the sale
of Avira products to students.

## Classes

The following classes were implemented in the design of this app:

* **Product**: defines the properties of each item on sale
	Methods:
	* *Name*: the get and set methods in this category set and return the name
				of a product
	* *Price*: this method category is split into a get and a set method that
				update and retrieve the given price of a product
* **Cash**: defines the methods used in cash payments
	Methods:
	* On initialization of an object, a dictionary containing each type of 
	currency that can be used. This dictionary will be used to keep track of
	all the currency inserted into the machine
	* *insertMoney*: adds inserted currency to the dictionary
	* *getChange*: gives back owed change
	* *getMoney*: returns the total ammount of currency inserted

