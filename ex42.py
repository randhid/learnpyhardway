## Animal is-a object (yes, sort of confusing) look at xtra credit
class Animal(object):
	pass

## Dog is-a animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name of some sort
		self.name = name

## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a nam of some sort
		self.name = name
## ?
class Person(object):

	def __init__(self, name):
		# Person has-a name of some kind
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employe is-a person
class Employee(Person):

	def __init__(self, name, salary):
		## calls Employee class, has-a self(object)
		super(Employee, self).__init__(name)
		## Employee has-a salary of some sort
		self.salary = salary

## Fish is-a object 
class Fish(object):
	pass

## Salmon is-a fish
class Salmon(Fish):
	pass

## Halibut is-a fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a cat pet satan
mary.pet = satan

## Frank is-a employee has-a salary of 120000
frank = Employee("Frank", 120000)

## frank has-a pet rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()



