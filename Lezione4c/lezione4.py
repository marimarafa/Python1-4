#marim arafa
#23-4-2024

"""
8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in 
this chapter. Call the function, and make sure the message displays correctly.
"""
#funzione dichiarata nel file message.py
import message
message.display_message("What are you learning about in this lesson? \n")

"""
8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message,
such as "One of my favorite books is Alice in Wonderland". Call the function, making sure to include a book title as an argument
in the function call.
"""
def favorite_book(title :str)-> str:
    print(f'One of my favorite book is {title}')
favorite_book("Dream of the Red Chamber (紅樓夢)")

"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the 
shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function
once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
"""
def make_shirt(size:int ,message :str) -> str:
    print(f'Size shirt: {size} , Message: {message}')
size = "Small"
message = "Have a good day"    
make_shirt(size,message)
print("\n")

"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
"""
make_shirt("Large","I love python")
make_shirt("Medium","I love python")
make_shirt("Xsmall","..,..")
print("\n")

"""
8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a 
simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three
different cities, at least one of which is not in the default country
"""
def describe_city(city:str , country:str) -> str:
    print(f'{city} is in {country}')
describe_city("Rome","Italy")
describe_city("London","England")
describe_city("Cairo","Egypt")
print("\n")

"""
8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should
return a string formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, 
and print the values that are returned.
"""
def city_country(city :str,country :str) -> str:
    return (f'"{city}, {country}"')
city_and_country1 = city_country("Santiago","Chile")
city_and_country2 = city_country("Rome","Italy")
city_and_country3 = city_country("Tokyo","Japan")
print(city_and_country1)
print(city_and_country2)
print(city_and_country3,"\n")

"""
8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name
and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries
representing different albums. Print each return value to show that the  dictionaries are storing the album information correctly.Use None to 
add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value 
for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs
on an album.
"""
def make_album(artist_name, album_title, number_songs=None):
    music_album = {'artist': artist_name,'album title': album_title}
    if number_songs:
        music_album['number_of_songs'] = number_songs
    return music_album
print(make_album("John","One day"))
print(make_album("Grita","Love",4))
print(make_album("Alice","Cold weather",9),"\n")

"""
8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title.
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit
value in the while loop.
"""
#utilizzare la funzione dichiarata nell'esercizio 8-7
while True:
    albums_artist = input("Enter the album's artist: ")
    if albums_artist.lower() == "quit":
        break
    album_title = input("Enter the album's title: ")
    if album_title.lower() == "quit":
        break
    print(make_album(albums_artist, album_title))
    break
print("\n")

"""
8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(),
which prints each text message.
"""
def show_messages(lista :list) -> str:
    for text in lista:
        print(text)
short_texts = ["hello","good morning","have a good day","I love python"]
show_messages(short_texts)
print("\n")

"""
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text 
message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to 
make sure the messages were moved correctly.
"""
def send_messages(lista :list) -> str:
    texts = []
    for text in lista:
        texts.append(text)
    return texts
print("\nOriginal messages:")
show_messages(short_texts)
print("\nSent messages:")
show_messages(send_messages(short_texts))
print("\n")

"""
8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the original list has retained its messages.
"""
short_texts2 = short_texts.copy()
send_messages(short_texts2)
print(short_texts)
print(short_texts2)

"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that 
collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function
three times, using a different number of arguments each time.
"""
def sandwich_item(items:list) -> str :
    print("\nThe items in this sandwich are:")
    for item in items:
        print(item)
        
sandwich_item(["cheese","bacon","eggs","olives"])
sandwich_item(["meat","cheese","pickle","tomatoes","lettuce"])
sandwich_item(["peanut butter","jelly"])

"""
8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs
that describe you. All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow,
age 45, hair brown, weight 67"
"""
def build_profile(name:str,age:int,hair:str,weight:int,tall:int) -> str :
    return str(f'\nname :{name} , age :{age} , hair :{hair}, weight :{weight}, tall :{tall}')
print(build_profile("Mario Rossi",30, "brown" , 70, 170))
print("\n")

"""
8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model
name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value 
pairs, such as a color or an optional feature. Your function should work for a call like this one: car = make_car('subaru', 'outback', 
color='blue', tow_package=True) Print the dictionary that’s returned to make sure all the information was stored correctly.
"""
#chiamare la funzione dal file car.py
def make_car(manufacturer:str,model:str,color = None,tow_package=True or False) -> dict :
    car = {}
    car["manufacturer"] = manufacturer
    car["model"] = model
    if color is not None:
        car['color'] = color
    car['tow_package'] = tow_package
    return car
print(make_car('subaru','outback',color='blue',tow_package=False))

"""
8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py.
Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
"""
from printing_functions import printing_text
printing_text("\nHello everyone, have a nice day!")
print("\n")

"""
8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main
program file, and call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
"""
#usare la funzione dell'esercizio 8-1 nel file message.py
from message import display_message
display_message("Good morning")
from message import display_message as dm
dm("Have a good day")
import message as ms
ms.display_message("Studying pyhton")
from message import *
display_message("byeeeee")