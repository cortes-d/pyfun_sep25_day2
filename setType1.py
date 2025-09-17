"""
Set: a kind of mutable collection
"""

s1={3,4,5,10,-3,4,10}

print("s1:",s1)
print("length of s1:",len(s1))

for e in s1:
    print(e)

s1=set([23,45,67,78,23])
print(s1)

s1.add(100)
print(s1)

s2={67,78,200,220}
print(s2)

s3=s1.union(s2)
print(s3)

s3=s1.intersection(s2)
print(s3)

d=[23,45,67,78,23]

d1={e**2 for e in d} # set comprehension

print(d1)

