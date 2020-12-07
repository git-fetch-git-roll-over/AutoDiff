# :)
import numpy as np
import graddog.math as math
from graddog.trace import Trace, one_parent

'''
Any implementable unary (one_parent) or binary (two_parent) operations can be added here
'''

def sin(t : Trace):
    '''
    This allows to create sin().

    Parameters:
        t (Trace instance)

    Return Trace that constitues sin() elementary function
    '''
    return one_parent(t, math.Ops.sin)

def cos(t : Trace):
    '''
    This allows to create cos().

    Parameters:
        t (Trace instance)

    Return Trace that constitues cos() elementary function
    '''
    return one_parent(t, math.Ops.cos)

def tan(t : Trace):
    '''
    This allows to create tan().

    Parameters:
        t (Trace instance)

    Return Trace that constitues tan() elementary function
    '''
    return one_parent(t, math.Ops.tan)

def exp(t : Trace, base=np.e):
    '''
    This allows to create exp().

    Parameters:
        t (Trace instance)
        base (int, or float)

    Return Trace that constitues exp() elementary function with input base (default=e)
    '''
    formula = None
    if base != np.e:
        formula = f'{np.round(base,3)} ^ ({t._trace_name})'
    return one_parent(t, math.Ops.exp, param = base, formula = formula)

def log(t : Trace, base=np.e):
    '''
    This allows to create log().

    Parameters:
        t (Trace instance)
        base (int, or float)

    Return Trace that constitues log() elementary function with input base (default=e)
    '''
    formula = None
    if base != np.e:
        formula = f'log_{np.round(base,3)}({t._trace_name})'
    return one_parent(t, math.Ops.log, base, formula = formula)

def sinh(t : Trace):
    '''
    This allows to create sinh().

    Parameters:
        t (Trace instance)
        base (int, or float)

    Return Trace that constitues sinh() elementary function
    '''
    return one_parent(t, math.Ops.sinh)

def cosh(t : Trace):
    '''
    This allows to create cosh().

    Parameters:
        t (Trace instance)

    Return Trace that constitues cosh() elementary function
    '''
    return one_parent(t, math.Ops.cosh)

def tanh(t : Trace):
    '''
    This allows to create tanh().

    Parameters:
        t (Trace instance)

    Return Trace that constitues tanh() elementary function
    '''
    return one_parent(t, math.Ops.tanh)

def sqrt(t : Trace):
    '''
    This allows to create sqrt().

    Parameters:
        t (Trace instance)

    Return Trace that constitues sqrt() elementary function
    '''
    return one_parent(t, math.Ops.sqrt)

def sigmoid(t : Trace):
    '''
    This allows to create sigmoid().

    Parameters:
        t (Trace instance)

    Return Trace that constitues sigmoig() elementary function
    '''
    return one_parent(t, math.Ops.sigm)

