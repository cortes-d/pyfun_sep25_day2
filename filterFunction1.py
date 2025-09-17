
"""
The filter() function
"""

result=[2,-4,6,-7,8,-8,19,10]

def fct(arg):
    return arg >=0

result=list(filter(fct, result))
print(result)

def iseven(arg):
    return arg%2 == 0

result=list(filter(iseven, result))
print(result)

