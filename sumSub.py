#O(n) running time with additional space
#trade space with time

def sum(lst,total):
    result=[]
    extra={}
    print len(extra)
    for j in range(len(lst)):
        extra[total-lst[j]]=[j,lst[j]]

    for i in range(len(lst)):
        if extra[lst[i]]!=-1:
            result.append([i,extra[lst[i]][0]])
    if len(result)==0:
        return [-1,-1]
    else:
        return result

def main():
    test=[0,1,5,3,6,9,8,10];
    print sum(test,9)
if __name__=='__main__':
    main()
