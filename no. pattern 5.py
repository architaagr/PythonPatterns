#no. pattern 5
n = int(input("enter the no. of lines: "))
for i in range(n):
    for j in range(1,i+1):
        print((n-i)*' ',j+i,sep='',end='')
    print()
