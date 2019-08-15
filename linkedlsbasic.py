class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
e1=Node("mon")
e2=Node("Tue")
e3=Node("Wed")
e1.nextval=e2
e2.nextval=e3
temp=e1
while(temp.nextval!=None):
    print(temp.dataval)
    temp=temp.nextval
print(temp.dataval)
