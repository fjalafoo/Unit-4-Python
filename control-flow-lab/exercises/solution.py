# exercise 1
print("exercise 1:")
vowels = ('a','e','i','o','u')

letter = input("Please enter a letter from the alphabet (a-z or A-Z): ")


if letter in vowels:
    print("%s is vowel." % letter)
else:
     print("%s is not a vowel." % letter)



# exercise 2
print("exercise 2:")
count = 0

phrase = input("Please enter a word or phrase: ")

for x in phrase:
  count=count+1
  
print("What you entered is %s characters long" %count)

# exercise 3
print("exercise 3:")

age = int(input("Input a dog's age in dog years: "))
if age <= 2:
    age = age*10
    print(f"The dog's age in human years is {age}")
else:
    age = 20 + (age-2)*7
    print(f"The dog's age in human years is {age}")

# exercise 4
print("exercise 4:")
side_1 = int(input('Enter the lengths of three side of a triangle: \n a:' ))
side_2 = int(input('b:' ))
side_3 = int(input('c:' ))

if side_1 == side_2 == side_3:
    print('equalateral')
elif side_1 == side_2 | side_1 == side_3 | side_2 == side_3:
    print('isosceles')
else:
    print('scalene')

# exercise 5
print("exercise 5:")
a,b,i = 0,1,0
while(i<51):
    print(f'term: {i} / number: {a}')
    a = b - a
    b = a + b
    i += 1

# exercise 6
print("exercise 6:")