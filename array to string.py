''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    i=int(input())
    l = list(map(int,input().split()))
    a= list()
    for j in range(0,i):
        if(l[j]%2==0):
            a.append(str(l[j]))
    print("".join(a))



main()

# input
# 6
# 22 21 47 34 78 91

# output
# 223478