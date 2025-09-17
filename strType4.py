"""
a str is "sequence":
    len(), for, in, not in, [], [:], [::], +, *, ...
"""
# Creation

nb=3
text=f"nb is {nb} nb ** 2 is {nb**2}" 

for e in text[5:15]:
    print(e)

text="marTiNi"
print()
print(text)    
result=text.capitalize()
print("result is",result)
print("text is",text)

text="earth.gif"
if text.endswith("gif"):
    print(text, "is a gif file")
    
text="this is a first   example    of a    multi-part  str"
result=text.split()
print(result)

text="x1:3.45:x2:6.78:y1::6.78"
result=text.split(":")
print(result)

data=["x1","3.4", "x2", "4.5"]
result=";".join(data)
print(result)

text="   the text itself    "
print(text, len(text))
result=text.rstrip()

print(result, len(result))
result=text.lstrip()
print(result, len(result))
result=text.strip()
print(result, len(result))

text="*****the text itself **"
print(text, len(text))
result=text.rstrip("*")
print(result, len(result))
result=text.lstrip("*")
print(result, len(result))
result=text.strip("*")
print(result, len(result))

text="x1:3.45:x2:6.78:y1:6.78"
bis=text
print(text, id(text))
text=text.replace(":",";")
print(text, id(text))

#import re # regular expression
