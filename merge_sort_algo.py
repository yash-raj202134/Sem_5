
"""Lab 2 : Implement Merge Sort Algorithm with all the necessary functions."""
def merge(arr,left,right):
    '''A utility function that simply merges 2 passed sorted array or a list''' 
    i=j=k=0  # starting indices
    while i < len(left) and j < len(right):  
        if left[i] <= right[j] :  # comparing left and the right array elements
            arr[k]=left[i]   # assigning the shortest element to our original array
            i+=1   
        else:
            arr[k]=right[j] 
            j+=1
        k+=1  
    
    # checking for the left out element in left array just in case
    while i < len(left): 
        arr[k]=left[i]
        i+=1
        k+=1
    # checking for the left out element in right array 
    while j < len(right): 
        arr[k]=right[j]
        j+=1
        k+=1
        

def mergeSort(arr):
    '''MergeSort function to implement merge sort technique ''' 
    
    # exit condition
    if len(arr)<=1: # already sorted 
        return   # return nothing
    # calculating mid of the array passed
    mid = int(len(arr)/2) 
    Left = arr[:mid]  # creating Left array (from start till the mid value)  
    Right = arr[mid:] # creating Right array(from mid value till the end)
    mergeSort(Left) # recursive call for left array 
    mergeSort(Right)  # recursive call for right array
    merge(arr,Left,Right)  # finally merge 

# Driver code:
array = [14, 146, 43, 27, 5, 41, 45, 21, 0] # test case
mergeSort(array)
print(array)


