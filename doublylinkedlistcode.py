'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.prev=None
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            self.tail.next=new
            new.prev=self.tail
            self.tail=new
    def printing(self):
        i=self.head
        while i:
            print(i.data)
            i=i.next
l=[1,2,3,4,5]
o=dll()
for i in l:
    o.insertatend(i)
o.printing()'''



'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.prev=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
    def printing(self):
        i=self.head
        while i:
            print(i.data)
            i=i.next
l=[1,2,3,4,5]
o=dll()
for i in l:
    o.insertatbeg(i)
o.printing()'''


'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.prev=None
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            self.tail.next=new
            new.prev=self.tail
            self.tail=new
    def printing(self):
        i=self.head
        while i:
            print(i.data)
            i=i.next
    def reverse(self):
        curr=self.head
        while curr:
            if curr.next==None:
                self.head=curr
            curr.next,curr.prev=curr.prev,curr.next
            curr=curr.prev       
l=[1,2,3,4,5]
o=dll()
for i in l:
    o.insertatend(i)
o.printing()
o.reverse()
o.printing()'''

    
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class cll:
    def __init__(self):
        self.head=None
        self.tail=None
    '''def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            self.tail.next=new
            new.prev=self.tail
            self.tail=new'''
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
        self.tail.next=self.head
        self.head.prev=self.tail
    def printing(self):
        i=self.head
        while i:
            print(i.data)
            i=i.next
    '''def reverse(self):
        curr=self.head
        while curr:
            if curr.next==None:
                self.head=curr
            curr.next,curr.prev=curr.prev,curr.next
            curr=curr.prev  '''     
l=[1,2,3,4,5]
o=cll()
for i in l:
    o.insertatbeg(i)
o.printing()

