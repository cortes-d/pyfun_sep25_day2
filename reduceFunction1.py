
"""
The reduce() function
"""
import functools

data=[2,-4,6,-7,8,-8,19,10]

def fct(a, b):
    return a+b

result=functools.reduce(fct, data)
print(result)



