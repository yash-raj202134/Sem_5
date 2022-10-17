# Lab 5 : Job sequencing Problem
def jobsequencing(arr: list, m: int) -> list:
    '''a function to implement job sequencing problem'''
    '''sorting the passed array 
    on the basis of their deadlines''' 
    
    arr = sorted(arr, key=lambda i: i[2], reverse=True) 
   
    max_profit = 0
    max_list = [] # an empty list to collect results
    for a in range(len(arr)-1): # logic to get maximum item for 2 same deadlines 
        if arr[a][2] == arr[a+1][2]:
            max_item = arr[a]
            break

    for i in range(m): # to create a slot equal to the max deadline
        max_item = (max_item[0], 0, 0)
        for item in arr: # iterating list.
            if item[2] == i+1 and item[1] > max_item[1]:
                max_item = item  # assigning the max item after it satisfies the job sequencing conditions.

        max_list.append(max_item)  # appending the result 

    return [[i[0],i[1]] for i in max_list] # return list of jobs.


# Driver code:
jobs = input("Enter jobs : ")   #taking jobs as input (seperated by ",")
jobs = list(jobs.split(','))  # creating list of jobs

profits = input("Enter profits : ") # taking profits input
profits = list(profits.split(','))
profits = [int(i) for i in profits]  #creating list of profits

deadlines = input("Enter deadlines :") # taking deadlines input
deadlines = list(deadlines.split(','))
deadlines = [int(i) for i in deadlines] #creating list of deadlines

# a data model arr to store list of tuples of jobs , profits , deadlines
arr = [(jobs[i], profits[i], deadlines[i]) for i in range(len(jobs))]

print(jobsequencing(arr, max(deadlines))) # calling the function jobsequencing
