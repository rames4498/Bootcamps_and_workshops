'''Using the same Dog class, instantiate three new dogs,
   each with a different age.
    Then write a function called, get_biggest_number(),
   that takes any number of ages (*args) and returns the oldest one.
  Then output the age of the oldest dog like so:

   The oldest dog is ?? years old.'''

class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

'''These attributes are passed to the __init__ method,
which gets called any time you create a new instance, attaching the name and age to the object.
You might be wondering why we didn’t have to pass in the self argument.'''

# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)
snupy  = Dog("sherlock",9)
# Access the instance attributes

def get_biggest_number(*args):
    return max(args)


print("The oldest dog is {} years old ".format(get_biggest_number(philo.age,mikey.age,snupy.age)))
    





