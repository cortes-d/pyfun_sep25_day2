"""
    Define a function isPrime which purpose is to determine if
    the number it receives as argument is a prime number or not.
    
    Step1:
        test the argument received to ensure it is an int > 1
    Step2:
        with the help of a loop try to divide the argument received 
        (lets call it "number") by 2,3,4,5, up to number-1
        For instance, if number is 17 you can test: 2,3,4,5,...,15,16
        Ex: if number % 2 == 0 then 2 is a divisor of number
        As soon as you find a divisor of "number" you can return False
    Step3:
        At the end of the loop, you will have tested all possible
        divisor of number, you can return True: "number" is a 
        prime number
"""

def isPrime(aNumber):
    """
    isPrime returns True or False depending on the fact that aNumber
    is a prime number or not
    
    Parameters
    ----------
    aNumber : the int to be tested

    Returns
    -------
    True if aNumber is a prime number.
    False if aNumber is not a prime number.
    None if an error is encountered.

    """
    if not isinstance(aNumber, int):
        print("Wrong argument given: should be an int!")
        return None
    if aNumber <= 1:
        print("Wrong argument given: should be an int > 1!")
        return None
    for divisor in range(2,aNumber):
        if aNumber % divisor == 0:
            return False
    return True

nb=int(input("Enter a positive int: "))
result = isPrime(nb)
if result == True:
    print(nb, "is a prime number")
elif result == False:
    print(nb, "is not a prime number")
else:
    print("There is something wrong ...")