#player는 name, hp, power 정보 저장
#5명 이상의 서로 다른 player들의 리스트 생성
#A팀, B팀 모두 랜덤하게 3명씩 고름
#한 팀의 멤버가 모두 죽어서 0명이 되면 게임을 종료
#남은 멤버가 1명이라도 있으면 우승
import random
def makePlayer(n):
    member=[[0]*3 for _ in range(n)]
    for i in range(0,n):
        print("------%d번째 player------"%(i+1))
        name=input("player의 namer을 정해주세요:")
        member[i][0]=name
        hp=int(input("player의 hp를 정해주세요:"))
        member[i][1]=hp
        power=int(input("player의 power를 정해주세요:"))
        member[i][2]=power
    return member
        
def makeTeam(team,players,num):
    m_no=[]
    i=0
    while (i<3):
        k=random.randint(0,num-1)
        if k in m_no:
            continue
        else:
            m_no.append(k)
            for t in range(0,3):
                team[i][t]=players[m_no[i]][t]
            i+=1

def showTeam(team,name):    
    print("-----------------------------------------------")
    print("   %s팀 - %d 명"%(name,len(team)))
    print("-----------------------------------------------")
    print("    이름     :          hp            power")
    print("-----------------------------------------------")
    for i in range(len(team)):
          print(" %5s   %10d   %10d"%(team[i][0],team[i][1],team[i][2]))
          
def showTeams(team1,team2,name1,name2):
    print("--------------------------------------------------------------")
    print("  %s팀 - %d 명                %5s팀 - %d 명"%(name1,len(team1),name2,len(team2)))
    print("--------------------------------------------------------------")
    print("  이름 :    hp      power  |  이름 :    hp      power    ")
    for i in range(0,3):
        if(i<len(team1)):
            print("%s:%6d%6d       "%(team1[i][0],team1[i][1],team1[i][2]),end=" ")
        else:
            print("                          ",end=" ")
        if(i<len(team2)):
            print("%6s:%6d%6d       "%(team2[i][0],team2[i][1],team2[i][2]))
        else:
            print()
    print("--------------------------------------------------------------")

def attack(team1,team2):
    k=random.randint(0,1)
    if k==0:        
        at=team1[random.randint(0,len(team1)-1)]
        ta=team2[random.randint(0,len(team2)-1)]
        print("A:",at[0],"공격!---->","B:",ta[0])
        ta[1]-=at[2]
    if k==1:        
        at=team2[random.randint(0,len(team2)-1)]
        ta=team1[random.randint(0,len(team1)-1)]
        print("A:",ta[0],"<----공격!","B:",at[0])
        ta[1]-=at[2]
        
def check(team):
    for i in range(0,len(team)):
        if(team[i][1]<=0):
            del team[i]
            
            
#main                    
num=int(input("몇명의 player를 만드시겠습니까?:(5명 이상)"))
mem_list=[[0]*3 for _ in range(num)]
mem_list=makePlayer(num)
#A,B team생성
A=[[0]*3 for _ in range(3)]
B=[[0]*3 for _ in range(3)]
makeTeam(A,mem_list,num)
makeTeam(B,mem_list,num)
showTeam(A,"A")
showTeam(B,"B")
showTeams(A,B,"A","B")

print("===================battle start=======================")
while True:
    if len(A)==0:
        print("B팀이 이겼습니다. 배틀을 종료합니다.")
        break
    if len(B)==0:
        print("A팀이 이겼습니다. 배틀을 종료합니다.")
        break
    attack(A,B)
    check(A)
    check(B)
    showTeams(A,B,"A","B")

