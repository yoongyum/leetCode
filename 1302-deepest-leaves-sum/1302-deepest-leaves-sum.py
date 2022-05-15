import queue
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        #short python BFS level order traversal
        pre,cur=[],[root]
        while cur:
            pre,cur=cur,[child for node in cur for child in [node.left,node.right] if child]
        return sum(node.val for node in pre)
        