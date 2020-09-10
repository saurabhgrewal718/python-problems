# create a new dict from i to n ....(including both) such that the elemnts of dict are (i,i*i)...and print the dict after that

first_num = int(input("Enter first number : "))
last_num = int(input("Enter last number : "))
d = dict()

for i in range (first_num,last_num+1):
    d[i] = i*i

print(d)

