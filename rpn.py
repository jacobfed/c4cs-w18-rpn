#!/usr/bin/env python3

import operator

operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'S': sum,
	'!': operator.mul,
        'C': operator.add,
        '^': operator.pow,
}

def factorial(arg):
	defualt = 1
	if arg == 0:
		return default
	else:
		for i in range (1, arg):
		    arg *= i
		return arg

def calculate(arg):
	stack = list()
	for token in arg.split():
		try:
			value = int(token)
			stack.append(value)
		except ValueError:
	      		#if token != '!':
			function = operators[token]
			if token == 'S':
				result = function(stack)
				stack = list()
				stack.append(result)
			elif token == '!':
				arg = stack.pop()
				result = factorial(arg)
				stack.append(result)
			elif token == 'C':
				arg = stack[0]
				stack.insert(0, arg)
			else:
				arg2 = stack.pop()
				arg1 = stack.pop()
				result = function(arg1,arg2)
				stack.append(result)
		print(stack)	
	if len(stack) != 1:
		if token != 'C':
			raise TypeError
	return stack.pop()
def main():
	while True:
		print(calculate(input('rpn calc> ')))

if __name__ == '__main__':
	main()

