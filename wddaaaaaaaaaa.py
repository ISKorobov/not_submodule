
from random import randint
def sortir(a,l,r,k):
    print()
    print(l,r)
    if (l+1>=r):
        return a[k]
    chislo=a[randint(l,r)]
    m=l
    mi=[]
    ma=[]
    c=0
    for i in range(l,r+1):
        if(a[i]<chislo):
            mi.append(a[i])
        elif(a[i]>chislo):
            ma.append(a[i])
        else:
            c+=1
    a=[]
    for i in range(len(mi)):
        a.append(mi[i])
    for i in range(c):
        a.append(chislo)
    for i in range(len(ma)):
        a.append(ma[i])
    m=len(mi)
    print(chislo)
    print(a)
    print(m,k)
    if(m==0 and k==2):
        return
    if(k==m):
        print(a[m])
        return a[m]
    if(k<m):
        sortir(a,l,m,k)
    if(k>m):
        sortir(a,m,r,k)
a=[1,2,80,-50,103]
b=(sortir(a,0,4,2))
print(b)

