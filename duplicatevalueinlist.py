# Lab-6: Write a function to find Duplicate values in the List..
def duplicateInlist(lst:list) -> tuple :
    '''A function that returns the collection of all the duplicate values
    present in the passed list'''
    
    items = set()   # an empty set 
    for item in lst:  #iterating the list
        if lst.count(item) > 1 :   
            #if occurence of any item is greater than 1 then add the item in set.
            items.add(item)
            
    return tuple(items) 


# Driver code
a = [100,2,30,20,100,90,1,0,30,1,32,100]
print(duplicateInlist(a))