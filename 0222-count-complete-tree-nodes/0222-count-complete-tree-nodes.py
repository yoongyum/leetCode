# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import math
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_levels =1;
        l = root.left
        while l:
            l = l.left
            left_levels+=1;
        right_levels=1;
        r = root.right
        while r:
            r = r.right
            right_levels+=1
        if(left_levels==right_levels):
            return int(math.pow(2, left_levels)-1)
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
        