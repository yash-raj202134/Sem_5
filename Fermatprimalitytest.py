# Lab-10: Primality Test using Fermat method

def exponent(x,n):
    '''a utility function to compute power of x using log n time'''
    if n==0:
        return 1
    elif n==1:
        return x
    else:
        m = exponent(x,n//2)
        if n % 2==0:
            res = m * m
        else:
            res = m * x * m
    return res

def primalityTest(num):
    '''a function to check whether a number is prime or not using Fermat method'''
    if num == 0 or num == 1 : return False
    
    for a in range(2,num-1):
        E = exponent(a,num-1)  # calling exponent function to compute power
        
        if E % num != 1 : # condition.
            return False
            
    return True  # if condition satisfies.

# Driver code:
num = 11
print(primalityTest(num))