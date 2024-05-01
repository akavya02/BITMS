'''def fun(n):
    if n==0:
        return 1
    else:
        return (n*fun(n-1))
print(fun(5))'''

n=int(input())
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(n))