# HackItAll Elimination Round

This is a code implementation of a vending machine designed to allow the sale
of Avira products to students.

## Classes

The following classes were implemented in the design of this app:

* **Product**: defines the properties of each item on sale
	* *Name*: the get(*self*) and set(*self, name*) methods in this category
				set and return the nameof a product
	* *Price*: this method category is split into a get(*self*) and a 
				set(*self, price*) method that update and retrieve the given
				price of a product
* **Cash**: defines the methods used in cash payments
	* On initialization of an object, a dictionary containing each type of 
	currency that can be used. This dictionary will be used to keep track of
	all the currency inserted into the machine
	* *insertMoney(self, amount)*: adds inserted currency to the dictionary
	* *getChange(self, currentcredit, totalcartvalue)*: gives back owed change
	* *getMoney(self)*: returns the total ammount of currency inserted
* **Card**: defines methods used for card payments
	* On initialization of an object, a preset card balance and pin are set up
	(this is done only for the purpose of this implementation)
	* *checkFunds(self, price)*: checks to determine if the selected items are 
	affordable based on card balance
	* *checkPin(sef, givepin)*: checks to see if inputted pin is correct
* **VendingMachine**: this class is the core of the machine; it is set up as a
	singleton class so there can only be one object of this type
	* On initialization, this class sets up all of the available products, creates a dictionary with the prices of each item as well as a dictionary
	with the number of products contained in the machine
	* *getCredit(self)*: returns credit available to the user
	* *getNo< product_name >(self)*: returns the existing amount for each
	product
	* *getPrice< product_name >(self)*: returns the price for each item
* **Button(object)**: this class defines a button object for use in UI
	* On initializition the button is place at it's respective coordinates on
	the screen, it's size is defined, it gets given a name and an image to
	display
	* *draw(self,screen)*: this method is called every frame to have the button
	redrawn
	* *event_handler(self, event)*: this method handles what happens when the
	button is clicked
* **PaymentButton(Button)**: this class defines the button type for the buttons
	used in selecting the payment methods
	* On initialization the same setup is performed as for the standard button 
	class defined above
	* *event_handler(self, event)*: this method handles what happens when the
	button is clicked
* **Text**: defines the label-style objects used to display text
	* On initialization the font style and size, text and position are set up
	* *draw(self, screen)*: this method is used to redraw and update the label
	every frame
* **PriceText(Text)**: this defines the labels that are used for displaying UI
	text
	* On initialization these labels have the same setup as defined in the 
	generic text label class 

* **CoinsText(Text)**: this defines a clickable label that is used to display 
	each increment of currency accepted
	* On initialization these labels use the same setup as defined in the
	generic text label class the only difference being that these posses a 
	value and are clickable
	* *event_handler(self,event)*: this method handles what happens when the 
	labels are clicked

* **TextButton(Text)**: this defines a clickable label for each product
	* On initialization these labels use the same setup as defined in the
	generic text label class the only difference being that these posses a 
	value and are clickable
	* *event_handler(self,event)*: this method handles what happens when the 
	labels are clicked
