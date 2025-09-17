"""
    Define a function addList() which purpose is to add 2 lists
    of numbers given as arguments, element by element.
    
    Example:
        l1=[5,6,3]
        l2=[1,0,-1,10]
        l3=addList(l1, l2) # l3 is [6,6,2,10]
        
"""

def addList(list1, list2, default=0):
    """
    addList will add the elements of the two lists received as argument by pair.
    In case the 2 lists are not of the same size, the element that exist in one
    list and not the other will be added to the value default

    Parameters
    ----------
    list1 : a list of numbers
        
    list2 : a list of numbers
       
    default: an int with a default value of 0
    
    Returns
    -------
    newList : a new list

    """
    newList=[]
    
    if len(list1) > len(list2):
        for index in range(len(list2)): 
            newList.append(list1[index]+list2[index])
        for index in range(len(list2), len(list1)): 
            newList.append(list1[index]+default)
    else:
        for index in range(len(list1)):
            newList.append(list1[index]+list2[index])
        for index in range(len(list1), len(list2)):
            newList.append(list2[index]+default)
            
    return newList

# This is an alternative possible implementation:
    
def addList_version2(list1, list2, default=0):
    #list1=[2,3,4,7,8]
    #list2=[2,23,5]
    #list2.extend([4,4])
    
    newList=[]
    # First I do extend the shortest list:
    if len(list1) > len(list2):
        list2.extend([default]*(len(list1)-len(list2)))
    else:
        list1.extend([default]*(len(list2)-len(list1)))
    # Now the 2 list are of the same size!
    for index in range(len(list1)):
        newList.append(list1[index]+list2[index])
    return newList


d1=[2,3,4,7,8]
d2=[2,23,5]

d3=addList(d2,d1) 

print(d3) # [4, 26, 9, 7, 8]
d3=addList(d1,d2) 

print(d3) # [4, 26, 9, 7, 8]

d3=addList(d1,d2,3) 

print(d3) # [4, 26, 9, 10, 11]

d3=addList_version2(d1,d2,3) 

print(d3) # [4, 26, 9, 10, 11]