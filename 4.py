import random
num=random.randint(0,101)
print("num:%d"%num)
i=0
limit=3

while True:
    if(i==limit):
        print("3번의 기회를 모두 쓰셨습니다!")
        break
    user=int(input("[%d]:숫자를 입력하세요:"%(i+1)))
    if(user==num):
        print("Bingo!")
        break
    if(user>num):
        print("Down!")
    else:
        print("Up!")
    i+=1
    
