'''l=[int(i) for i in input().split()]
print(l)'''
'''l=input().split()'''
'''for i in range(len(l)):
    l[i]=int(l[i])
print(l,type(l))'''
l=[2,3,4,5,6]
print(l.append(8))
print(l)
print(l.append([2,3,4]),l.extend([2,3,4]))
print(l)
l.insert(1,10)
print(l)