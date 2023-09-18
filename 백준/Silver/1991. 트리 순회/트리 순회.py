from collections import defaultdict
import queue


n = int(input())

tree = defaultdict(list)

for _ in range(n):
    root, left, right = input().split()
    if tree[root]:
        tree[root][0] += [left]
        tree[root][1] += [right]
    else:
        tree[root] = [left, right]

def preorder(visit):

    if visit == '.':
        return ''
    
    else:
        return visit + preorder(tree[visit][0]) + preorder(tree[visit][1]) 

def inorder(visit):

    if visit == '.':
        return ''
    
    else:
        return inorder(tree[visit][0]) + visit + inorder(tree[visit][1]) 

def postorder(visit):

    if visit == '.':
        return ''
    
    else:
        return postorder(tree[visit][0]) + postorder(tree[visit][1]) + visit
   
print(preorder('A'))
print(inorder('A'))
print(postorder('A'))
