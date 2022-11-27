<img src="https://i.imgur.com/4wgT88k.jpg">

# Classes in Python

## Learning Objectives

| Students Will Be Able To: |
|---|
| Describe the difference between classes and objects |
| Define a class in Python |
| Instantiate a class to create an object |
| Explain the special `__init__` method |
| Understand class vs. instance members |

## Roadmap

- Setup
- Review of OOP
- Writing a basic Python `class`
- Creating Objects by Instantiating a Class
- Overriding Methods
- Class vs. Instance Members
- Inheritance
- Essential Questions
- Practice Exercise
- Further Study

## Setup

Create a Python-based repl in [repl.it](https://repl.it).

## Review of OOP

Python is an **object-oriented programming (OOP) language**.

Object-oriented programming is characterized by programming with **objects** that represent the real-world objects of the application.

<details><summary>
❓What are classes used for in OOP?
</summary>
<p><strong>Classes are used to create objects.</strong></p>
</details>

A key principle of OOP we discussed during the JS Classes lesson was **encapsulation**...

<details><summary>
❓What's encapsulation?
</summary>
<p><strong>The bundling of related properties (attributes) and methods (behavior) together in an object.</strong></p>
</details>

Another key principle of OOP we discussed  was **inheritance**...

<details><summary>
❓What's inheritance?
</summary>
<p><strong>When a class subclasses/extends another class and thus inherits that parent/superclass's attributes & methods.</strong></p>
</details>

#### Objects in Python

As you've already heard, everything in Python is an object. What this means is that every variable or piece of data has properties and/or methods encapsulated within the object.

Python provides a `dir()` function that can be used to list an object's members (attributes and methods):

```python
# create a list
nums = [1, 2, 3]
# print the attributes & methods nums has
print( dir(nums) )
```

Some of the members like `append` & `pop` might look familiar.

The other methods that start and end with double-underscores, are called [_magic_ (or _dunder_) methods](https://rszalski.github.io/magicmethods/). They are internal methods most commonly used to _overload_ operators. If you would like to learn more about them, be sure to check out the link in the Further Study section.

We'll be using the `__init__` dunder method shortly. 

When we start working with Django, we'll be defining quite a few classes, so let's see how to we do it...

## Writing a basic Python `class`

Like many of you, I like dogs - let's define a `Dog` class to create doggies from:

```python
class Dog():
  def __init__(self, name, age = 0):
    self.name = name
    self.age = age

  def bark(self):
    print(f'{self.name} says woof!')
```

> The naming convention for Python classes is UpperCamelCasing.

Python automatically calls the `__init__` magic method when a new dog is created.

`__init__` is short for "initialize" because the method is used to initialize the properties of the new object.

**❓ What method in JS classes performs the same thing?**

The `age = 0` in `__init__`'s parameter list is called a _default parameter_ and will be assigned the the result of the expression to the right of the `=` if the function is called without an argument for that positional parameter.

The attributes for a dog instance are `name` and `age`.

`bark` is an _instance_ method in this Dog class.

**❓ What's an _instance_ method?**

### What's this `self` business?

In the JS lesson about `this`, it was mentioned that every OOP language must have the same or similar mechanism as `this` to be able to:

- Enable a method to access the other properties/methods in an object, and
- Enable a single-copy of a method in memory to serve any number of instances.

JavaScript, Java, C++, C#, and others call it `this`.

Ruby, Swift and others call it `self`.

However, in Python, only by convention is it called `self` because it's just a parameter name...

Take a look at the `__init__` and `bark` method definitions, notice how the first parameter is named `self`.  When we write code like `spot.bark()`, the object to the left of the dot is automatically assigned to the method's first parameter - which should be named `self`. This is how Python provides the "context" in both instance and class methods!

## Creating Objects by Instantiating a Class

By defining the `Dog` class, we now know the structure that each of the pooches will have!

Let's make a doggie:

```python
spot = Dog('Spot', 8)

print(spot) # -> similar to <__main__.Dog object at 0x7f27bad2c208>

# print the name and age attributes of the spot object
print(spot.name, spot.age) # -> Spot 8

# invoke the spot object's bark instance method
spot.bark() # -> Spot says woof!
```

Let's try out the default parameter for a new dog's `age`:

```python
dog = Dog('Lassie')

print(dog.name, dog.age) # -> Lassie 0
```

## Overriding Methods

As you saw above, when we used `print(spot)` to print the `spot` object, we got an unfriendly output.

We can change this behavior by _overriding_ the `__str__` method that the `print` function calls automatically to obtain the string to print out.

Let's modify the `Dog` class to override the `__str__` method:

```python
class Dog():
  def __init__(self, name, age = 0):
    self.name = name
    self.age = age

  def bark(self):
    print(f'{self.name} says woof!')
    
  def __str__(self):
    return f'Dog named {self.name} is {self.age} years old'
```

Let's try it out:

```python
spot = Dog('Spot', 8)

print(spot) # -> Dog named Spot is 8 years old
```


## Class vs. Instance Members

In Python, **instance** attributes & methods (members) are intended to be accessed/invoked by instances of the class, whereas, **class** members are intended to be accessible on the class only, not an instance.

Each object instance has its own copy of its attributes, e.g., `name`. However, all instances share class attributes.

To demonstrate class attributes, let's add a `nextId` class attribute to the `Dog` class that can be used to assign an `id` to each dog instance:

```python
class Dog():
  # class attribute
  next_id = 1

  # updated __init__
  def __init__(self, name, age = 0):
    self.name = name
    self.age = age
    self.id = Dog.next_id
    Dog.next_id += 1

  def bark(self):
    print(f'{self.name} says woof!')

  # updated __str__
  def __str__(self):
    return f'Dog ({self.id}) named {self.name} is {self.age} years old'
```

Note how the `Dog.next_id` class attribute is being accessed within the `__init__` method.

> Note: Technically, instances can also access class members via `self` due to the fact that if the instance does not have an accessed member, Python will check the class and provide the class version of the member if it exists.

Now let's make sure it worked :)

```python
spot = Dog('Spot', 8)
print(spot)
pup = Dog('Lassie')
print(pup)
```

Cool, now let's see how class methods are created by adding a `get_total_dogs` method.

Add this to the bottom of the `Dog` class:

```python
  def __str__(self):
    return f'Dog ({self.id}) named {self.name} is {self.age} years old'
  
  # new code below

  @classmethod
  def get_total_dogs(cls):
    # cls represents the Dog class
    return cls.next_id - 1
```

There's only two differences when defining a class method:

1. The `@classmethod` _decorator_
2. The naming convention of the first parameter is to use `cls` instead of `self`

> _Decorators_ in programming are used to implement _metaprogramming_ (when a program has knowledge or manipulates itself).  In Python, decorators are used to modify the behavior of a function or class. They are not very common, but there's a link in the Further Study section if you'd like to learn more about decorators in Python.

Let's test out the new class method:

```python
spot = Dog('Spot', 8)
pup = Dog('Lassie')

# class methods are called on the class, not an instance
print(Dog.get_total_dogs())  # -> 2
```


## Exercise - Banking System (1 hour)

### Part 1
Create a BankAccount class that meets the following criteria:

- Bank accounts should accept a type property - (like "savings" or "checking").
- Each account should keep track of its current balance which should start at 0.
- Each account should have access to a deposit and a withdraw methods.
- withdraw should return the new account balance after withdrawing
- Deposit should return the new account balance after depositing
- Once you've defined the class, create a checking account and a savings account. Withdraw money from the savings account and deposit that amount into the checking account.

### Part 2
- Prevent withdrawing money if the balance will go negative.


### Part 3
- Start each account with an additional overdraft_fees property that starts at 0. If a call to withdraw ends with the balance below zero then overdraft_fees should be incremented by 20. You should also prevent the user from going below a balance of -100, including the overdraft fees.

- Your program can be tested with these sample statements.

```python
checking = BankAccount('checking')
savings = BankAccount('savings')

print(savings.deposit(1000))

transfer = savings.withdraw(1200)
print(transfer)

print(checking.deposit(transfer))

print("checking.balance", checking.balance)
print("savings.balance", savings.balance)

print("checking.overdraft_fees", checking.overdraft_fees)
print("savings.overdraft_fees", savings.overdraft_fees)
```



## Inheritance

Maybe the following graphic will jog your memory in regards to what **inheritance** is:

<img src="https://i.imgur.com/MvXw4nD.gif">

Using inheritance, a **subclass** automatically inherits all of the attributes and methods of its **superclass**.

The **subclass** can then define additional attributes and/or methods to make a more _specialized_ class than the superclass.

For example, in the JS Classes lesson, we specialized the `Vehicle` class by _extending_ it to create a `Plane` subclass.

Let's see how inheritance is implemented in Python by creating a `ShowDog` class that specializes the `Dog` class:

```python
# Pass in superclass as argument
class ShowDog(Dog):
  # Add additional parameters AFTER those in the superclass
  def __init__(self, name, age = 0, total_earnings = 0):
    # Always call the superclass's __init__ first
    Dog.__init__(self, name, age)
    # Now add any new attributes
    self.total_earnings = total_earnings
  
  # Add additional methods
  def add_prize_money(self, amount):
    self.total_earnings += amount
```

> If not specified, the default superclass is Python's `object` class.

It's show time!

```python
winky = ShowDog('Winky', 3, 1000)
print(winky) # Yay, inherited the overriden __str__
winky.bark() # Yay, inherited the bark method
print(winky.total_earnings) # -> 1000
winky.add_prize_money(500) # New method that 'Dogs' don't have
print(winky.total_earnings) # -> 1500
```

Inheritance is critical to OOP languages. In fact, they even have their own **object hierarchies**.  Check this out:

<img src="https://i.imgur.com/GC3UE9l.jpg">

Frameworks like Django and Rails have elaborate object hierarchies of their own.  For example, when we move on to Django, we'll be defining Models by inheriting from a Django class like this:

```python
class Person(models.Model):
```

## Essential Questions

Take a couple of minutes to review these...

1. **What's the difference between a class and an object?**

2. **What Python keyword is used to define a class?**

3. **How do we create objects using a class?**

4. **True or False: Class attributes are shared by all instances of that class.**

5. **What OOP principle refers to subclasses specializing superclasses?**

## Practice Exercise

## Python Inheritance Lab - Banking System

### Part 1
- Create a base BankAccount class
1. Bank accounts keep track of their current balance
2. Bank accounts have a check_balance method that returns the current balance
3. Bank accounts have a deposit method that returns the balance of the account after adding to it
4. Bank accounts have a withdraw method that returns the amount of money that was successfully withdrawn.
5. Bank accounts return False if someone tries to deposit or withdraw a negative amount.
6. Bank accounts are created with a default interest rate of 2%
7. Bank accounts have a accumulate_interest method that sets the balance equal to the balance plus the balance times the interest rate
8. accumulate_interest returns the balance of the account after calculating the accumulated interest


### Part 2
- Create a ChildrensAccount class
1. Inherits from BankAccount
2. Children's bank accounts have an interest rate of Zero.
3. Every time accumulate_interest is executed on a Child's account the account always gets $10 added to the balance.

### Part 3
- Create an OverdraftAccount class
1. Inherits from BankAccount
2. An overdraft account penalizes customers for trying to draw too much money out of their account.
3. Overdraft accounts are created with an overdraft_penalty property that defaults to $40.
4. Customer's aren't allowed to withdraw more money than they have in their account. If a customer tries to withdraw more than they have then the withdraw method returns False and their balance is deducted only by the amount of the overdraft_penalty.
5. Overdraft accounts don't accumulate interest if their balance is below zero.

- Program can be tested against these sample statements.

```Python
# Sample Input
basic_account = BankAccount()
basic_account.deposit(600)
print(f"Basic account has ${basic_account.balance}")
basic_account.withdraw(17)
print(f"Basic account has ${basic_account.balance}")
basic_account.accumulate_interest()
print(f"Basic account has ${basic_account.balance}")
print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
print(f"Child's account has ${childs_account.balance}")
childs_account.withdraw(17)
print(f"Child's account has ${childs_account.balance}")
childs_account.accumulate_interest()
print(f"Child's account has ${childs_account.balance}")
print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print(f"Overdraft account has ${overdraft_account.balance}")
overdraft_account.withdraw(17)
print(f"Overdraft account has ${overdraft_account.balance}")
overdraft_account.accumulate_interest()
print(f"Overdraft account has ${overdraft_account.balance}")
```

## Further Study

[Classes Tutorial](https://docs.python.org/3.7/tutorial/classes.html)

[Python Inheritance](https://www.programiz.com/python-programming/inheritance)

Learn more about magic methods [here](https://rszalski.github.io/magicmethods/)

Learn more about Python's `self` [here](https://medium.com/quick-code/understanding-self-in-python-a3704319e5f0)

Learn more about metaprogramming [here](https://stackoverflow.com/questions/514644/what-exactly-is-metaprogramming)

[Decorators](https://www.programiz.com/python-programming/decorator) in Python