#star of diamonds

r = input('run code y/n: ')
while r=='y':
    n = int(input("enter the no. of lines: "))
    for i in range(1,n//2+2):
        a = n//2-i+1
        print(a*' '+(i*('* ')))
    for j in range(i-1,0,-1):
        b = i-j
        print(b*' '+(j*('* ')))
