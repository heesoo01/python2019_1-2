#1086_성적관리프로그램

def putScore():
    lt=[]
    i=0
    while(i<7):        
        n=int(input("%d번의 과목 점수를 입력하세요:"%(1+i)))
        if(n>=0 and n<=100):
            lt.append(n)
            i+=1
        else:
            print("범위를 맞춰주세요")
            continue  
    return lt

subject=[]
subject=putScore()
sum=0
for i in range(0,len(subject)):
    sum+=subject[i]
print("총점:%d"%sum)
print("평균:%d"%(sum/len(subject)))
great=subject[0]
small=subject[0]
for i in range(0,len(subject)-1):
    if(great<subject[i+1]):
        great=subject[i+1]
    if(small>subject[i+1]):
        small=subject[i+1]
print("최대=%d, 최소=%d"%(great,small))
subject.append(sum/len(subject))
subject.append(great)
subject.append(small)
for i in range(10,0,-1):
    print("%2d"%(i*10),end="")
    for t in range(0,10,1):
        if (subject[t]/10>=i):
            print("%2s"%"*",end="")
        else:
            print("  ",end="")
    print()
print("   ",end="")   
for i in range(0,10):
    print("%c "%(65+i),end="")
    
