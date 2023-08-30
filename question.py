#  Build a Shopping Cart 
# You can use either lists or dictionaries. The program should have the following capabilities:
# 1) Takes in input 
# 2) Stores user input into a dictionary or list 
# 3) The User can add or delete items 
# 4) The User can see current shopping list 
# 5) The program Loops until user 'quits' 
# 6) Upon quiting the program, print out all items in the user's list 

shopping_list = {}

def u_input():
    while True: 
       user_input = input("edit or view shopping list? ")
       if user_input == "view":
           print(shopping_list)
       elif user_input == "edit":
           user_input = input("add item or remove item ")
           if user_input == "add":
                item = input("enter Item here ")
                price = input("enter Price here ")
                shopping_list [item] = price
           if user_input == "remove":
                print(shopping_list)
                r_item = input("enter item you'd like removed ")
                del shopping_list[r_item]
       user_input = input("Quit or Continue? ")
       if user_input == "continue": 
         continue
       elif user_input == "quit":
         break   
u_input()
print(shopping_list)


# address_book = {}

# def u_input():
#     while True: 
#        name = input("enter name here ")
#        address = input("enter address here ")
#        address_book [name] = address
#        user_input = input("Quit or Continue? ")
#        if user_input == "Continue": 
#          continue
#        elif user_input == "Quit":
#          break   
# u_input()
# print(address_book)