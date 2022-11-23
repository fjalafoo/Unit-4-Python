# print("Hello World!!!")
"""
I can write a 
Multi line comment
"""

# my_number = 10

# print(type(str(my_number)))



# state = "Hawaii"

# year = 1959

# message = f"{state} was the last state to join the U.S. in {year}"

# print(message)



# split_string = "ace of spades".split("a")

# print(split_string)

# alphabet = "abcde"

# print(list(alphabet))



# index_of_x = "abcdqqxzzz".replace("z", "a")

# print(index_of_x)




# print(len("green eggs and ham"))






# string = "abcdefg"

# print(string[-2])


# num = 25

# # msg = "There are " + str(num) + " tacos"
# msg = "There are {}, {} tacos".format(num, "30")

# # new_msg = f"There are {num} tacos"
# print(msg)


# hex = a5

# print(int("a5", 16))

# if 1 == "1" #IN PYTHON, FALSE

# if num > 5 && num < 10 # IN JS

# if num > 5 and num <10 # PYTHON




# floor = "clean"
# walls = "sticky"

# if floor == "sticky": #:::::::::::
#     print("Clean the floor! It is sticky!")
# elif walls == "sticky":
#     print("Clean your walls!")
# else: #Optional
#     print("Your floor and walls are clean!")



# if walls:

#     print("Clean the walls! They're sticky!")
# color = ""
# while color != 'quit':
#     color = input('Enter "green", "yellow", "red": ').lower()
#     print(f'The user entered {color}')
#     if color == 'green':
#         print('Go')
#     elif color == 'yellow':
#         print('Slow Down')
#     elif color == 'red':
#         print('Stop!')
#     else:
#         print('Bogus!!!')

# names = ['Alex', 'Kareem', 'Nahid', 'Ahlam']

# for el in names:
#     print(el)




# print(type(range(5)))
# for num in range(2,11,4):
#     print(num)


# nums = tuple(range(5, 0, -1))
# print(nums)

# if 25 and 0:
#     print('True!')




# function fahrToKelvin(temp) {
# return ((temp -32 ... .. .))}
    

# def fahr_to_kelvin(temp):

#     #.. extra logic
#     #.. if statements
#     #.. for loops
#     #.. define variables

#     return ((temp - 32) * (5/9) + 273)


#Only one way to define a function
# def first_function():
#     return "My Python Function!"

# print(first_function())

# print(result)

# DECALRATIONS function sum() 
# ARROW const sum = () => {}
# EXPRESSIONS const sum = function() {} 


# Pythons Lambda function (equivalent of arrow functions)


# const numbers = [1,2,3,4,5]
# numbers = [1,2,3,4,5,6] #list

# let odds = numbers.filter(eachNum => eachNum % 2)
# def 
# odds = list(filter(lambda eachNum: eachNum % 2, numbers))

# print(odds)


# Hoisting???

# const mySum = findSum(3,5)

# function findSum(a,b){
#     return a + b
# }

#args -------> arguments
#kwargs -------> keyword arguments
# def add(**kwargs):
#     # Object.values(), Object.keys(), Object.entries()
#     for key,value in kwargs.items():
#         print(f'key: {key} and value: {value}')

# print(add(name='Alex', topic='Python', fun='coding'))

# def add(a,b, *args):
#     return a + b

# print(add(5, 10, 100))



# player = {
#   'name': 'Lionel Messi',
#   'team': 'Argentina',
#   'current_score': 1
# } 

# print(player.items())

# for key, value in student.items():
#     print(value)






# players = ['Messi', 'Maradona', 'Neymar', 'Salman', 'Ronaldo']

# for idx, p in enumerate(players):
#     print(idx, p)




# nums = [1,2,3,4,5,6,7,8,9,10]
# I want 'n * n' for each 'n' in nums 

# squares = []
# for n in nums:
#     squares.append(n*n)

