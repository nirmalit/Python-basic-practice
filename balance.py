bal=1000
sums=0
first=''
st=str(input("enter the string"))
ls=list(st)
first=ls[0]
ls.pop(0)
z=len(ls)
j=z-1
for k in range(0,z):
    ls[k]=int(ls[k])
for x in ls:
    sums+=x*(10**j)
    j=j-1
if first=='w':
    result=bal-sums
    
else:
    result=bal+sums
print("your balance is",result)
    
