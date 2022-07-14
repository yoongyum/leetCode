class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0: return None
        if len(preorder) == 1: return TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        return TreeNode(val = preorder[0], 
                        left = self.buildTree(preorder[1:i+1], inorder[:i]), 
                        right = self.buildTree(preorder[i+1:], inorder[i+1:]))
        