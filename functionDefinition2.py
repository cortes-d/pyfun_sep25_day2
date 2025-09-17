def myfunction(arg1, arg2):
    if isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
        temp = arg1 - arg2 # temp is local variable
        return temp
    else:
        print("Wrong argument received:", arg1)
        return None

nb=5 # nb is global variable
result=myfunction(12, nb) # positional arguments
print("result is", result)

result=myfunction(arg2=12, arg1=nb) # named arguments
print("result is", result)
