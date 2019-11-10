import functools as ft
import numpy as np
fib = [0,1]
array = np.array([])
def fib(integer):
    if integer < 0:
        print("Not a valid input")
    elif integer <= len(fib):
        return fib[integer - 1]
    else:
        temp_fibonacci =
