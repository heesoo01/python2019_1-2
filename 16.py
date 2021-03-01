a=""
b=""
for i in range(1,101,1):
    십=i//10
    일=i%10
    if(십 !=0 and 십%3==0):a="짝"
    if(일!=0 and 일%3==0):b="꿍"
    print("%d: %s%s"%(i,a,b))
    a=""
    b=""
