"""9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s 
methods to show that the import statement is working properly.
"""

from lezione6 import Restaurant

restaurant4 :Restaurant = Restaurant(name = "eger", cuisine="gerhgggggggg")

print(restaurant4.describe_restaurant())
print(restaurant4.open_restaurant(),"\n")
print(restaurant4.set_number_served(7))
print(restaurant4.increment_number_served())
print(restaurant4.increment_number_served())
print(restaurant4.increment_number_served())