#!/usr/bin/python3

from datetime import datetime

class greatlie:
	def __init__(self, wanted_choice):
		self.list_lies = []
		self.list_answers = []
		self.date_lies = []
		self.date_answers = []
		self.list_lies.append(wanted_choice)
		self.date_lies.append(datetime.now())
	def setlie(self,wanted_choice):
		self.list_lies.append(wanted_choice)
		self.date_lies.append(datetime.now())
	def setanswer(self, answer):
		self.list_answers.append(answer)
		self.date_answers.append(datetime.now())
	def islie():
		if self.list_lies[-1] == self.list_answers[-1]:
			return False
		return True
	def getanswer():
		return self.list_lies[ 1]
		
object_greatlie = greatlie(3)
