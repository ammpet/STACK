def cycleMinimum(cycleArray):
    '''
    this one equals to find the pivot of this rotated array
    '''
    i,j=0,len(cycleArray)-1
    while cycleArray[i]>cycleArray[j]:
        mid=i+(j-i)/2
        if cycleArray[mid]>cycleArray[j]:
            #upper bound is unsorted
            l=mid+1
        else:
            r=mid
    return l
    '''
    if i>j:
        return -1
    if i==j:
        return i
    if cycleArray[i]<cycleArray[j]:
        return cycleArray[i]
    mid=i+(j-i)/2
    print [i,j,mid]
    if cycleArray[mid]<=cycleArray[j]:
        return cycleMinimum(cycleArray,i,mid)
    elif cycleArray[mid]>cycleArray[j]:
        return cycleMinimum(cycleArray,mid+1,j)
    '''

def cycleK(lst,k):
    l,r=0,len(lst)-1
    while l<=r:
        mid=l+(r-l)/2
        if lst[mid]==k:
            return mid
        elif lst[mid]<lst[r]:
            #upper bound is sorted
            if lst[mid]<k and k<=lst[r]:
                l=mid+1
            else:
                r=mid-1
        elif lst[l]<=lst[mid]:
            #lower bound is sorted
            if lst[l]<=k and k<lst[mid]:
                r=mid-1
            else:
                l=mid+1


if __name__=="__main__":
    test=[5,1,2,3,4]
    print cycleK(test,1)



'''



def main():
    testCycle=[4,5,1,2,3]
    testCycle=[1,0,1,1,1]
    print cycleMinimum(testCycle,0,len(testCycle)-1)

if __name__=="__main__":
    main()
'''
