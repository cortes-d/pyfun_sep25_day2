PI=3.1415

def removeAll(data, value):
    """
    RemoveALL is a function that removes from a list
    all occurences of an element

    Parameters
    ----------
    data : a list
      
    value : the value to be removed

    Returns
    -------
    None.

    """
    if isinstance(data, list):
        while value in data:
            data.remove(value)
            
def mysum(*args):
    """
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
