'''Next, add a walk() method to both the Pets and Dog classes so that when you call the method on the Pets class, each dog instance assigned to the Pets class will walk(). Save this as dog_walking.py. This is slightly more difficult.

Start by implementing the method in the same manner as the speak() method. As for the method in the Pets class, you will need to iterate through the list of dogs, then call the method itself.

The output should look like this:

Tom is walking!
Fletcher is walking!
Larry is walking! '''

#Parent class
class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())


# Parent class
class Dog:

    # Class attribute
    species = 'mammal'
    is_hungry = True

    # Initializer / instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return self.name, self.age

    # Instance method
    def speak(self, sound):
        return "%s says %s" % (self.name, sound)

    # Instance method
    def eat(self):
        self.is_hungry = False

    def walk(self):
        return "%s is walking!" % (self.name)


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

# Instantiate the Pet class
my_pets = Pets(my_dogs)

# Output
my_pets.walk()


