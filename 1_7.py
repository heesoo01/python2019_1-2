#1971044 정희수



def fact(n):
    
    print(n,end="* ")
    
    if(n==1): return 1
    
    return n*fact(n-1)

n=5
res=fact(n)
print("%d!=%d"%(n,res))
