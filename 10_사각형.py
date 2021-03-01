#_사각형

    
a=int(input("한변의 길이:"))
i=a*a
while(i>a*a-a):
    print("%c %c %c %c"%(64+i,64+i-a,64+i-a*2,64+i-a*3))
    i-=1

    
