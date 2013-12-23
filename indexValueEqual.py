'''
Given a sorted array A of distinct integer, and return an index i such that
A[i]=i or indicate that no such index exists by returning -1
'''
import copy
def IndexValueEqual(lst):
    l,r=0,len(lst)-1
    while l<=r:
        mid=l+(r-l)/2
        print "lf",[l,r,mid]
        if lst[mid]==mid:
            return [mid,lst[mid]]
        elif mid<lst[mid]:
            r=mid-1
        elif mid>lst[mid]:
            l=mid+1
    return -1

def subtractIndex(lst):
    indeices=range(len(lst))
    tempArray=copy.deepcopy(lst)
    for i in indeices:
        tempArray[i]=lst[i]-i
    return tempArray

def BS(lst,target):
    l,r=0,len(lst)-1
    while l<=r:
        mid=l+(r-l)/2
        if lst[mid]==target:
            return mid
        elif lst[mid]<target:
            l=mid+1
        elif lst[mid]>target:
            r=mid-1
    return -1

def duplicateIndexValueEqual(lst):
    '''
    lst-index, convert this problem to binary locate 0
    running Time O(n)
    '''
    tempArray=subtractIndex(lst)
    print "Temp",tempArray
    '''
    No binary Seach since the array is not sorted
    '''
   #result=BS(tempArray,0)
    for i in range(len(tempArray)):
        if tempArray[i]==0:
            return ["Yes",i,lst[i]]
    return "No A[i]==i"


def main():
    testList=[-5,-2,0,3,5,7]
    print "List",testList
    print "inde",range(0,len(testList))
    print IndexValueEqual(testList)
    testList2=range(1,8)
    print testList2
    print IndexValueEqual(testList2)
    testDuplicate=[1,2,3,4,5,5,7,9]
    print testDuplicate
    print duplicateIndexValueEqual(testDuplicate)

if __name__=="__main__":
    main()
