# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def traverse(root,arr):
            
            if(root):
                traverse(root.left,arr)
                arr.append(root.val)
                traverse(root.right,arr)
        
        l1 = []
        l2 = []
        traverse(root1,l1)
        traverse(root2,l2)
        ans = []
        
        # print(l1,l2)
        index1,index2 = 0,0
        
        while(index1<len(l1) and index2<len(l2)):
            if(l1[index1]<l2[index2]):
                ans += [l1[index1]]
                index1 += 1
            
            else:
                ans += [l2[index2]]
                index2 += 1
            
        
        
        return ans + l1[index1:] + l2[index2:]
        
        # return(sorted(l1+l2))
            