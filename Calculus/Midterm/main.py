import math 
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

A=input("Please enter A(from 10 to 99):")
x= sp.symbols('x')
fx=x*x - 2*A*x-A*A
gx=-x*x + 4*A*x+A**3