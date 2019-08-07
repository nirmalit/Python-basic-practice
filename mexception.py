a=1
b=0
ls=[1,2,3]
try:
    d=a/b
except ArithmeticError:
    print("arithmetic error occured")
try:
    ls[3]=8
except IndexError:
    print("list reached maximum limit")