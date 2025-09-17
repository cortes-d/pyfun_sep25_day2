def myfunction(arg1, arg2):
    if isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
        temp = arg1 * arg2 # temp is local variable
        return temp
    else:
        print("Wrong argument received:", arg1, arg2)
        return None
        # raise ValueError("Wrong arg received")

nb=5 # nb is global variable
result=myfunction(12,nb)
print("result is", result)

result=myfunction("abc", 3)
print("result is", result)

print("The end")

