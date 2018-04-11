#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__='N SUN'

import sys

def test():
	args=sys.argv
	if len(args)==1:
		print ('hello world')
	elif len(args)==2:
		print('hello %s!' %args[1])
	else:
		print('too much arguments')

if __name__=='__main__':
	test()


def _pravite_1(name):
	print('hello %s!' %name)
def _pravite_2(name):
	print('hi %s!' %name)
def greetings(name):
	if (len(name)>2):
		_pravite_1(name)
	if (len(name)<=2):
		_pravite_2(name)
greetings('NOLAN')
greetings('ns')