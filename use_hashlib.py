#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
db = {}

def get_md5(s):
	md5 = hashlib.md5()
	md5.update(s.encode('utf-8'))
	return md5.hexdigest()

def register(username, password):
	db[username] = get_md5(password + username + 'the-Salt')

def login(username, password):
	content = password + username + 'the-Salt'
	md5 = hashlib.md5()
	md5.update(content.encode('utf-8'))
	return db[username] == md5.hexdigest()

if __name__ == '__main__':
	while True:
		username = input('please input username: ')
		password = input('please input password: ')
		register(username, password)
		username = input('please input username again: ')
		password = input('please input password again: ')
		print(login(username, password))