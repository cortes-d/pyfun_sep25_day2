def removeAll(data, value):
    if isinstance(data, list):
        while value in data:
            data.remove(value)
            
d=[5,6,5,7,5,8,10]

print(d)

removeAll(d, 5) # positional arguments

print(d)

removeAll(data=d, value=7) # named arguments

print(d)

