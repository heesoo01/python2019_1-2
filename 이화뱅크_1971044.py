#1971044 정희수
def bank(start,end,total,goal,rate,push):
    print("%4s %4s %8s %8s"%("회차","입금액","이율(월%)","총"))
    print(start,",",end)
    for i in range(start,end+1):
        if(goal<=total):
            break
        else:
            total=push+total*(1+rate/12/100)
            print("%4d %8d %8.2f %16.2f"%(i,push,rate/12,total))
    return total

#####################################################################
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("이화뱅크")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

per=float(input("저축이율을 입력하세요(연%):"))
put=int(input("한 달에 저축할 금액:"))
goal=int(input("목표액은 얼마인가요(원):"))
total=0.0
start=1
while (True):
    print("--------------------------------------")
    num=int(input("얼마동안 저축할까요?(월):"))
    total=bank(start,start+num-1,total,goal,per,put)
    start+=num
    if(goal<=total):
        break
    print("목표금액까지 %.2f원이 더 부족합니다."%(goal-total))
    print("지금부터 약 %d개월 더 저축하면 됩니다."%((goal-total)//put))
    a=input("저축을 이어서 계속하시겠습니까?(예,아니오):")
    if(a=='예'):
        continue
    else:
        print("예금을 종료합니다.")
        break
    
if(goal<=total):
        print("목표금액 달성!")
        print("예금을 종료합니다.")
print("이화뱅크를 사용해주셔서 감사합니다")

    
