
def findElements(arr,n):
    i=1
    j=0
    for i in range(n+1):
        if(i==arr[i-1]):
            j=i
            print(j)
    
    if(j==0):
        print("no match found")

        
arr = [15, 2, 45, 12, 7] 
n = len(arr) 
findElements(arr, n) 
