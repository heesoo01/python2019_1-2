#1971044 정희수
#n=회차, p=입금액 pe=연이율 t=총액 pem=월이율
def bank(end,start,p,pe,t):
    print("%4s %4s %8s %8s"%("회차","입금액","이율(월%)","총"))
    for i in range(end,start+1,1):
        t=p+t*(1+pe/12/100)
        print("%4d %8d %8.2f %16.2f"%(i,p,pe/12,t))
    return t
        
        

##########################################
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("이화뱅크")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

per=float(input("저축이율을 입력하세요(연%):"))
put=int(input("한 달에 저축할 금액:"))
num=int(input("얼마동안 저축할까요?(월):"))
goal=int(input("목표액은 얼마인가요(원):"))
total=0
print("--------------------------------------")
tot=bank(1,num,put,per,total)

if(goal>tot):
    print("목표금액까지 %.2f원이 부족합니다."%(goal-tot))
    print("지금부터 약 %d개월 더 저축하면 됩니다."%((goal-tot)//put))
    a=input("저축을 이어서 계속하시겠습니까?(Y,N):")
    if(a=='Y'):
        t=int(bank(num+1,((goal-tot)//put)-1,put,per,tot))
        print("축하축하! 목표금액을 달성했습니다.")
        print("예금을 종료합니다!")
    else:
        print("이화뱅크를 종료합니다.")
else:
    print("축하축하! 목표금액을 달성했습니다.")
    print("예금을 종료합니다!")

print("이화뱅크를 사용해주셔서 감사합니다")
        
