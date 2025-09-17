d1=[2,3,4,5,6,10,23]
print(d1)

# def fct(arg):
#     return arg**3

result=list(map(lambda arg: arg**3, d1))

print(result)

import functools

data=[2,-4,6,-7,8,-8,19,10]

# def fct(a, b):
#     return a+b

result=functools.reduce(lambda a, b: a+b, data)
print(result)

result=[2,-4,6,-7,8,-8,19,10]

# def fct(arg):
#     return arg >=0

result=list(filter(lambda a: a >= 0, result))
print(result)

# def iseven(arg):
#     return arg%2 == 0

result=list(filter(lambda a: a%2 == 0, result))
print(result)