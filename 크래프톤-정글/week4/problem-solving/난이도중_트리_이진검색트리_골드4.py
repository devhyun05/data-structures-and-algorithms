# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.value = value 
#         self.left = left 
#         self.right = right 

# def insert(root, new_node):
#     if not root: 
#         return TreeNode(new_node)

#     if root.value > new_node: 
#         root.left = insert(root.left, new_node)
#     else:
#         root.right = insert(root.right, new_node)
    
#     return root 

# root = TreeNode(tree_nodes[0])

# for node in tree_nodes[1:]:
#     insert(root, node)

# post_order_traversal(root)

# [50,30,24,5,28,45,98,52,60]

# left = [30,24,5,28,45], right = [98,52,60]

# import sys
# sys.setrecursionlimit(10**6)

preorder = [50,30,24,5,28,45,98,52,60]

# for line in sys.stdin: 
#     preorder.append(int(line))
    
def solve(start, end):
    if start > end: 
        return 

    root = preorder[start]

    mid = end + 1 

    for i in range(start+1, end+1):
        if preorder[i] > root: 
            mid = i 
            break 
    
    solve(start+1, mid-1)
    solve(mid, end)
    print(root)

solve(0, len(preorder)-1)




