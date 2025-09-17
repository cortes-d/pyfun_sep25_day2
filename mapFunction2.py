
"""
The map() function
"""

text="23:56:67:89:12:43"
result=text.split(":")
print(result)
result=list(map(int, result))
print(result)
print(sum(result))
