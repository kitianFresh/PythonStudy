#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import functools

def log(text='execute'):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			print('begin call')
			func(*args, **kw)
			print('end call')
		return wrapper
	return decorator

@log('call')
def now():
	print('2016/4/14')

@log()
def then():
	print('2015/4/14')
	
