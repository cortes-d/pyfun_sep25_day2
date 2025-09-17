"""  
Given a file with this format (you can use "data.txt" for instance or create your own test file):

    x1:0.34;x2:0.56
    x1:0.24;x2:0.45
    x1:0.27;x2:0.55
    ...

extract out of it the numerical values associated with x1 and x2.
The values associated with x1 will be stored in a list with the name X1.
The values associated with x2 will be stored in a list with the name X2.

To extract the 2 float out of each line you could:
    1) use slices
    2) use 2 split() methods
    3) use another strategy ??
    
Create a list Y1 that will contain the cosine of each value stored in X1 
(use the math.cos() function)

Create a list Y2 that will contain the sine of each value stored in X2 
(use the math.sin() function)

"""

import math

dataFile=open("data.txt")

X1=[]
X2=[]

for line in dataFile: # The for loop read the file line by line

    # A example of what a line looks like: "  x1:2.24;x2:2.58\n"
    
    # This is to "uniformise" the separator (":" only):
    line=line.replace(";",":")  
    # "  x1:2.24:x2:2.58\n"
    
    # To split each line into 4 parts:
    listOfTokens=line.split(":")
    
    if len(listOfTokens) != 4:
        print(f"The line {line} cannot be processed !")
        continue  # switch to the next line of the file (the next iteration)
    
    # The float values are at position 1 and -1:
    try:
        value1=float(listOfTokens[1]) 
    except ValueError:
        value1=0
        
    try:
        value2=float(listOfTokens[-1])
    except ValueError:
        value2=0
    

    # The float values are stored into 2 distinct lists: X1 and X2
    X1.append(value1)
    X2.append(value2)

        
print("X1:", X1)
print("X2:", X2)

Y1=[]
Y2=[]

# for e in X1:
#     Y1.append(math.cos(e))

# for e in X2:
#     Y2.append(math.sin(e))

for ix in range(len(X1)):
    Y1.append(math.cos(X1[ix]))
    Y2.append(math.sin(X2[ix]))
    
print("Y1:", Y1)
print("Y2:", Y2)    
