#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):
	def __init__(self, name, score):
		#self.name = name
		#self.score = score
		self.__name = name
		self.__score = score
	def print_score(self):
		print('%s: %d' %(self.__name, self.__score))
lisa = Student('Lisa', 99)
baba = Student('Baba', 88)
lisa.print_score()
lisa.age = 0
print('lisa.age: %d' % lisa.age)
print('baba._Student__score: %d' % baba._Student__score)
print(baba.score)
#print(baba.age)