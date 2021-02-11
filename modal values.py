def main():
    i = int(input())
    l = list(map(int,input().split()))
    m = {}
    for co in l:
        m.setdefault(co,0)
        m[co] = m[co] +1
    a = list()
    for f in m.keys():
        a.append(f)
    print(a[0])
    

    
        


main()