l=[1,2,3,4,5]
def fun(l,ind):
    try:
        a=l.copy()
        a[0]=l[0]/l[ind]
    except ValueError:
        print("value error")
    finally:
        print("out of function")
try:
    fun(l,5) 
except IndexError:
    print("Index Error")
finally:
    print("end  of blocks")