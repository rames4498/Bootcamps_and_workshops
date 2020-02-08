'''Using the same file, add an instance attribute of is_hungry = True to the Dog class.
Then add a method called eat() which changes the value of is_hungry to False when called.
Figure out the best way to feed each dog and then output “My dogs are hungry.”
if all are hungry or “My dogs are not hungry.” if all are not hungry.
The final output should look like this:

I have 3 dogs. 
Tom is 6. 
Fletcher is 7. 
Larry is 9. 
And they're all mammals, of course. 
My dogs are not hungry.'''
#Parent class
class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs


# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    # Instance method
    def description(self):
        return self.name, self.age

    # Instance method
    def speak(self, sound):
        return "%s says %s" % (self.name, sound)

    # Instance method
    def eat(self):
        self.is_hungry = False


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)

# Create instances of dogs
my_dogs = [
    Bulldog("Tom", 6), 
    RussellTerrier("Fletcher", 7), 
    Dog("Larry", 9)
]

# Instantiate the Pets class
my_pets = Pets(my_dogs)

# Output
print("I have {} dogs.".format(len(my_pets.dogs)))
for dog in my_pets.dogs:
    dog.eat()
    print("{} is {}.".format(dog.name, dog.age))

print("And they're all {}s, of course.".format(dog.species))

are_my_dogs_hungry = False
for dog in my_pets.dogs:
    if dog.is_hungry:
        are_my_dogs_hungry = True

if are_my_dogs_hungry:
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry.")




