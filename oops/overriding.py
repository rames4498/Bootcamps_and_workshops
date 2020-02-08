class Dog:
    species = 'mammal'
class SomeBreed(Dog):
    pass

class SomeOtherBreed(Dog):
    species = 'reptile'
frank = SomeBreed()
frank.species
'mammal'
beans = SomeOtherBreed()
beans.species
'reptile'
