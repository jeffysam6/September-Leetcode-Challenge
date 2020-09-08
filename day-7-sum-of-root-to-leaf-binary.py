# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        from collections import deque
        ans = []
        d = deque([(root,'')])
        
        if(root is None):
            return 0
        
        while(d):
            
            p = d.popleft()
            # print(p[0].left)

            if(p[0].left):
                d.append((p[0].left,p[1]+str(p[0].val)))
            
            if(p[0].right):
                d.append((p[0].right,p[1]+str(p[0].val)))
            
            if(p[0].left is p[0].right is None):
                ans.append(int(p[1]+str(p[0].val),2))
        
        return(sum(ans))