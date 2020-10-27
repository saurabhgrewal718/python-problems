a=[10,20,30,40,50,60,65,66,56,4564,5,52]
k=int(input())

def maxm(k,a):
    a.sort()
    print(a)
    print(k,"smallest is ",a[k-1])
    print(k,"largest is ",a[len(a)-k])

maxm(k,a)     
