#!/usr/bin/env python3

class Duck:
	def quack(self):
		print ('Quaaaack!')

	def walk(self):
		print('Duck Walk')

	def bark(self):
		print('Cannot Woof')

	def fur(self):
		print('Nice feathers')


class Dog:
	def bark(self):
		print('Woof')

	def fur(self):
		print('Nice fur')
	def quack(self):
		print ('Cannot Quaaaack!')

	def walk(self):
		print('Dog Walk')

def main():
     donald = Duck()
     fido = Dog()

     inTheForest(donald)
     inThePond(fido)


     #for o in (donald, fido):
     #	o.quack()
     #	o.walk()
     #	o.bark()
     #	o.fur()

def inTheForest(dog):
	dog.bark()
	dog.fur()

def inThePond(duck):
	duck.quack()
	duck.walk()




if __name__ == "__main__": main()