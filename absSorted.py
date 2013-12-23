def sumUp(arrayAbs,k):
    for index in range(len(arrayAbs)):
        value=arrayAbs[index]
        tempValue=k-value
        result=AbsBS(arrayAbs,abs(tempValue))
        if result is not -1:
            return [index,result]
    return [-1,-1]



def AbsBS(array,target):
    l,r=0,len(array)-1
    while l<=r:
        mid=l+(r-l)/2
        midValue=abs(array[mid])
        if midValue==target:
            return mid
        elif midValue<target:
            l=mid+1
        else:
            r=mid-1
    return -1

def main():
    testAbs=[-49,75,103,-147,164,-197,-238,314,348,-422]
    total=1670
    print sumUp(testAbs,total)

if __name__=="__main__":
    main()
