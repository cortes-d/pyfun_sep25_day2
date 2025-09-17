def myfunction(arg1=0, arg2=0):
    if isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
        temp = arg1 - arg2 # temp is a "local" variable
        return temp
    else:
        print("Wrong argument received:", arg1)
        return None


result=myfunction(30,20) # positional arguments
print("result is", result)

result=myfunction(30) # positional arguments
print("result is", result)

result=myfunction() # positional arguments
print("result is", result)
