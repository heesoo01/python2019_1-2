#1971044 정희수
def add(x,y):
    print("%d + %d" %(x,y),end="")
    return x+y

def sub(x,y):
    print("%d- %d"%(x,y),end="")
    return x-y

def mult(x,y):
    print("%d * %d" %(x,y),end="")
    return x*y

def div(x,y):
    if(y==0):
        print("0으로 나눌 수 없습니다:")
        return 0
    print("%d // %d"%(x,y),end="")
    return x//y

def mod(x,y):
    if(y==0):
        print("0으로 나눌 수 없습니다:")
        return 0
    print("%d %% %d"%(x,y),end="")
    return x%y

def show_menu():
    print("-------------------------------------------------------")
    print("1.더하기 2.빼기 3.곱하기 4.나누기(몫) 5.나누기(나머지) 6.두 정수 입력받기 0.종료")
    print("-------------------------------------------------------")
    
def input_num(msg):
    value=int(input(msg))
    return value

menu='1'
n1=0
n2=0
while menu!='0':
    show_menu()
    menu=input("menu:")
    if(menu=='0'):
        print("종료합니다.")
        break
    if(menu=='1'):
        res=add(n1,n2)
    if(menu=='2'):
        res=sub(n1,n2)
    if(menu=='3'):
        res=mult(n1,n2)
    if(menu=='4'):
        res=div(n1,n2)
    if(menu=='5'):
        res=mod(n1,n2)
    if(menu=='6'):
        n1=input_num("정수:")
        n2=input_num("정수:")
        continue
    
    print(" = %d" %res)

   

