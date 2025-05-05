#WORKS

#shopping_list = ['milk', 'apples', 'oranges', 'potatoes', 'bread']

#Use the append method to add bananas to your list
#shopping_list.append('bananas')
#Print your shopping list
#print(shopping_list)

#Use insert method to add onions at a specific position in your list
#shopping_list.insert(2,'onions')

#Print your shopping list
#print(shopping_list)

#Use the remove method to remove potatoes from the list
#shopping_list.remove('potatoes')
#Print your shopping list
#print(shopping_list)

#Expand your list by adding tuples for each item
#shopping_list = [('milk', 'dairy'), ('apples', 'fruits'), ('onions', 'vegetables'), ('oranges', 'fruits'), ('bread','bakery'), ('bananas', 'fruits')]

#Use for loop to iterate over list and get each tuple for unpacking
#for element in shopping_list:
  #unpack the tuple into item and section variables 
  #item, section = element
  #print the message
  #print("You can find the",item,"in the",section,"section.")


#Create a dictionary which contains the item as key and the section as value
#shopping_list = {'milk':'dairy', 'apples':'fruits', 'onions':'vegetables', 'oranges':'fruits', 'bread':'bakery', 'bananas':'fruits'}

#Print the keys
#print(shopping_list.keys())

#Print the values
#print(shopping_list.values())

#Print the key/value pairs
#print(shopping_list.items())



# SUPERMARKET SYSTEM

#Create a dictionary for your inventory

inventory = {'Milk':[4,1000,'dairy'],
             
             'Apples':[2,3,'fruits'],

             'Onions':[1,50,'vegetables'],

             'Oranges':[1.5,1000,'fruits'],

             'Bread':[3,100,'bakery'],

             'Bananas':[5,300,'fruits']} 


#Create a shopping list that specifies how much of each item you want to purchase
shopping_list = [('milk',1), ('apples',4), ('onions', 5), ('oranges',5), ('bread',2), ('bananas',10)]


#Define the check_stock function
def check_stock(shopping_list, inventory):
  #Create the empty shopping_list_updated
  updated_shopping_list = []
  #Write a for loop to iterate over each item in your shopping list
  for element in shopping_list:
    item, amount = element
    #Access the available stock in your inventory
    inventory_value = inventory[item]
    if amount > inventory_value[1]:
      amount = inventory_value[1]
      print("We dont have enough stock of", item,"you can buy a maximum amount of",inventory_value[1])
    #append item and amount to your updated shopping list
    updated_shopping_list.append((item,amount))
  return updated_shopping_list


#Define the compute_bill function
def compute_bill(updated_shopping_list, inventory):
  #Create a bill variable that equals 0
  bill = 0
  #Write a for loop to iterate over each item in your updated shopping list
  for element in updated_shopping_list:
    item, amount = element
    #access the price in your inventory
    inventory_value= inventory[item]
    #Compute the price and add it to the bill
    bill += inventory_value[0] * amount
  return bill


#Define the update_stock function 
def update_stock(updated_shopping_list, inventory):
  #Write a for loop to iterate over each item in your updated shopping list
  for element in updated_shopping_list:
    item, amount = element
    #access the stock in your inventory
    inventory_value = inventory[item]
    #Decrease the stock by the amount that was purchased
    inventory_value[1] = inventory_value[1] - amount
  
  return inventory


#Call check_stock function for your shopping list
updated_shopping_list = check_stock(shopping_list, inventory)
print("Your updated shopping list:", updated_shopping_list)

#Call the compute_bill function for your updated shopping list
bill = compute_bill(updated_shopping_list, inventory)
print("Total price:",bill,"$")

#Call the update_stock function for your updated shopping list
new_inventory = update_stock(updated_shopping_list, inventory)
print("The inventory was updated:", new_inventory)