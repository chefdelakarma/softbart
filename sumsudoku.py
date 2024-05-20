#!/bin/env python3
from itertools import combinations_with_replacement as c
import math

puzzle_array = []

class puzzle_region:
	def __init__(self, shape, total, size=9, operator="sum"):
		self.size=int(size)
		self.total=int(total)
		self.operator=str(operator)
		if isinstance(shape, str):
			self.shape=[ int(i) for i in shape.split(',') ]
		elif isinstance(shape, list):
			self.shape=shape
		self.n=sum(self.shape)
		self.items=range(1,self.size+1)
		self.combs = []
	def setcombs(self):
		if self.operator == "sum":
			for i in c(self.items, self.n):
				if sum(i) == self.total:
					self.combs.append(i)
		if self.operator == "product":
			for i in c(self.items, self.n):
				if math.prod(i) == self.total:
					self.combs.append(i)
		self.remove_multiple()
	def getcombs(self):
		for i in self.combs:
			print(i)
	def getproperties(self):
		return f"shape:{self.shape}, total:{self.total}, size:{self.size}, operator:{self.operator}"
		
	def filterout(self, item, repeat):
		item=int(item)
		newcombs=[]
		for i in self.combs:
			if i.count(item) < repeat: newcombs.append(i)
		self.combs=newcombs
	def filterin(self, item, repeat):
		item=int(item)
		newcombs=[]
		for i in self.combs:
			if i.count(item) >= repeat: newcombs.append(i)
		self.combs=newcombs
	def remove_multiple(self):
		newcombs=[]
		multiple=len(self.shape ) if len(self.shape) < max(self.shape) else max(self.shape)
		for i in self.items:
	 		for j in self.combs:
	 			if j.count(i) <= multiple: newcombs.append(j)
		self.combs=newcombs
	
def create_region():
	shape = input("shape?")
	total = input("total?")
	newregion = puzzle_region(shape, total)
	newregion.setcombs()
	puzzle_array.append(newregion)
def filter(arraynr, income, number, repeattimes):
	if income:
		puzzle_array[arraynr].filterin(number, repeattimes)
	else:
		puzzle_array[arraynr].filterout(number, repeattimes)
def list(verbose=False):
	i_nr=0
	for i in puzzle_array:
		print(f"{i_nr}. {i.getproperties()}")
		if verbose: i.getcombs()
		i_nr=i_nr+1

	
while True:
	cmd=input("function arg?").split(' ',1)
	function=cmd[0]
	if function == 'exit':
		exit()
	if len(cmd) == 2:
		argument=str(cmd[1])
	else:
		argument=''
	command=f"{function}({argument})"
	exec(command)
