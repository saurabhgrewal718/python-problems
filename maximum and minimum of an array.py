# a=[12,2,2,34,235,67,43,45,567,65,83,258,74,54,767]
# a.sort()
# lastelement= a[len(a)-1]
# firstelement = a[0]
# print(lastelement,firstelement)
# print(a) 

def arrayfun(a):
    if(len(a)<1):
        return "empty array"
    elif(len(a)==1):
        return (a[0])
    elif(len(a)==2):
        if(a[0]<a[1]):
            return a[0]
        else:
            return a[1]
    elif(len(a)>3):
        return a
        

a=[]
b= arrayfun(a)
print(b)
