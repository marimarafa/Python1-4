#marim arafa
#18-04-2024
from audioop import reverse
"""
2-3. Personal Message: Use a variable to represent a person’s name, and print a message
to that person. Your message should be simple, such as, “Hello Eric, would you like to
learn some Python today?”
"""
#questa variabile contiene il nome 
name : str = ("Marim")
#questa variabile contiene il messaggio
message : str =(f'Hello {name},would you like to learn some python today? \n')
print(message)

"""
2-4. Name Cases: Use a variable to represent a person’s name, and then print
that person’s name in lowercase, uppercase, and title case.
"""
#questa variabile contiene il nome
nome : str =("Mario")
name_upper: str = nome.upper()
name_lower: str = nome.lower()
name_title : str= nome.title()
print(f'{name_lower}, {name_upper},{name_title}\n')

"""
2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output 
should look something like the following, including the quotation marks: Albert Einstein once said,“A person who never made 
a mistake never tried anything new.”
"""
name :str = ("Nelson Mandela")
quote :str = ("The greatest glory in living lies not in never falling, but in rising every time we fall.")
print(f'{name} once said : "{quote}"\n ')

"""
2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a
variable called famous_person. Then compose your message and represent it with a new variable
called message. Print your message.
"""
famous_person :str = ("Nelson Mandela")
message :str = ("The greatest glory in living lies not in never falling, but in rising every time we fall.")
print(f'{message}\n ')

"""
2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the
value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the 
filename without the file extension, like some file browsers do.
"""
file_name :str = ("python_notes.txt")
file_no_extension =file_name.removesuffix(".txt")
print(f'{file_no_extension}\n')

"""
3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name
by accessing each element in the list, one at a time
"""
list_names: list= ["Mario", "Luca", "Francesco", "Maria"]
for e in list_names:
    print({e})
print("\n")
"""
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name,
print a message to them. The text of each message should be the same, but each message should be personalized 
with the person’s name.
"""
#usare la ista dichiarata nell'esercizio 3-1
for e in list_names:
    print(f'Good morning {e}')
print("\n")

"""
3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a
list that stores several examples. Use your list to print a series of statements about these items, such as “I
 would like to own a Honda motorcycle.”
"""
lista :list =["ferrari", "mercedes","audi","range rover"]
for e in lista:
    if e == lista[0]:
        print(f'I would like to own a {e} car')
    elif e == lista[1]:
        print(f'My dad have a {e} car')
    elif e == lista[2]:
        print(f'I saw an {e} car yesterday')
    elif e == lista [3]:
        print(f'The new {e} car costs 300.000 $')
print("\n")

"""
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list
that includes at least three people you’d like to invite to dinner. Then use your list to print a message to
each person, inviting them to dinner.
"""
# usare la lista dichiarate nell'esercizio 3-1
place = "Le Bernardin"
time = "8:00 pm"
message = f'I would love for you to join me for dinner at {place} at {time} for great food and even better company! \n Inform me if you will be able to attend'
for e in list_names:
    print(f'Good evening {e}, {message}')
print("\n")
    
"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.
"""
# usare la lista dichiarate nell'esercizio 3-1
new_guest = "Paulo"
guest_cant_make_it = list_names.pop(3)
for e in list_names:
    print(f"Dear {e},Unfortunately, I've just been informed that {guest_cant_make_it} won't be able to join us to the dinner.")

list_names.append(new_guest)
message2 =f' Just a friendly reminder that our dinner at {place} is scheduled for tomorrow night at {time}.' 
'I am really looking forward to catching up and enjoying a wonderful meal together.'
for e in list_names:
    print(f'Good evening {e}, {message2} ')
print("\n")

"""
3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
"""
# usare la lista dichiarate nell'esercizio 3-1
for e in list_names:
    print(f"Dear{e},We have exciting news! We've just found a bigger dinner table, so we now have more space available.\n"
"This means we can invite a few more guests to join us for dinner. Looking forward to sharing a wonderful evening together with all of you!")
list_names.insert(0,"Claudia")
list_names.insert(3,"Pietro")
list_names.append("Lorenzo")
print(list_names)    
for e in list_names:
    print(f'Good evening {e}, {message2} ')
print("\n")

"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
"""
# usare la lista dichiarate nell'esercizio 3-1
print(f'I can invite only two people for dinner \n')
message3 ="I am sorry to inform you that we are unable to extend an invitation for dinner at this time.Please accept my sincere apologies for any inconvenience caused"
print(list_names)
while len(list_names) >2:
    remove_guest = list_names.pop()
    print(f'Dear{remove_guest}, {message3}')
print(list_names)
for e in list_names:
    print(f'Dear {e}, you are still invited for the dinner of tomorrow night')
del list_names[:]
print(list_names,"\n")

"""
3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed.
"""
places_to_visit = ["The Great Barrier Reef", " The Colosseum", "Machu Picchu", "The Grand Canyon", "The Great Wall of China"]
sorted(places_to_visit)
print(places_to_visit)
sorted(places_to_visit, reverse=True)
print(places_to_visit)
places_to_visit.reverse()
print(f'reversed the order: {places_to_visit}')
places_to_visit.reverse()
print(f'reversed the order again: {places_to_visit}')
places_to_visit.sort()
print(f'stored in alphabetical order: {places_to_visit}')
places_to_visit.sort(reverse=True)
print(f'stored in reverse-alphabetical order: {places_to_visit}\n')

