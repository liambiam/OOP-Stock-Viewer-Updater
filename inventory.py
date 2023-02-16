
from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity): # Initialiser, with instances
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):             # Forgot I had these
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):                                          # Str output for printing
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"


#=============Shoe list===========

shoe_list = []                                          # Store a list of objects of shoes

#==========Functions outside the class==============
def read_shoes_data():
    while True:       
        try:
            with open(f'inventory.txt', 'r') as i:
                data = i.readlines()

            list_of_shoes = []                          # Each Shoe line is in it's own list, in list_of_shoes                         
            for i in data:                 
                i_list = i.split(",")            
                list_of_shoes.append(i_list) 
            list_of_shoes.pop(0)                        # Remove first 'categories' line

            for i in range(len(list_of_shoes)):         # Assign data to respective class instance
                country = list_of_shoes[i][0]
                code = list_of_shoes[i][1]
                product = list_of_shoes[i][2]
                cost = list_of_shoes[i][3]
                quantity = int(list_of_shoes[i][4])
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
            break
        
        except FileNotFoundError:                       # If no inventory.txt file exists
            print("No file of that name exists, generating empty file")
            with open(f'inventory.txt', 'w') as i:
                i.write("")
            break

def capture_shoes():
    while True:

        new_country = input("Enter the new shoe Country: ")         # New data input
        new_code = input("Enter the new shoe code: ")
        new_product = input("Enter the new shoe product name: ")
        
        while True:                                                 # Ensure ints input
            try:
                new_cost = int(input("Enter the new shoe cost (numbers only): "))
                break
            except ValueError:
                print("Integers only please, try again")
        
        while True:
            try:
                new_quantity = int(input("Enter the new shoe quantity: "))
                break
            except ValueError:
                print("Integers only please, try again")
        
        print(f"\nExample format:\nSouth Africa,SKU44386,Air Max 90,2300,20)")                # Allow user to compare example with their data
        new_shoe = Shoe(new_country, new_code, new_product, new_cost, new_quantity)
        
        print(f"Your new shoe:\n{new_shoe}")
        happy = input("Would you like to add the new shoe to the shoe list? (y/n)").lower() # If happy, append to shoe_list and..
        if happy == 'y':                                                                    # ..write to file, elif try again, else main menu
            shoe_list.append(new_shoe)
            categories = f'Country,Code,Product,Cost,Quantity\n'            
            with open('inventory.txt', 'w') as i:
                i.write(categories)
                for shoe in shoe_list:
                    i.write(f'{shoe}\n')
            break
        
        elif happy == 'n':
            print("OK, reenter the data")
        else:
            break

    pass

def view_all():
    
    table = []
    for s in shoe_list:                         # Iterating through shoe_list, convert to string, then list of individual words
        table.append(str(s).split(","))         # Append to empty list  
    print(tabulate(table))                      # Use tabulate
    pass

def re_stock():

    index = min(range(len(shoe_list)), key=lambda i: shoe_list[i].quantity) # Iterate through shoelist.quantity, finding index of min value 
    print(f'\nThe shoe with the lowest quantity is:\n{shoe_list[index]}')     
    
    choice = input("Would you like to update the quantity? (y/n) ").lower()
    
    if choice == "y":
        while True:
            try:                                                            # Try/except for integers
                quant = int(input("What is the new quantity? "))
                shoe_list[index].quantity = quant                           # Replace element with that index with user input
                break
            except ValueError:
                print("Integers only please, try again")

        print(f"\nThe shoe has been updated:\n{shoe_list[index]}\n")

        categories = f'Country,Code,Product,Cost,Quantity\n'                
        with open('inventory.txt', 'w') as i:                               # Rewrite inventory.txt with new shoe details
            i.write(categories)
            for shoe in shoe_list:
                i.write(f'{shoe}\n')

    else:
        print(" \'y\' not entered, returned to main menu")

    pass

def search_shoe():

    shoe_code = str(input("Please enter the shoe code (format ABC12345): ").upper())
    
    for i in range(len(shoe_list)):                 # Iterate through the shoe_list[i].code to find a matching code, then print
        if shoe_code == str(shoe_list[i].code):
            print(shoe_list[i])
            break
        else:
            continue

    pass

def value_per_item():
    
    for i in range(len(shoe_list)):                                         # Iterate through each object, complete calc and display result
        value = int(shoe_list[i].cost)*int(shoe_list[i].quantity)
        print(f'''Shoe code:  {shoe_list[i].code} 
Value:      {value} dollarydoos
''')

    pass

def highest_qty():
    
    index = max(range(len(shoe_list)), key=lambda i: shoe_list[i].quantity)     # Find max quantity using above method and print
    print(f'\nThis shoe is now available for sale:\n{shoe_list[index]}')
    
    pass

#==========Main Menu=============

while True:
    read_shoes_data()
    menu = input('''
Main Menu:
cs - Add a new shoe to the file
va - View data for all shoes
rs - Restock a shoe
se - Search and display data for a shoe
vl - Display the value for all shoes
hi - View shoe with highest quantity
ex - Exit the program
    ''')

    if menu == 'cs':
        capture_shoes()
    elif menu == 'va':
        view_all()
    elif menu == 'rs':
        re_stock()
    elif menu == 'se':
        search_shoe()
    elif menu == 'vl':
        value_per_item()
    elif menu == 'hi':
        highest_qty()
    elif menu == 'ex':
        print("\nBye bye!\n")
        break
    else:
        print("Incorrect choice, try again!")