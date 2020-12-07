# :)
import numpy as np
import pandas as pd
import graddog.calc_rules as calc_rules
Ops = calc_rules.Ops
from graddog.compgraph import CompGraph

# TODO: dunder methods for comparison operators like __lt__ <

# TODO: figure out how to recursively print a trace object's FULL formula 
# because a Trace element no longer stores its full own formula
# e.g.

# f = sin(x) - cos(3y)

# v1 = x
# v2 = y
# v3 = sin(v1)
# v4 = 3*v2
# v5 = cos(v4)
# v6 = v3 - v5 <------ f



# TODO: add missing docstrings


class Trace:
	'''
	This is a class for creating single Trace element.
	'''
	def __init__(self, formula, val, der, parents, op = None, param = None):
		'''
		The constructor for Trace class.

		Adds the new trace element to the CompGraph

		'''
		self._formula = formula

		# val stores the value
		self._val = val

		# der stores the derivative
		self._der = der

		# parents stores the 1 or 2 parent Trace object(s)
			# for example:
			# if v3 = v1+v2, then v3._parents = [v1, v2]
			# if v5 = sin(v4), then v5._parents = [v4]
		# is an empty list [] if this is a variable
		self._parents = parents

		# op stores the operation: '+', 'sin', etc
		# 
		# op is None if this is a variable
		self._op = op

		# optional parameter for a function, e.g. the base of a logarithm
		self._param = param

		# accesses the current CompGraph to know what this Trace's tracename should be
		# because we number the traces in order of their creation in the computational graph
		self._trace_name = CompGraph.add_trace(self)

		#name by default is the trace name, but can be changed to something like 'Cost' or 'Objective' or 'Loss'
		self._name = self._trace_name

			
	@property
	def name(self):
		'''
		Returns non-public attribute _name
		'''
		return self._name

	@name.setter
	def name(self, new_name):
		'''
		This resets the _name of a Trace instance
		'''
		self._name = new_name

	@property
	def val(self):
		'''
		Returns non-public attribute _val
		'''
		return self._val

	@val.setter
	def val(self, new_val):
		'''
		This resets the _val of a Trace instance
		'''
		if isinstance(new_val, numbers.Number):
			self._val = new_val
		else:
			raise TypeError('Value should be numerical')

	@property
	def der(self):
		'''
		Returns non-public attribute _der

		If the function is single-variable, returns as a scalar instead of a dictionary

		Optional parameter: key, for example 'x', so that the user can call f.der('x')
		'''

		if len(self._der) == 1:
			return list(self._der.values())[0]
		return self._der

	def der_wrt(self, key):

		# current design choice
		# if the key doesnt exist yet the derivative still is zero
		# because why not :)
		try:
			return self._der[key]
		except KeyError:
			return 0

	def __repr__(self): 
		return self._name

	def __eq__(self, other):
		try:
			return self.val == other.val
		except AttributeError:
			return self.val == other


	def __add__(self, other):
		'''
		This allows to do addition with Trace instances or scalar numbers. 
		AttributeError is caught when input `other` is not a instance of 
		Trace class. 

		Parameters:
			other (Trace, float or int)

		Returns Trace: contains new formula, new value and new derivative.
		'''
		return two_parents(self, Ops.add, other)


	def __radd__(self, other):
		'''
		This is called when int or float + an instance of Variable class.
		
		Returns Trace: contains new formula, new value and new derivative
		'''
		return self.__add__(other)

	def __sub__(self, other):
		'''
		This allows to do subtraction with Trace instances or scalar numbers. 
		AttributeError is caught when input `other` is not a instance of 
		Trace class. 

		Parameters:
			other (Trace, float or int)

		Returns Trace: contains new formula, new value and new derivative.
		'''
		return two_parents(self, Ops.sub, other)

	def __rsub__(self, other):
		'''
		This is called when int or float - an instance of Trace class.

		Returns Trace: contains new value and new derivative
		'''
		return one_parent(self, Ops.sub_R, other)

	def __mul__(self, other):
		'''
		This allows to do Multiplication with Trace instances or scaler number. 
		AttributeError is caught when input other is not a instance of 
		Trace class. 

		Parameters:
			other (Trace, float or int)

		Returns Trace: contains new formula, new value and new derivative.
		'''
		return two_parents(self, Ops.mul, other)

	def __rmul__(self, other):
		'''
		This is called when int or float / an instance of Trace class.

		Returns Trace: contains new formula, new value and new derivative
		'''
		return self.__mul__(other)

	def __truediv__(self, other):
		'''
		This allows to do Division with Trace instances or scalar number. 
		AttributeError is caught when input `other` is not a instance of 
		Trace class. 

		Parameters:
			other (Trace, float or int)

		Returns Trace: contains new formula, new value and new derivative.
		'''
		return two_parents(self, Ops.div, other)

	def __rtruediv__(self, other):
		'''
		This is called when and int or float / Trace instance
		
		Returns Trace: contains new formula, new value and new derivative
		'''
		return one_parent(self, Ops.div_R, other, formula = str(other) + '/' + self._trace_name)    
	
	def __neg__(self):
		'''
		This allows to negate Trace instances itself.
		
		Returns Trace: contains instance name, (-1) * instance value and (-1) * instance derivative.
		'''
		return one_parent(self, Ops.sub_R, 0, formula = '-'+self._trace_name)

	def __pow__(self, other):
		'''
		This allows to do Trace ^ Trace or scalar number. 
		AttributeError is caught when input `other` is not a instance of 
		Trace class. 

		Parameters:
			other (Trace, float or int)

		Returns Trace: contains new formula, new value and new derivative.
		'''
		return two_parents(self, Ops.power, other)
	
	def __rpow__(self, other):
		'''
		This is called when int or float ^ Trace instance
		
		Returns Trace: contains new formula, new value and new derivative
		'''
		return one_parent(self, Ops.exp, other, formula = str(other) + '^' + self._trace_name)

def one_parent(t, op, param = None, formula = None):
	'''
	Creates a trace from one parent, with an optional parameter and optional formula
	'''
	try:
		new_formula =  f'{op}({t._trace_name})'
		if formula:
			new_formula = formula
		val = calc_rules.val(t, op, param)
		der =  calc_rules.deriv(t, op, param)
		parents = [t]
		return Trace(new_formula, val, der, parents, op, param)	
	except AttributeError:
		# when t is actually a vector input, we are still able to apply the op to the whole vector (e.g. sin([x1,x2]) = [sin(x1),sin(x2)])
		return np.array([one_parent(t_, op, param, formula) for t_ in t])

def two_parents(t1, op, t2, formula = None):
	'''
	Creates a trace from two parents, with an optional formula
	'''
	try: 
		# when t2 is a trace
		new_formula =  t1._trace_name + op + t2._trace_name
		val = calc_rules.val(t1, op, t2)
		der =  calc_rules.deriv(t1, op, t2)
		parents = [t1, t2]
		return Trace(new_formula, val, der, parents, op)
	except AttributeError: 
		# when t2 is actually a constant, not a trace, and this should really be a one parent trace
		return one_parent(t1, op, t2, formula = t1._trace_name + op + str(t2))


