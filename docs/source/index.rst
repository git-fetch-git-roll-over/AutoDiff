AutoDiff: Software Library Documentation
==================================================

..
    Authors:  Peyton Benac, Max CemIvan Shu and Seeam Shahid Noor
    ^^^^^^^^^^^^^^^^
Introduction
============
In engineering, statistical modelling, and countless other scientific disciplines, derivatives are calculated to measure change in a dynamic system. It is crucial for professionals of all kinds who work with quantitative systems to have access to software that can calculate derivatives quickly, efficiently, and with a simple-to-use interface. That is why ``TensorFlow`` exists. Our software package, ``AutoDiff``, will try to do the same.

``AutoDiff`` performs automatic differentiation to machine precision, as well as improves computational costs. This documentation walks through some of the mathematics of automatic differentiation, as well as some basic information about the usage of our library.

.. image:: ../../images/dog.jpg
  :width: 600

Background
==========
Computing gradients the old-fashioned way (by hand) is certainly feasible for many mathematical functions that appear in many applications. A key step in almost every derivative is known as the chain rule, which applies whenever our function's inner structure is a composition of functions, e.g.,

:math:`\\f(x, y) = g(h(x, y))`

Here's an example of computing the gradients of the function 

:math:`\\f(x, y) = \sin(2x + 3y)e^{-x^2}`

The partial derivative $\partial f/\partial x$ can be calculated using the product rule and the chain rule:

:math:`\partial f/\partial x = \sin(2x + 3y)(-2x)e^{-x^2} + 2\cos(2x + 3y)e^{-x^2}`

The partial derivative $\partial f/\partial y$ only needs to be calculated using the chain rule, since a term only involving x is constant with respect to y:

:math:`\partial f/\partial y = 3\cos(2x + 3y)e^{-x^2}`


We can represent the function's individual operations in a graphical format:

By parsing the structure of the function :math:`\\f(x, y)` into its atomic building blocks, we can construct atrace table from which we can read the results of the chain rule at every step of the computation.

.. image:: ../../images/func_graph.jpeg
  :width: 600

The fact that this process is **automatic** comes very much in handy when computing gradients of more complex functions, for example:

:math:`f(x,y) = 3sin(e^{6x - ln(4y^3 - 3x^2)} + 17\sqrt{y^5-tanh(x)})17(4x^{1/3}+29yln(x - y))^{7/19}`

Yeah, we would prefer not to do that by hand.

How to use package
==================

How to install
--------------

Go to the directory that you want to run this package, and then open your command line prompt. 

* ``https://github.com/git-fetch-git-roll-over/AutoDiff.git`` to download the package
* ``cd AutoDiff`` to go inside the directory
* ``virtualenv autodiff`` to create a virtual environment
* ``source autodiff/bin/activate`` to activate the environemnt
* ``pip install -r requirements.txt`` to install the necessary dependencies
* ``cd forward_mode`` to go inside the modules
* create your own driver script and please follows the basic demo for an illustration

Basic Demo
----------

Say there is a simple function and we want to get the derivative at :math:`x=4`:

:math:`f(x) = sin(x) + cos(x)`

First, from the module variable.py import class ``Variable`` and from function.py import class ``Function``::

    from variable import Variable
    from function.Function import sin, cos 

Then create an instance of Variable class and construct your elementary functions :math:`sin(x), cos(x)`::
    
    x = Variable(name='x', val=4)
    f1 = sin(x)
    f2 = cos(x)

Last create a variable f to add of your f1 and f2 and print out f::

    f = f1 + f2 
    print(f)
    >>> sinx+cosx: sinx+cosx value: -1.410; derivative: 0.103


Software organization
=====================

Directory Structure
-------------------

With our main directory ``cs107-FinalProject``, We plan to organize our package as follows:

* dependencies in ``requriements.txt``
* continuous integration ``.travis.yml`` 
* code coverage ``.codecov.yml``
* documentation in ``\docs``
* test suite in ``\tests``
* code in ``\forward_mode``
* images in ``\images``

Basic Modules
-------------

We plan to include two modules called variable.py and function.py and they create instances of single input variable and computes the value and derivative via the forward mode of automatic differentiation.  

How to Tests
------------

Both ``TravisCI`` and ``CodeCov`` are used and  our test suite will live inside our repositary in a ``\tests`` directory.

Future Installation 
-------------------

As of now, we primarily distribute our code by having clients clone our github repositary, but we hope to also make it pip-installable. For the future, we plan to package our project using `wheels <https://www.python.org/dev/peps/pep-0427/>`_. This should make it easily pip installable.


Implementation Details
======================

Descriptions
------------

We used ``numpy`` arrays as our core data structure, because this will make it easy to perform operations on either single values or single or multidimensional arrays. Our only external dependency should be ``numpy``. 

The main class of this package is the are ``Variable`` and ``Function`` classes and ``Variable`` creates instances of single input varaibles. This class contains arrtibutes such as *name*, *value* and default *derivative*. On the other hand, ``Function`` classes creates basic elementary function methods (e.g. :math:`sin, cos, tan, exp` and :math:`log`)


Future Direction
----------------

We are planning to extend our basic automatic differentation package to handle cases where involves multi dimensional inputs and outputs. We are also interested in implementating an extra feature either with dual numbers or optimatization. 

.. toctree::
   :maxdepth: 2
   :caption: Contents:

    licencse
    help


..
    Indices and tables
    ==================

    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`
