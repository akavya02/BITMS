'''class cse:
    def __init__(self,name,rollno):
        self.n=name
        self.ron=rollno
    def fun(s):
        print(s.n,s.rn)
s1=cse('rahul',34)
s2=cse('raghu',36)
s1.fun()
s2.fun()
print(s1.n,s2.n)'''
import math
class circle:
    def __init__(self,radius):
        self.r=radius
    def printing(self):
        print(math.pi*self.r*self.r)
class rectangle:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def printing(self):
        print(self.l*self.b)
l=float(input())
b=float(input())
r=float(input())
o=circle(r)
o.printing()
o1=rectangle(l,b)
o1.printing()
