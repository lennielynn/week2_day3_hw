
# # use the dict below
# truck = {
#     'year': 2018,
#     'make': 'Chevrolet',
#     'model': 'Silverado'
# }

# print(truck['year'])

# people = {
#     'Max': 'blue',
#     'Lilly': 'brown',
#     'Barney': 'blue',
#     'Larney': 'brown',
#     'Ted': 'purple'
# }

# def e_color(name, c):
#     for name , c in people.items():
#         print(name, " has", c, " eyes") 
# e_color(people.items())



## Exercise #3 - Write a Function that asks someone's name and address, and then stores that into a dictionary, and continues to do so until they choose to 'quit'. Once they quit, the program should print all names and addresses. <br>
# <p>
# <b>Proper steps:</b><br>
# step 1: write a function that takes in information and stores it in a dictionary<br>
# step 2: define an empty dictionary to work with<br>
# step 3: create our loop, which asks the user for information until they quit<br>
# step 4: ask for the information, and store it into variables<br>
# step 5: check if the user types quit<br>
# step 5a: print out all information<br>
# step 5b: break out of the loop<br>
# step 6: if they didn't quit, add the information to the dictionary<br>
# step 7: invoke the function by calling it
# </p>


address_book = {}

def u_input():
    while True: 
       name = input("enter name here ")
       address = input("enter address here ")
       address_book [name] = address
       user_input =input("Quit or Continue? ")
       if user_input == "Continue": 
         continue
       elif user_input == "Quit":
         break
    
u_input()
print(address_book)