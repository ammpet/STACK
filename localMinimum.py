'''
In special case where a[0]>=a[1] and a[n-2]<=a[n-1],
algorithm workis in O(logn).
'''
def localMinimum(lst,start,end):
    if start>end:
        return -1
    mid=start+(end-start)/2;
    if lst[mid-1]<=lst[mid] and lst[mid]>=lst[mid+1]:
        return mid
    elif lst[mid-1]>lst[mid]:
        return localMinimum(lst,start,mid-1)
    elif lst[mid]<lst[mid+1]:
        return localMinimum(lst,mid+1,end)


def main():
    testList=[1,13,12,18,19,20,7,6,5,4,3,2,1]
    print testList
    print localMinimum(testList,0,len(testList)-1)


if __name__=="__main__":
    main()
