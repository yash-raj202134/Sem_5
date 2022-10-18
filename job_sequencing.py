# Lab 5 : Job sequencing Problem
def jobsequencing(arr: list, m: int) -> list:
    '''a function to implement job sequencing problem'''
    
    '''sorting the passed array 
    on the basis of their deadlines'''  
    arr = sorted(arr, key=lambda i: i[2], reverse=True) 
   
    count = 0 # for counting jobs added to sequence
    job_sequence=[None]*m
    for item in arr:
        if count >= m:
            break
        i=0
        for i in range(item[2]-1,-1,-1):
            if job_sequence[i] == None:
                job_sequence[i] = (item[0],item[1])
                count+=1
                break
    
    return job_sequence # return list of jobs.

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
