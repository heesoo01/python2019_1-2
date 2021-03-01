#기본 코드업 1410 올바른 괄호 개수 세기
string = input("?:")
open=0
close=0
for i in range(0,len(string)):
    if string[i]=="(":
        open+=1
    if string[i]==")":
        close+=1
print("open:%d, close:%d"%(open,close))
