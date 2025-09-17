
d1=[2,3,-4,5,6,-10,23]
print(d1)

# Version 1

result=[]
for e in d1:
    if e > 0:
        result.append(e**3)
print(result)

# Version 2: here a list comprehension is used

result=[e**3 for e in d1 if e > 0]
print(result)