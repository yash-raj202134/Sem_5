''' A Function to convert given list to string'''
def listToString(lst):
    return ''.join(lst)   # returns a string

'''Function for generating different permutations of the passed string'''
result_permutation=[]  # an empty list to store the permutations
def permutation(string,s_index,e_index):  
    cur_index = 0   # current index is assigned to zero
    if s_index == e_index-1:  
        result_permutation.append(string) # appends all the permutations in the list result_permutation
    else:   
        for cur_index in range(s_index,e_index):
            i = list(string)   
            #Swapping the string by fixing the  character  
            temp = i[s_index] 
            i[s_index] = i[cur_index]
            i[cur_index] = temp  
            
            #Recursively calling function permutation()
            permutation(listToString(i),s_index+1,e_index)
            #Swapping the string by fixing the character  
            temp = i[s_index]
            i[s_index] = i[cur_index]  
            i[cur_index] = temp
    
    return result_permutation

string = "XYZ"     # given string
print(permutation(string,0,len(string)))  #permutation function call
    
