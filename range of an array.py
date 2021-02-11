''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    i = int(input())
    l = list(map(int,input().split()))
    l.sort()
    print(l[-1]-l[0])

main()


# input
# 6
# 90 98 100 102 105 110
