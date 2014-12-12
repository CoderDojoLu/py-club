#!/usr/bin/env python3
import sys
import platform

class Animal:
	def talk(self): print('I cannot talk')
	def walk(self): print('I can walk')
	def clothes(self):  print('I do not need clothes')

class Duck(Animal):
	##def __init__(self, color = 'white'):
	##	self._color = color
	##def __init__(self, **kwargs):
	##	self._color = kwargs.get('color', 'white')
	##	self._feet = kwargs.get('feet', 3)

	def __init__(self, **kwargs):
		self.variables = kwargs

	def quack(self):
	##	print ('Quaaaack!', self._color)
		print ('Quaaaack!')
		super().walk() # 
		print('Duck Walk')

	##def set_color(self, color):
	##	self._color = color
	##	self.variables['color'] = color

	##def get_color(self):
	##	return self._color
	##	return self.variables.get('color', None)

	def set_variable(self, k, v):
		self.variables[k] = v

	def get_variable(self, k):
		return self.variables.get(k,None)

class Dog(Animal):
	pass


def main():
     ##donald = Duck()
     ##donald = Duck(color = 'green', feet = 42)
     donald = Duck(feet = 2)
     donald.set_variable('color','orange')
     donald.quack()
     donald.walk()
     print(donald.get_variable('color'))
     donald.set_variable('color', 'blue')
     print(donald.get_variable('color'))

     donald.clothes()

     fido = Dog()
     fido.walk()
     
     frank =  Duck()
     frank.quack()
     frank.walk()
     print(sys.version)
     print(platform.python_version())

if __name__ == "__main__": main()