#1971044 정희수
def show_array(seat, row, col):
    for r in range(0,row):
        print("%2d : "%(r+1),end=" ")
        for c in range(0,col):
            if(seat[r][c]==0):
                print("□",end=" ")
            else:
                print("■",end=" ")
        print()
def ticket(a):
    if(a=="성인"):
        value=7000
    if(a=="청소년"):
        value=9000
    return value
    
def show_menu():
    print("---------------------------------------------")
    print("1.좌석보이기 2.예약하기 3.취소하기 0.종료하기")
    print("---------------------------------------------")
    
#main()    
print("/////////////////////////////////////////////////")
print("%25s"%("이화극장"))
print("/////////////////////////////////////////////////")
n=0
b=int(input("성인 몇명입니까?:"))
c=int(input("청소년 몇명입니끼?:"))
price=b*ticket("성인")+c*ticket("청소년")
seat=[[0]*10 for _ in range(10)]
while True:
    show_menu()
    menu=int(input("menu : "))
    if(menu==1):
        show_array(seat,10,10)   
    if(menu==2):
        num=int(input("예약할 좌석의 개수를 입력하세요."))
        n+=num
        if(n>b+c):
            print("예매 가능한 좌석의 개수를 넘었습니다.")
            n-=num
            continue
        for i in range(0,num):
            x=int(input("예약할 행:"))
            y=int(input("예약할 열:"))
            if(seat[x-1][y-1]==0):
                seat[x-1][y-1]=1
            else:
                print("이미 예약된 자석입니다.")
                continue            
    if(menu==3):
        num=int(input("취소할 좌석의 개수를 입력하세요."))
        n-=num
        if(n>(b+c) or n<0):
            print("취소 가능한 좌석의 개수를 넘었습니다.")
            n+=num
            continue
        for i in range(0,num):
            x=int(input("취소할 행:"))
            y=int(input("취소할 열:"))
            if(seat[x-1][y-1]==1):
                seat[x-1][y-1]=0
            else:
                print("이미 취소된 자석입니다.")
                continue
    if(menu==0):
        if(b+c==n):            
            print("좌석예매를  종료합니다.")
            break
        else:
            print("총 %d명의 좌석 예매가 완료되지 않았습니다."%(b+c))
            print("%d명의 좌석을 더 예매해주세요."%(b+c-n))
            continue
            
print("성인 %d명, 청소년 %d명으로 총 가격은  %d원 입니다."%(b,c,price))
print("즐거운 영화관람 되세요.")
    
