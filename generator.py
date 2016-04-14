#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def triangles(max):
	L = [1]
	n = 0
	while n < max:
		yield L
		L.append(0)
		L = [L[i-1] + L[i] for i in range(len(L))]
		n = n + 1
	return 'done'
n = 0
for l in triangles(15):
	print(l)