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
		multiple=len(self.shape ) if len(self.shape) < max(self.shape) else max(self.shape)
		if self.operator == "sum":
			for i in c(self.items, self.n):
				if sum(i) == self.total:
					add=True
					for j in self.items:
						if i.count(j) > multiple: 
							add=False
							break
					if add: self.combs.append(i)
		elif self.operator == "product":
			for i in c(self.items, self.n):
				if math.prod(i) == self.total:
					add=True
					for j in self.items:
						if i.count(j) > multiple: 
							add=False
							break
					if add: self.combs.append(i)
					
	def getcombs(self):
		for i in self.combs:
			print(i)
	def getproperties(self):
		return f"shape:{self.shape}, total:{self.total}, size:{self.size}, operator:{self.operator}"
		
	def filter(self, item, repeat):
		item=int(item)
		newcombs=[]
		if repeat > 0:
			for i in self.combs:
				if i.count(item) >= repeat: newcombs.append(i)
		else:
			repeat= -repeat
			for i in self.combs:
				if not i.count(item) >= repeat: newcombs.append(i)
		self.combs=newcombs
	def remove_multiple(self):
		newcombs=[]
		multiple=len(self.shape ) if len(self.shape) < max(self.shape) else max(self.shape)
		for i in self.combs:
			add=True
			for j in self.items:
	 			if i.count(j) > multiple: 
	 				add=False
	 				break
			if add: newcombs.append(j)
		self.combs=newcombs.copy()
	
def create_region():
	shape = input("shape?")
	total = input("total?")
	newregion = puzzle_region(shape, total)
	newregion.setcombs()
	puzzle_array.append(newregion)
def filter(arraynr, item, repeat):
	puzzle_array[arraynr].filter(item, repeat)

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
