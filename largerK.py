'''
Given a sorted array A and a key k, find the index of the first
occurance an element larger than k; return -1 if every element is
less than or equal to k.
'''

def search_first_larger_k(lst,k):
    l,r,pos=0,len(lst)-1,-1
    while l<=r:
        mid=l+(r-l)/2
        if lst[mid]<k:
            l=mid+1
        elif lst[mid]==k:
            pos,r=mid,mid-1
        elif lst[mid]>k:
            r=mid-1
    return pos

def main():
    testList,k=[1,2,3,3,3,4,4,5,6,7,8],11
    print testList
    print search_first_larger_k(testList,k)

if __name__=="__main__":
    main()

