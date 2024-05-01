'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=node(1)
a.next=node(2)
a.next.next=node(3)
print(a,a.data,a.next)
print(a.next,a.next.data,a.next.next)
print(a.next.next,a.next.next.data,a.next.next.next)
a=node(1)
b=node(2)
c=node(3)
a.next=b
b.next=c
print(a,a.data,a.next)
print(b,b.data,b.next)
print(c,c.data,c.next)'''



'''class node:       #frontinsert
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self)->None:
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(1)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def printing(self):
        if self.head==None:
            return
        i=self.head
        while i:
            print(i.data)
            i=i.next
    def reverse(self):
        curr=self.head
        prev=None
        nxt=self.head.next
        while curr:
            curr.next=prev
            prev=curr
            curr=nxt
            if nxt:
                nxt=nxt.next
        self.head=prev
l=[1,2,3,4,5]
o=sll()
for i in l:
    o.insertatbeg(i)
o.printing()
o.reverse()
o.printing()'''


                 #endinsert
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self)->None:
        self.head=None
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            i=self.head
            while i.next:
                i=i.next
            i.next=new
    def printing(self):
        if self.head==None:
            return
        i=self.head
        while i:
            print(i.data)
            i=i.next
    def delatbeg(self):
        self.head=self.head.next
        self.head.prev=None
    def delatend(self):
        i=self.head
        while i.next.next:
            i=i.next
        i.next=None
    '''def length(self):
        count=0
        i=self.head
        while i:
            count+=1
            i=i.next
        return count'''
l=[1,2,3,4,5]
o=sll()
for i in l:
    o.insertatend(i)
o.printing()
o.delatbeg()
o.delatend()
o.printing()
o.printing()