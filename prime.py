j=0
n=int(input("enter the number"))
for i in range(1,n+1):
    if n%i==0:
        j=j+1
if j==2:
    print("it is prime")
else:
    print("it is not a prime")
