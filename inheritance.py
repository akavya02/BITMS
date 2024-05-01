'''class a:
    def fun(self):
        print("fun1")
    def fun(self):
        print("fun2")
class b:
    def __init__(self)-> None:
        print("1")
    def __init__(self)-> None:
        print("2")
    def fun(self):
        print("fun3")
    def fun(self):
        print("fun4")
a.fun()'''

class ab:
    branch="cse"
    def __init__(self,a)->None:
        ab.x=10
        self.a=a
    def fun(self):
        print("fun1",self.branch,self.x)
        print("fun1",ab.branch,ab.x)
o=ab(10)
o.fun()
