# sort an array of 0,1 and 2 without using any sorting algo
# this approach will use o(n)+o(n) time i.e o{2n} time ! so thats why it is not efficeint enough! 

# ar=[0,0,1,2,1,1,1,1,2,2,0,0,0,0,1,1,1,2]
# def sortinganarray(ar):
#     a=0
#     b=0
#     c=0
#     for i in range(0,len(ar)):
#         if(ar[i]==0):
#             a+=1
#         if(ar[i]==1):
#             b+=1
#         if(ar[i]==2):
#             c+=1
#     print(a,b,c)
#     for i in range(0,a):
#         ar[i]=0
#     for i in range(a,a+b):
#         ar[i]=1
#     for i in range(a+b,a+b+c):
#         ar[i]=2
#     print(ar)
# sortinganarray(ar)




#sorting the array using the dutch algorithm in which we are keeping big values at the last samll values at the front and mid values are untouched
ar=[0,0,1,2,1,1,1,1,2,2,0,0,0,0,1,1,1,2]

def arraysort(ar):
    low=0
    mid=0
    high=len(ar)-1
    while mid<=high:
        print(low,mid,high)
        if(ar[mid]==0):
            ar[low],ar[mid]=ar[mid],ar[low]
            mid=mid+1
            low=low+1
        elif(ar[mid]==1):
            mid=mid+1
        else:
            ar[mid],ar[high]=ar[high],ar[mid]
            high=high-1
        
    print(ar)

arraysort(ar)


