# grocery-bill-using-python
i will try to make a code for a grocery shop bill making system.
 **hear is the reforence link below:** 
https://www.geeksforgeeks.org/creating-a-receipt-calculator-using-python/


**Project Details: Creating a Receipt Calculator using Python**
A receipt calculator is generally a slip in which the total invoice along with their names is mentioned. We will use the class PrettyTable inside the prettytable library for making our receipt calculator.

What is PrettyTable ?
It is a class present inside prettytable library which help us to make relational tables in Python.  

**Installation of library:**

pip install prettytable

**Generating PrettyTable :**

_Initialisation :_

<table name> = PrettyTable(['<column1>','<column2>',....])

To add a row :
add_row(['<row1>','<row2>',....])
  
**Approach :**

There will be two columns: Item Name & Item Price. 

We will keep taking item name and item price (in new line) 
Until the user enters ‘q’ and store the price in another variable name ‘total’ initialized as 0. When user
Enters ‘q’, program will stop taking inputs and ret![Uploading geeeeeks.png…]()
urn the table along with the total amount specified at the end.
  

![image](https://user-images.githubusercontent.com/103409816/163105483-f520063f-cb7b-414f-9b72-2a77a7d80294.png)

  
