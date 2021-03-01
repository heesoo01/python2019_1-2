#정희수 1971044
def shrimp():
    value=7320
    print("새우볶음밥 : %d"%value)
    print("새우볶음밥을 만듭니다")
    return value
    
def kimchi():
    value=6530
    print("김치볶음밥 : %d"%value)
    print("김치볶음밥을 만듭니다")
    return value

def meat():
    value=6670
    print("스팸볶음밥 : %d"%value)
    print("스팸볶음밥을 만듭니다")
    return value

def egg(n):
    value=n*500
    print("계란후라이 : %d"%value)
    return value
    
def soda(n):
    value=n*1000
    print("사이다 : %d"%value)
    return value
    
def coke(n):
    value=n*1100
    print("콜라 : %d"%value)
    return value

def plus():
    value=0
    a=input("음료를 추가하시겠습니까?:(예,아니오):")
    if(a=='예'):
        a=input("사이다와 콜라중에 선택하세요(1,2):")
        if(a=='1'):
            a=int(input("몇 개?:"))
            value+=soda(a)
        else:
            a=int(input("몇 개?:"))
            value+=coke(a)
            
    a=input("계란후라이를 추가하시겠습니까?:(예,아니오):")
    if(a=='예'):
        a=int(input("몇 개?:"))
        value+=egg(a)
    return value

def show_menu():
    print("-------------------------------------------------------")
    print("1.새우볶음밥 2.김치볶음밥 3.스팸볶음밥 0.종료")
    print("-------------------------------------------------------")
print("///////////////////////////////////////////")
print("이화볶음밥에 오신걸 환영합니다!")
print("///////////////////////////////////////////")
price=0
total=0
pay=0
while True:
    show_menu()
    menu=input("메뉴:")
    if menu=='0':break
    if menu=='1':
        price=shrimp()+plus()
    if menu=='2':
        price=kimchi()+plus()
    if menu=='3':
        price=meat()+plus()
    if menu<'0' or menu>'3':
        print("그런 메뉴는 없습니다.")
        continue
    print(" 가격 : %d"%price)
    price-=price%100
    print(" 할인가격: %d"%price)
    total+=price
    print("총 가격: %d"%total)
print("주문을 종료합니다!")
print("총 계산된 금액: %d"%total)
pay=int(input("받은 금액"))
left=pay-total
print("%d원을 거슬러주어야 합니다."%left)
a=left//10000
b=left%10000//5000
c=left%10000%5000//1000
d=left%10000%5000%1000//500
e=left%10000%5000%1000%500//100
f=left%10000%5000%1000%500%100
print("10000원 개수:%d \n5000원 개수: %d \n1000원 개수: %d \n500원 개수: %d \n100원 개수:%d"%(a,b,c,d,e))
print("100원 미만인 나머지 잔돈:%d원은 불우이웃에게 기부합니다."%f)



              
              
    
