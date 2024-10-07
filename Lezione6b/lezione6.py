#marim arafa
#8-5-2024
"""9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() 
that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class.
Print the two attributes individually, and then call both methods.
"""
import random


class Restaurant:
    def __init__(self,
                 name :str,
                 cuisine :str,
                 number_served:int= 0) -> None:
        self.name = name 
        self.cuisine = cuisine
        self.number_served = number_served

    def describe_restaurant(self):
        return(f'name of the restauranrt :{self.name}, cuisine type :{self.cuisine}')
    def open_restaurant(self):
        return(f"The restaurant is open!! number of people served :{self.number_served}")
    def set_number_served(self,new_num_served):
        self.number_served = new_num_served
        return f'number to serve:{new_num_served}'
    def increment_number_served(self):
        while self.number_served:
            self.number_served += 1
            return f' number to serve :{self.number_served}'

        
        
restaurant1 :Restaurant = Restaurant(name="ndfsvk",cuisine="vmdcwdc",number_served= 0)
print(restaurant1.describe_restaurant())
print(restaurant1.open_restaurant(),"\n")
print(restaurant1.set_number_served(7))
print(restaurant1.increment_number_served())
print(restaurant1.increment_number_served())
print(restaurant1.increment_number_served())

"""9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.
"""
restaurant2 :Restaurant = Restaurant(name = "djvedv", cuisine="jnvkedv")
restaurant3:Restaurant = Restaurant(name="ixcjs", cuisine="scfwef")
print(restaurant2.describe_restaurant())
print(restaurant3.describe_restaurant(),"\n")

"""9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored
 in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a
personalized greeting to the user. Create several instances representing different users, and call both methods for each user.
"""
from user import User

user1 :User = User(first_name= "marco", last_name= "rossi",email="marcorossi32@gmail.com" ,password= 215435,num_phone= 467879700,login_attempts= 3)
user2 :User = User(first_name= "luca", last_name= "verdi",email="verdiluca@gmail.com" ,password= 4335578,num_phone= 466646460,login_attempts=3)
user3 :User = User(first_name= "alice", last_name= "gialli",email="malicegialli@gmail.com" ,password= 56765785,num_phone= 46787575450,login_attempts=3)
print(user1.describe_user(),"\n",user1.great_user())
print(user2.describe_user(),"\n",user2.great_user())
print(user3.describe_user(),"\n",user3.great_user())
print(user2.increment_login_attempts())
print(user2.increment_login_attempts())
print(user2.reset_login_attempts())



"""9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class.
 Print the number of customers the restaurant has served, and then change this value and print it again. Add a method called set_number_served() that lets you set the number of customers that
have been served. Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
 Call this method with any number you like that could represent how many customers were served in, say, a day of business. 
"""
#esercizio risolti dentro esercizio 9-1
"""9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method called increment_login_attempts() that increments the value of login_attempts 
by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. Print 
the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
"""
#esercizio risolto dentro esercizio 9-3

"""9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4.
 Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors.
 Create an instance of IceCreamStand, and call this method
"""
class IceCreamStand(Restaurant):
    def __init__(self,
                  name: str,
                    cuisine: str,
                      number_served: int = 0,
                    flavors:list[str] = []) -> None:
        super().__init__(name, cuisine, number_served)
        self.flavors = flavors

    def iceCream_falvors(self):
        print("\nIce cream flavors:")
        for flavor in self.flavors:
            print(f'   {flavor}')

ice_cream :IceCreamStand = IceCreamStand(name = "jcs", cuisine = "jfenfgel",flavors=["strawberry","lemon","chocolate"])
ice_cream.iceCream_falvors()

"""9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5. Add an attribute, privileges, 
that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges.
 Create an instance of Admin, and call your method.
"""
#esercizio risolto nel file admin_priv.py
"""9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. Move the show_privileges()
 method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.
"""
#esercizio risolto nel file admin_priv.py

"""9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides
the die has. Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""
class Die:
    def __init__(self,
                 sides: int = 6) -> None:
        self.sides = sides

    def roll_die(self):
        return(random.randint(1,self.sides))
    
    def roll_multiple_times(self,die , rolls: int) -> None:
        for _ in range(rolls):
            print(die.roll_die())
        print("\n")
    
print("Rolling a 6-sided die 10 times:")
die6 :Die = Die(sides=6)
die6.roll_multiple_times(die6,10)

print("Rolling a 10-sided die 10 times:")
die10 = Die(sides=10)
die10.roll_multiple_times(die10,10)

print("Rolling a 20-sided die 10 times:")
die20 = Die(sides=20)
die20.roll_multiple_times(die20,10)

        
"""9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 numbers or letters from the list and print a message saying that any ticket matching 
these 4 numbers or letters wins a prize."""
win_ticket_series = [3, 5, 7, 4, 56, "f", "j", 75, 35, 54, 12, 900, "I", "o", "M"]

winning_combination = random.sample(win_ticket_series, 4)

print(f"Winning combination: {winning_combination},\n")

"""9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers
until your ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket.
"""
my_ticket = random.sample(win_ticket_series, 4)

attempts = 0
while True:
    attempts += 1
    drawn_ticket = random.sample(win_ticket_series, 4)
    if set(drawn_ticket) == set(winning_combination):
        break

print(f"My ticket: {my_ticket}")
print(f"It took {attempts} loop to give me a winning ticket.")