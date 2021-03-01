#1658_최대공약수와최소공배수
def gcd_get(x,y):
    gcd=0
    for i in range(1,x+1):
        if(x%i==0 and y%i==0):
            gcd=i
    return gcd

n=int(input("?:"))
p=int(input("?:"))
gcd=gcd_get(n,p)
lcm=n*p/gcd
print("gcd=%d, lcm=%d"%(gcd,lcm))
            
