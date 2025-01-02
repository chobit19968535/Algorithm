# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:10:37 2024

@author: Lycoris
"""

class treeNode:
    def __init__(self, val):
         # 初始化節點
         self.val = val
         self.left = None
         self.right = None

    def insertLeft(self, val):
         # 如果要新增左邊節點，先檢查是否已存在，若左節點不存在則放入左節點
         if self.left == None:
             self.left = treeNode(val)
         # 如果左節點已經存在，則放入左節點的下一層左節點，這邊用遞迴的方式進行搜尋，直到可以讓入左節點為止
         else:
             self.left.insertLeft(val)
    def insertRight(self, val):
        # 新增右邊節點的方式則和新增左節點的方式相同
        if self.right == None:
            self.right = treeNode(val)
        else:
            self.right.insertRight(val)

# 執行方式
sampleTree = treeNode(5)
sampleTree.insertRight(7)
sampleTree.insertRight(8)
sampleTree.insertLeft(3)
sampleTree.insertLeft(2)
sampleTree.right.insertLeft(6)
sampleTree.left.insertRight(4)
sampleTree.right.right.insertLeft(20)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    if root is None:
        return
    print(root.val, end=" ")  # 先訪問根節點
    preorderTraversal(root.left)  # 遞歸訪問左子樹
    preorderTraversal(root.right)  # 遞歸訪問右子樹
    
def inorderTraversal(root):
    if root is None:
        return

    inorderTraversal(root.left)  # 遞歸訪問左子樹
    print(root.val, end=" ")  # 訪問根節點
    inorderTraversal(root.right)  # 遞歸訪問右子樹
    
def postorderTraversal(root):
    if root is None:
        return

    postorderTraversal(root.left)  # 遞歸訪問左子樹
    postorderTraversal(root.right)  # 遞歸訪問右子樹
    print(root.val, end=" ")  # 訪問根節點
    
# 建立一棵示例樹
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.right.left = TreeNode(5)
root.right.right = TreeNode(10)

# 進行先序遍歷
preorderTraversal(root)
print("\n")
inorderTraversal(root)
print("\n")
postorderTraversal(root)