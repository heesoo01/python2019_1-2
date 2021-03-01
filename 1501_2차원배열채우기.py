#2차원 배열 채우기
i=int(input("?:"))
mem=[[0]*i for _ in range(i)]
i=1
for k in range(0,3):
    for t in range(0,3):
        mem[k][t]=i
        i+=1
print(mem)
