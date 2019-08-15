c=0
class node:
    def  __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def iatbegin(self,value):
        newnode=node(value)
        newnode.next=self.head
        self.head=newnode
def getv():
    print('1.inert value 2.insert value at any position 3.insert at end 4.delete at begining 5.delete at end 6.delete at any position 7.display 8.exit')
    
ll=sll()
c=1
while(c!=8):
    if(c==7):
        temp=ll.head
        while(temp.next!=None):
            temp=temp.next
            print(temp.data)
    elif(c==1):
        a=int(input("enter the value to be inserted "))
        ll.iatbegin(a)
    
    elif(c==2):
        i=1
        val=input('enter the value to be iserted ')
        a=int(input('enter the node position for inserting '))
        temp=ll.head
        while(i<a):
            temp=temp.next
            i=i+1
        newnode=node(val)
        newnode.next=temp.next
        temp.next=newnode
        
    elif(c==3):
        temp=ll.head
        while(temp.next!= None):
            temp=temp.next
        a=int(input('enter the value to be inserted '))
        newnode=node(a)
        temp.next=newnode
        
    elif(c==4):
        temp=ll.head
        ll.head=ll.head.next
        temp.data=None
        
    elif(c==5):
        temp=ll.head
        temp1=temp.next
        while(temp1.next!=None):
            temp=temp.next
            temp1=temp.next
        temp.next=None
        temp1=None
        
    elif(c==6):
        a=int(input('enter the position you want to delete '))
        i=0
        temp=ll.head
        while(i<a):
            temp=temp.next #node before deleting node
            temp1=temp.next
            temp2=temp1.next #node after deleting node
        temp.next=temp2
        temp1.data=None
        
    elif(c==7):
        temp=ll.head
        while(temp.next==None):
            print(temp.data)
            temp=temp.next
        print(temp.data)    
    getv()
    c=int(input('enter the choice'))
        
        
            
            
            
        
