#Problem 11.1

def search_first(lst,target):
    left=0
    right=len(lst)-1
    while left<=right:
        mid=left+(right-left)/2
        if lst[mid]==target:
            index,right=mid,mid-1
        elif lst[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return index

def main():
    lst=[222,333,444,555,555,666]
    target=666
    print search_first(lst,target)

if __name__=="__main__":
    main()

