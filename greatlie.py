#!/usr/bin/python3

from datetime import datetime

class greatlie:
	def __init__(self, number_choices, wanted_choice):
		self.number_choices = number_choices
		self.list_lies = []
		self.list_answers = []
		self.list_lies.append(wanted_choice)
		self.nlies=1
		self.nanswers=0
		self.date_lies = []
		self.date_answers = []
		self.date_lies.append(datetime.now())
	def setlie(self,wanted_choice):
		self.list_lies.append(wanted_choice)
		self.nlies+=1
		self.date_lies.append(datetime.now())
	def setanswer(self, answer):
		self.list_answers.append(answer)
		self.nanswers+=1
		self.date_answers.append(datetime.now())
	def islie():
		if self.list_lies[self.nlies-1] != self.list_answers[self.nanswers-1]:
			return True
		else:
			return False
	def getanswer():
		return self.list_lies[self.nlies - 1]
		
var_greatlie = greatlie(3,1)
