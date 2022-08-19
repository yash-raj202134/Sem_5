# Lab 1 : A function which return all the unique palindromes from a given string

'''A function to check whether a given object is palindrome or not'''
def isPalindrome(x):
    s=str(x)
    for i in range(len(s)):
        if s[i]!=s[len(s)-1-i]:
            return False
    return True

"""A function to collect all the palindrome sets present in the passed string"""
def palindromeInString(s):
    result=[]    # an empty list to collect the result
    for i in range (len(s)):  
        temp="" # empty string
        for j in range(i,len(s)):
            temp=temp+s[j] # appends the previous character to the next character for every iteration of j
            if isPalindrome(temp):
                if len(temp) > 1:  # condition to check whether a string has len > 1 
                                   # since isPalindrome() returns True for single character
                    result.append(temp)
    return result

if __name__ == '__main__':
    s='cdozvzoroba'
    print(palindromeInString(s))
    
    
    
