#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    helper.__name__= func.__name__

    return helper

@call_counter
def succ(x):
    return x + 1

print('callable: %s' %[attr for attr in dir(succ) if callable(attr)])
print('not callable: %s' %[attr for attr in dir(succ) if not callable(attr)])
print(succ.calls)
for i in range(10):
    print(succ(i))
    
print(succ.calls)