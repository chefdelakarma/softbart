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
			self.shape=[ int(i) for i in shape.split(',') ]
		if isinstance(shape, list):
			self.shape=shape
		self.number_of_boxes=sum(self.shape)
		self.items=list(range(1,size+1))
		self.combs = []
		
	def setcombs(self):
		if operator == "sum":
			for i in combinations_with_replacement(self.items, self.number_of_boxes):
				if sum(i) == self.total:
					self.combs.append(i)
		if operator == "product":
			for i in combinations_with_replacement(self.items, self.number_of_boxes):
				if math.prod(i) == self.total:
					self.combs.append(i)
		self.remove_multiple()
	def getcombs(self):
		for i in self.combs:
			print(i)
	def getproperties(self):
		print(f"size: {self.size}, total: {self.total}, size: {self.size}, operator: {self.operator}")
	def filterout(self, item, repeattimes):
		item=int(item)
		newcombs=[]
		for i in self.combs:
			c = i.count(item)
			if c < repeattimes
				newcombs.append(i)
		self.combs=newcombs
	def filterin(self, item, repeattimes):
		item=int(item)
		newcombs=[]
		for i in self.combs:
			c = i.count(item)
			if c > repeattimes
				newcombs.append(i)
		self.combs=newcombs
	def remove_multiple(self):
		newcombs=[]
		multiple=len(self.shape ) if len(self.shape) < max(self.shape) else max(self.shape)
		for i in items:
	 		for j in self.combs:
	 			count=j.count(i)
	 			if count <= multiple:
	 				newcombs.append(j)
	 	self.combs=newcombs
	
def create_region():
	shape = input("shape?")
	total = input("total?")
	newregion = puzzle_region(shape, total)
	puzzle_array.append(newregion)
def filter(arraynr, in_or_out, number, repeattimes):
	if in_or_out == "in":
		puzzle_array[arraynr].filterin(number, repeattimes)
	if in_or_out == "out":
		puzzle_array[arraynr].filterout(number, repeattimes)
	
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
