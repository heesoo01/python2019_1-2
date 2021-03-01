id="jhs"
passwd="qwert"
i=0
while(True):
    s=input("아이디를 입력하시오:")
    if s!=id:
        print("아이디를 찾을 수 없습니다.")
    else:
        print("환영합니다.")        
        while(True):
            p=input("비밀번호를 입력하시오:")
            if p==passwd:
                print("로그인되었습니다.")
                i+=1
                break;
            else:
                print("비밀번호가 틀렸습니다.")
    if i==1:
        break;
 
