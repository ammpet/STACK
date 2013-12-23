#Simple Implementation of Binary Search
#Author Lexie

import random

#Iterative Way
def iterative_BS(lst,target):
    start=0
    end=len(lst)-1
    '''
    Cannot use while True! Because once the target is not in the list,
    the while loop will run forever!
    '''
    while start<=end:
        mid=start+(end-start)/2
        if lst[mid]==target:
            return [mid,"Find IT"]
        elif lst[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return [-1,"Missed It"]
#recursive way of implementation
def recursive_BS(lst, target,start,end):
    if start>end:
        return [-1,"Missed It"]
    mid=start+(end-start)/2
    if lst[mid]==target:
        return [mid,"Find It!"]
    elif lst[mid]<target:
        return recursive_BS(lst,target,mid+1,end)
    else:
        return recursive_BS(lst,target,start,mid-1)

def main():
    length=10
    target=100
    arr=sorted(random.sample(range(50),length))
    result=iterative_BS(arr,target)
    print result
    print recursive_BS(arr,target,0,len(arr)-1)
if __name__=="__main__":
    main()
