# defining a function
def greet_user():
    # display simple greeting
    print("Hello!")
greet_user()

# passing information to a function/

def greet_user(username):
    print(f"Hello, {username.title()}")
greet_user('rachel')

# the variable username in the definition of greet_user() is an example of a parameter a piece of information the function needs to do its job.The value 'jesse' in greet_user('jessse') is an example of an argument

def describe_pet(animal_type,pet_name):
    print(f"\nI have a {animal_type}")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}")
describe_pet('hamster','harry')

# positional argument 
# multiple functions call.you can call a function as many times as you needed

describe_pet('hamster','harry')
describe_pet('dog','willie')

# calling function multiple times is a very efficient way to work.
# Order is matters in posional arguments/

describe_pet('harry','hamster')

# keyword argument directly associate the name and the value with argument

describe_pet(animal_type = 'hamster', pet_name = 'harry')

# Default values. For example if you notice that the most of the calls to decsribe_pet() are being used to describe dogs you can set the default value of animal 'dog'

def describe_pet(pet_name,animal_type = 'dog'):
    """Display information about a pet """
    print(f"\nI have a {animal_type}")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}")
describe_pet(pet_name = 'willie')

# we could provide just dog's name

describe_pet('willie')

# equivalent function calls
# A dog named Willie

describe_pet('willie')
describe_pet(pet_name = 'willie')

# A hamster named Harry

describe_pet('harry','hamster')
describe_pet(pet_name = 'harry',animal_type = 'hamster')
describe_pet(animal_type = 'hamster',pet_name = 'harry')

# all following calls would work
# return values
# returning simple value
# example a function tekes first and last name and returns a nearly formatted full name

def get_formatted_name(first_name,last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician  = get_formatted_name('jimi','hendrix')
print(f"\n{musician}")

# making an argument optional
# get_formatted_name(first_name,middle_name,last_name)
# we could add middle name in example shown before but middle name aren't always needed and this function as writtten would not work. To meke get_formatted_name() work without middle_name provided we need to set default value to middle_name

def get_formatted_name(first_name,last_name,middle_name = ''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)
musician = get_formatted_name('john','hooker','lee')
print(musician)

# returning a dictionary

def build_person(first_name,last_name):
    """Return a dictionary of information abour a person"""
    person = {'first': first_name,'last': last_name}
    return person
musician = build_person('jimi','hendrix')
print(musician)

# we extend this function adding age
def build_person(first_name,last_name,age=None):
    person = {'first': first_name,'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi','hendrix',age=27)
print(musician)

# using a function with a while loop//
def get_formatted_name(first_name,last_name):
    """Return a full name,neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
# this is infinite loop//
    
while True:
    print("\nPlease tell your name: ")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
formatted_name = get_formatted_name(f_name,l_name)
if 'q' not in f_name and l_name:
    print(f"\nHello, {formatted_name}")
    
# Passing a List//
# it's useful to pass a list to a function whether it is a list of names,numbers or more complex objects,such as dictionaries
    
def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)
usernames = ['hannah','ty','rachel']
greet_users(usernames)

# Modifying a list in a function//
# when you pass a list to a function, the function can modify the list.Any changes made to the list inside the function's body are permanent
# Start with some designs that need to be printed

unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

# Simulate printing each designs, until none are left
# Move each design to completed_models after printing

while unprinted_designs:
    current_designs = unprinted_designs.pop()
    print(f"Printing model: {current_designs}")
    completed_models.append(current_designs)
    
# Display all completed models
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)
    
# we can reorganize this code by wrinting two functions//
def print_models(unprinted_designs,completed_models):
    """Simulate printing each designs, until none are left.Move each design to completed_models after printing"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """Show all models  that were printed"""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

# Preventing a function from modifying a list//
# sometimes you need keep a list form modifying.You can make a copy of a list, any changes will affect only a copy
# function_name(list_name[:]) example
# print_models(unprinted_designs[:],completed_models)
# Passing an arbitrary number of argument
# sometimes you won't know how many arguments a function need to accept. Python allows a function to collect an arbitrary number of arguments from calling statement
# Example function builds a pizza topppings
def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','mozarella')

# *toppings tells Python to make an empty tuple called toppings
def make_pizza(*toppings):
    """Print all requested topppings"""
    print("Making pizza with following topppings: ")
    for topping in toppings:
        print(f"-{topping}")
make_pizza("pineapple")
make_pizza('salami','pepperoni','mozarella')

# Mixing Positional and Arbitrary Arguments
# the argument that accepts an arbitrary argument must placed last in the function definition
def make_pizza(size,*toppings):
    """Summarize the pizza we about to make"""
    print(f"\nMaking a {size} inch pizza with the following topppings:")
    for topping in toppings:
        print(f"{topping}")
make_pizza(6,'pepperoni')
make_pizza(12,'salami','mozarella')

# Using arbitrary keyword arguments
# sometimes want to accept arbitrary number of arguments, but you won't know ahead what kind of information will be given to the function.Good example building user profile: you know you will get information about user but you don't know what kind of information
def build_profile(first,last,**user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['fisrt_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert','einstein',location = 'princeton',field = 'physics')
print(user_profile)

# **user_info allows Python to create an empty dictionary called user_info and pack whatever name-value pairs it receives.
# You'll often see the parameter name **kwargs used to collect non-specific keyword arguments

# storing your functions in print_models
# you can store functions in modules and than importing that module,storing functions in a seperate file allows you to hide the details of your code
# Importing an Entire Module//
# Importing specific functions
# General syntax for this approach
# from module _name import function_name
# you can import as many functions from module as you want seperate functions name by comma: from module_name import functions_0,function_1,function_2
# Using as to give a functions an alias
# if the name of a funcion you are importing might have coflict with existing name or if function name is long you can use short unique alias - alternate name similar to a nickname. from pizza import make_pizza as mp. To import all functions in a Module by using asteriks (*) operator