print("Hello world!!!")


# This is a comment! Python will ignore it. 
"""
This is a
multiline comment
"""

# This is a
# multiline comment

my_number = 15

print(my_number)

#variable naming in python are case sensitive


#functions lab
def to_sum(n):
    sum = 0
    for num in range(1,n+1):
        sum+=num
    return sum
        
def largest(list):
    print(max(list))



def occurances(word, seekedItem):
    return word.find(seekedItem)


print(occurances('fleep floop', 'e'))


def product(*args):
    result =1
    for n in args:
        result*=n
    return result