# squares = [n*n for n in nums if (n*n) % 2 == 0]

# print(squares)

# one, two, three = 'abc'

# print(two)






# Lab 1
# movies = [
#     {
#         'title': 'Fast and Furious 7',
#         'duration': 'Almost 1 our 14 minutes',
#         'stars': ['Paul Walker', 'Vin Diesel', 'Dwayne The Rock Johnson']
#     },
#     {
#         'title': 'Jumanji',
#         'duration': '2 hours 10 minutes',
#         'stars': ['Kevin Hart', 'Dwayne The Rock Johnson', 'Robin Williams']
#     },
# ]


# for m in movies:
#     stars = ','.join(m['stars'])
#     print(f"{m['title']} lasts for {m['duration']}. Stars: {stars}")





# books = [
#     {
#         'title': 'Django Unchained',
#         'author': 'Quentin Tarantino',
#         'alreadyRead': True
#     },
#     {
#         'title': 'Rich Dad, Poor Dad',
#         'author': 'Robert Kiyosaki',
#         'alreadyRead': False
#     },
# ]


# for b in books:
#     if b['alreadyRead']:
#         print(f"You already read {b['title']} by {b['author']}")
#     else:
#         print(f"You still need to read {b['title']} by {b['author']}")



# Lab 2


students = ['mariam', 'john', 'sumaya', 'peter', 'carlos', 'annie', 'ali', 'adam', 'ramesh', 'lee']

# print(students[1])
# print(students[-1])

foods = ('pizza', 'icecream', 'malghoom', 'pasta', 'machboos', 'steak', 'mansaf', 'koshary', 'molakhiya')

# for f in foods:
#     print(f"{f} is good")

# (one, two, *favs) = foods
# for fav in favs:
#     print(f"{fav}")

# for f in foods[-2:]:
#     print(f"{f} is a good food")

# home_town = {
#     'city': 'Doha',
#     'state': 'I dont know',
#     'population': '3000000000',
# }
# print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']} ")

# for key, val, in home_town.items():
#     print(f"{key} = {val}")




cohort = []

students = [
    {
        'student': 'mariam',
        'fav_food': 'pizza',
    },
    {
        'student': 'carlos',
        'fav_food': 'steak',
    },
    {
        'student': 'ramesh',
        'fav_food': 'mansaf',
    },
]

# for s in students:
#     cohort.append(s)
# print(cohort)

awesome_students = [f"{s['student']} is awesome" for s in students]
#Return f"{s'student'} is awesome", for every s in student
# for a in awesome_students:
#     print(a)

foods = ('pizza', 'icecream', 'malghoom', 'pasta', 'machboos', 'steak', 'mansaf', 'koshary', 'molakhiya')


foods_with_a = [f for f in foods if 'z' in f]
# Return f, for f in foods, if 'z' is in f
# [<expression> for <item> in <list>]
# This reads as: I want <expression> for each <item> in <list>
# for f in foods_with_a:
#     print(f)




# nums = [1,2,3]

# print (dir(nums))




class Dog():
    next_id = 1
    #init is the equivalent of the constructor fn in JS
    #self is the equivalent of 'this' in JS obj/classes
    def __init__(self, name, age = 0):
        # this.name = name
        self.name = name
        self.age = age
        self.id = Dog.next_id
        Dog.next_id += 1

    def bark(self):
        print(f"{self.name} says woof!")

    def __str__(self):
        return f"Dog name {self.name} is {self.age} years old"

    @classmethod
    def get_total_dogs(cls):
        return cls.next_id - 1
# Dog.get_total_dogs() 
# XXXXX spot.get_total_dogs() XXXXX

spot = Dog('spot', 8)

fluffy = Dog('fluffy', 4)
fluffy2 = Dog('fluffy2', 4)
fluffy3 = Dog('fluffy3', 4)
# print(Dog.get_total_dogs())
# spot.bark()
print(spot)



