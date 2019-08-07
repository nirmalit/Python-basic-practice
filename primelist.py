n=int(input("enter the number"))
def p(n):
    j=0
    for i in range(1,n+1):
        if n%i==0:
            j=j+1
    if j==2:
        print(n)
for i in range(n+1):
    p(i)