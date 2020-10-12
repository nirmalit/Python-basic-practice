def move(f,t):
    print("move disk from {} to {}".format(f,t))
def hanoi(n,f,t,h):
    if n==1:
        return move(f,t)
    hanoi(n-1,f,h,t)
    move(f,t)
    hanoi(n-1,h,t,f)
hanoi(3,"A","c","b")
