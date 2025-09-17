# Here **numbers means fact accepts a variable number of "named arguments.
# These arguments are available via a dict which name is numbers

def fct(**numbers):
    print(numbers)

fct(a=5,file="data.txt",sep=",")

