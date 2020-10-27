
# best time in which the negitive elements can be moved in the begining

a=[-1,-2,3,-34,-3,-2,-4,2,-2,-3,34,345,-5,3,-4,-1,-2,3,-34,-3,-2,-4,2,-2,-3,34,345,-5,3,-4,-1,-2,3,-34,-3,-2,-4,2,-2,-3,34,345,-5,3,-4,-1,-2,3,-34,-3,-2,-4,2,-2,-3,34,345,-5,3,-4,-1,-2,3,-34,-3,-2,-4,2,-2,-3,34,345,-5,3,-4]

def moving(a):
    l = 0
    m = 0
    for i in range(0,len(a)):
        if(a[i]<0):
            a[l],a[m] = a[m],a[l]
            l=l+1
            m=m+1
        else:
            m=m+1
    print(a)

moving(a)
            

