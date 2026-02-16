# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def inOrder(root):
            if root is None:
                return
            
            # 1. Traverse the left subtree
            inOrder(root.left)
            # 2. Visit the node (append to our list instead of printing)
            result.append(root.val)
            # 3. Traverse the right subtree
            inOrder(root.right)
            
        inOrder(root)
        return result
    