#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
def find(s, p='.'):
	for d in os.listdir(p):
		curpath = os.path.join(p,d)
		if os.path.isdir(curpath):
			find(s, curpath)
			continue
		if os.path.isfile(curpath) and s in d:
			print(curpath)
			continue


if __name__ == '__main__':
	find('py')
	find('Test','d:\javastudy')