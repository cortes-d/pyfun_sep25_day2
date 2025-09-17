
"""
a str is "sequence":
    len(), for, in, not in, [], [:], [::], +, *, ...
"""
# Creation

nb=3
text=f"nb is {nb} nb ** 2 is {nb**2}" 
print(text)

nb=99
text=f"nb is {nb} nb/3 is {10/3}" 
print(text)

nb=99
text=f"nb is {nb:>10} nb/3 is {10/3:.2f}" 
print(text)

nb=str(3.45)
print(nb, type(nb))