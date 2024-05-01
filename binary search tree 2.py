class node:
    def __init__(self,data)->None:
        self.data=data
        self.left=None
        self.right=None
def bfs(root):
    q=[root]
    while q:
        a=q.pop(0)
        print(a.data)
        if a.left:
            q.append(a.left)
        if a.right:
            q.append(a.right)

def dfs_inorder(root):
    if root==None:
        return
    dfs_inorder(root.left)
    print(root.data)
    dfs_inorder(root.right)
def dfs_preorder(root):
    if root==None:
        return
    print(root.data)
    dfs_preorder(root.left)
    dfs_preorder(root.right)
def dfs_postorder(root):
    if root==None:
        return
    dfs_postorder(root.left)
    dfs_postorder(root.right)
    print(root.data)
root=node(4)
root.left=node(2)
root.right=node(6)
root.left.left=node(1)
root.left.right=node(3)
root.right.left=node(5)
dfs_inorder(root)
dfs_preorder(root)
dfs_postorder(root)
