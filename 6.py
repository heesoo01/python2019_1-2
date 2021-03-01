hg=int(input("높이: "))
for i in range(1,hg+1,1):
    if(i%2==1):
        print("▲"*i,end="")
        print(":",i)
    else:
        print("△"*i,end="")
        print(":",i)
    
