# Lab 1 : Implement Binary Search

class Solution(object):
    '''A function to implement a binary search in a given sorted list  using iteration'''
    def binarySearchIteration(self, lst, key):
        low = mid = 0
        high = len(lst)-1
        while(low <= high):
            mid = int((low+high)/2)
            if key == lst[mid]:
                return mid
            elif key > lst[mid]:
                low = mid+1
            else:
                high = mid-1
        return -1
    
    '''A function to implement a binary search in a given sorted list using Recursion'''
    def binarySearchRecursion(self,lst,low,high,key):
        sol=Solution()
        mid=int((high+low)/2)
        if key==lst[mid]:
            return mid
        elif key > lst[mid]:
            if mid==high:
                return -1
            return sol.binarySearchRecursion(lst,mid+1,high,key)
        else:
            if mid==0:
                return -1
            return sol.binarySearchRecursion(lst,low,mid-1,key)
        
sol = Solution()
ls = [2, 16, 32, 90, 167, 1001, 5002, 7890, 20279]  # note :list or array must be sorted
target = -2  
print(sol.binarySearchRecursion(ls, 0,len(ls)-1,target)) # returns -1 if target element is not present in the list
print(sol.binarySearchIteration(ls, target)) # returns -1 if target element is not present in the list
