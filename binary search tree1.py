q=[]
while q:
    a=q.pop(0)
    print(a.data)
    if a.left:
        q.append(a.left)
    if a.right:
        q.append(a.right)
