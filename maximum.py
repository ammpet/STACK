#Consider an Array consists of a strictly ascending sequence, followed by a descending sequence

def maximum(lst,l,r):
    mid=l+(r-l)/2
    if lst[mid-1]<=lst[mid] and lst[mid]>=lst[mid+1]:
        return [mid,lst[mid]]
    elif lst[mid-1]<lst[mid]:
        return maximum(lst,mid+1,r)
    elif lst[mid-1]>lst[mid]:
        return maximum(lst,l,mid-1)

def main():
    testList=range(1,3)
    temp=range(1,10)
    temp.reverse()
    testList.extend(temp)
    print testList
    print maximum(testList,0,len(testList))

if __name__=="__main__":
    main()

