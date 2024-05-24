#!/bin/env python3
from itertools import combinations_with_replacement
import math

puzzle_array = []

class puzzle_region:
	def __init__(self, shape, total, size=9, operator="sum"):
		self.size=int(size)
		self.total=int(total)
		self.operator=str(operator)
		if isinstance(shape, str):
			self.shape=[ int(i) for i in shape.split('-') ]
		elif isinstance(shape, list):
			self.shape=shape
		self.n=sum(self.shape)
		self.items=range(1,self.size+1)
		self.combs = []
		self.multiple=len(self.shape ) if len(self.shape) < max(self.shape) else max(self.shape)
	def check_multiple(self, comb):
		for j in self.items:
			if comb.count(j) > self.multiple: return False
		return True
	def setcombs(self):
		if self.operator == "sum":
			for i in combinations_with_replacement(self.items, self.n):
				if sum(i) == self.total and self.check_multiple(i): self.combs.append(i)
		elif self.operator == "product":
			for i in combinations_with_replacement(self.items, self.n):
				if math.prod(i) == self.total and self.check_multiple(i): self.combs.append(i)
	def getcombs(self):
		for i in self.combs:
			print(i)
	def getproperties(self):
		properties=f"shape:{self.shape}, total:{self.total}, size:{self.size}, operator:{self.operator}"
		print(properties)		
	def filter(self, item, repeat):
		item=int(item)
		newcombs=[]
		if repeat > 0:
			for i in self.combs:
				if i.count(item) >= repeat: newcombs.append(i)
		else:
			repeat= -repeat
			for i in self.combs:
				if i.count(item) <= repeat: newcombs.append(i)
		self.combs=newcombs.copy()
	
def new():
	shape = input("shape?")
	total = input("total?")
	newregion = puzzle_region(shape, total)
	newregion.setcombs()
	puzzle_array.append(newregion)
def filter(arraynr, item, repeat):
	puzzle_array[arraynr].filter(item, repeat)
def show(verbose=False):
	for i in puzzle_array:
		i.getproperties()
		if verbose: i.getcombs()
def getcommand(cmd):
	cmd=cmd.split(' ')
	func=cmd[0]
	if func == 'exit':
		exit()
	arg=''
	if len(cmd) > 1:
		for i in cmd[1:]: arg = arg + ',' + str(i)
	arg=arg[1:]
	result=f"{func}({arg})"
	return result

while True:
	command=getcommand(input("?"))
	try:
		exec(command)
	except Exception as e:
		print(e)
