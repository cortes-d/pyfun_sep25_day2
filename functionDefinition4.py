# Here *args means mysum accepts a variable number of positional arguments.
# These arguments are available via a tuple which name is args
    
def mysum(*args): 
    """
    A docstring:
    mysum is a function whihch purpose is ....
    ....
    Parameters
    ----------
    *args : a collection of 0 up to n numbers
    
    Returns
    -------
    total : a numeric value: the sum of the numbers received
    
    """
    total=0
    for e in args:
        total += e
    return total
    
   
result=mysum(2,7,8,24,2,1,2) # positional arguments
print("result is", result)
result=mysum() # positional arguments
print("result is", result)
result=mysum(12,56) # positional arguments
print("result is", result)

