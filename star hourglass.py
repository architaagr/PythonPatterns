#star hourglass

n = int(input("enter the no. of lines: "))
for i in range(n//2+2,1,-1):
    a = n//2-i+1
    print((a+1)*' '+(n//2-a)*('* '))
for j in range(2,i+n//2):
    b = i-j+n//2-1
    print(b*' '+(j*('* ')))
