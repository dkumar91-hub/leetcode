def twosum(l1,n):
    l2 = []
    for i in range(0,len(l1)-1):
        n2 = (n-l1[i])
        if n2 in l1:
            l2.append(i)
            l2.append(l1.index(n2))
            return l2
        else:
            return "value not found"
l1=[1,3,8,7]
n = 8
print(twosum(l1,n))