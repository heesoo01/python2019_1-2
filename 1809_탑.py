#1809_탑
a=int(input("몇개의 탑?:"))
building=[]
arr=[0]*a
for i in range(0,a):
    b=int(input("%d번의 탑 높이:"%(i+1)))
    building.append(b)
for i in range(a-1,-1,-1):
    check=0
    for j in range(i,-1,-1):
        if(building[i]<building[j]):
            check=j+1
            #print(check)
            break
    print(check)
    arr[i]=check
print(arr)
        
