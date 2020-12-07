import numpy as np
from graddog.variable import trace
from graddog.functions import sin, cos, tan, exp, log
from graddog.compgraph import CompGraph

from graddog import hello

# Hi I'm graddog

# I can fetch you the derivative of any function f : Rm --> Rn

# Just use trace(f, seed). 

# I figures out how many variables you want from the seed, 
# then I trace the path of the function to build a computational graph. 
# I use it to calculate derivatives

def demo0():
	print('demo 0')
	print('A function R --> R using variable-input')

	def f(x):
		return x**3 - 4*x + cos(exp(-sin(tan(log(x)))))

	seed = [1.0]
	assert seed[0] > 0 # input to log must be positive
	trace(f, seed)
	CompGraph.show_trace_table()
	CompGraph.forward_mode()
	CompGraph.reverse_mode()
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def demo1():
	print('demo 1')
	print('A function Rm --> R using variable-input')

	def f(x, y):
		return x*y + exp(x*y)

	trace(f, seed = [1, 2])
	CompGraph.show_trace_table()
	CompGraph.forward_mode()
	CompGraph.reverse_mode()
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def demo2():
	print('demo 2')
	print('A function Rm --> R using vector-input')

	def f(v):
		
		return v[0] + 3*v[2]**2

	trace(f, seed = [1,2,3])
	CompGraph.show_trace_table()
	CompGraph.forward_mode()
	CompGraph.reverse_mode()
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def demo3():
	print('demo 3')
	print('A function Rm --> Rn using vector-input')

	def f(v):
		return [v[0] + 3*v[2]**2, v[1] - v[0], v[2] + sin(v[1])]

	trace(f, seed = [1,2,3])
	CompGraph.show_trace_table()
	CompGraph.forward_mode()
	CompGraph.reverse_mode()
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def demo4():
	print('demo 4')
	print('A function Rm --> Rn using variable-input')

	def f(x, y, z):
		return [exp(-(sin(x) - cos(y))**2), sin(- log(x) ** 2 + tan(z))]

	f = trace(f, seed = [np.pi/2,np.pi/3,np.pi/4])
	CompGraph.show_trace_table()
	CompGraph.forward_mode()
	CompGraph.reverse_mode()
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def demo5():
	print('demo 5')

	def f(x, y):
		return [x,y]

	f = trace(f, seed = [np.pi/2,np.pi/3])
	CompGraph.show_trace_table()
	CompGraph.forward_mode()
	CompGraph.reverse_mode()
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def run_demos():
	l = [demo0, demo1, demo2, demo3, demo4, demo5]
	for d in l:
		d()


