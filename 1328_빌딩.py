#1328_빌딩

a=int(input("빌딩 몇개?:"))
building=[]
for i in range(0,a):
    c=int(input("%d번째 빌딩의 높이:"%(i+1)))
    building.append(c)

for i in range(a):
    check=0
    for k in range(i,a):
        if(building[i]<building[k]):
            check=(k+1)
            continue
    print(check)
