class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        small, large = min(p.val, q.val), max(p.val, q.val)
        while root:
            if root.val < small:
                root = root.right
            elif root.val > large:
                root = root.left
            else:
                return root
        return None
        