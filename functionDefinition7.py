
def fct(**numbers):
    print(numbers)

print(fct(a=5,file="data.txt",sep=","))

d1=[2,3,4]
d2=[7,8,9]
d3=[7,8,9]
print(list(zip(d1,d2,d3)))



for ix,val in enumerate(d1):
    print(ix, "->", val)