"""
3-9. Dinner Guests: Working with one of the programs from Exercises 3, 
use len() to print a message indicating the number of people you’re inviting to dinner.
"""
# usare la lista dichiarate nell'esercizio 3-1
print(f'Number of people you’re inviting to dinner: {len(list_names)}\n')

"""
3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities,
languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced
in this chapter at least once.
"""
list_countries :list = ["Italy","Russia","Egypt","United States","Japan"]
print(list_countries)
print(len(list_countries))
print(max(list_countries))
print(min(list_countries))
print(sorted(list_countries))
list_countries.reverse()
print(list_countries)
print("\n")

"""
6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city
in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
"""
d_information : dict= {"first_name":"Marim", "last_name" : "Arafa","age" :19,"city" :"Rome"}
for keys in d_information:
    print(keys," : ",d_information[keys])
print("\n")
"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary.
Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number.
For even more fun, poll a few friends and get some actual data for your program.
"""
d_fav_num : dict= {"Luca":4, "Mathew" : 28,"Giovanni" :356,"Carlo" :34,"Giuseppe":987}
for keys in d_fav_num:
    print(f'{keys} favourite number is :{d_fav_num[keys]}\n')

"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the
word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each 
word-meaning pair in your output
"""
glossary :dict = { "RANGE": "Generates a sequence of numbers.","SORTED": "Returns a sorted list from the elements of any iterable."
    ,"LOOP": "Repeats code without duplication.", "PRINT": "Displays information on the screen.","INPUT": "Accepts user input."}
for word in glossary:
    meaning = glossary[word]
    print(f'{word} : \n {meaning}')
print("\n")

"""
6-7. People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three 
dictionaries in a list called people.Loop through your list of people.As you loop through the list,print everything you know about each person.
"""
# usare il dizionario dichiarato nell'esercizio 6-1
d_information2 : dict= {"first_name":"Sofia", "last_name" : "Rossi","age" :22,"city" :"Milan"}
d_information3 : dict= {"first_name":"Marco", "last_name" : "Bianchi","age" :45,"city" :"New York"}
list_people :list = [d_information,d_information2,d_information3]
for persona in list_people:
    print(f'First name : {persona["first_name"]}')
    print(f'Last name : {persona["last_name"]}')
    print(f'Age : {persona["age"]}')
    print(f'City : {persona["city"]}\n')
    
"""
6-8. Pets: Make several dictionaries,where each dictionary represents a different pet.In each dictionary, include the kind of animal and the 
owner’s name.Store these dictionaries in a list called pets.Next,loop through your list and as you do,print everything you know about each pet. 
"""
pet1 :dict = {"kind_of_animal":"cat","owners_name" :"Sara"}
pet2 :dict = {"kind_of_animal": "dog", "owners_name": "Alice"}
pet3 :dict = {"kind_of_animal": "parrot", "owners_name": "Charlie"}
pet4 :dict = {"kind_of_animal": "rabbit", "owners_name": "David"}
pet5 :dict = {"kind_of_animal": "hamster", "owners_name": "Emma"}
list_pets =[pet1,pet2,pet3,pet4,pet5]
for pet in list_pets:
    print(f'Kind  : {pet["kind_of_animal"]}')
    print(f'Owner : {pet["owners_name"]}\n')

"""
6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three
favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. 
Loop through the dictionary, and print each person’s name and their favorite places.
"""   
favourite_places :dict = {"Bob" :["Tokyo", "New York"], "Sofia" :["Rome","Paris","London"], "Claudia":["Milan"]}
for person, places in favourite_places.items():
    print(f"{person}'s favorite places are: ")
    for place in places:
        print(f'{place}')
    print("\n")
"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers
"""
# usare il dizionario dichiarato nell'esercizio 6-2
d_fav_num : dict= {"Luca":[4,3,534,6], "Mathew" : [28,34,7,8,9],"Giovanni" :[356,0,34,23],"Carlo" :[34,98],"Giuseppe":[987,9,1]}
for person, numbers in d_fav_num.items():
    print(f"{person}'s favorite numbers are: ")
    for num in numbers:
        print(f'{num}')
print("\n")

"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and
 include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information you have stored about it.
"""
cities : dict ={"Rome": {"country" : "Italy","population": "2,873 million", "fact" : "Modern Rome has 280 fountains and more than 900 churches"},
                 "London" : {"country" : "England","population": "8,982 million","fact" : "Over 300 languages are spoken in London. "}
                 ,"Paris":{"country" : "France","population": "67,97 million", "fact" : "France is known as L'Hexagone ⬡"}}
for city,info in cities.items():
    print(f'About {city}:')
    for information in info:
        print(f'{information} :{info[information]}')
    print("\n")

"""
6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs 
from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.
"""
# usare il dizionario dichiarato nell'esercizio 6-9
favourite_places["Paolo"] = ["Casablanca", "Rome","Napoli"]
for person, places in favourite_places.items():
    print(f"{person}'s favorite places are: ")
    for place in places:
        print(f'\t {place}')
    print("\n")

