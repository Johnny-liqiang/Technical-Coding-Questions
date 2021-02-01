# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
        
class Solution(object):
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        """
        :type root: TreeNode
        :rtype: float
        """
        # reclusive value of current root value
        self.res = 0
        
        def dfs(root):
            if not root: return [0, 0.0]
            n1, s1 = dfs(root.left)
            n2, s2 = dfs(root.right)
            n = n1 + n2 + 1
            s = s1 + s2 + root.val
            self.res = max(self.res, s / n) 
            # make sure in python3 In Python2, s / n is Integer Division, while in Python3, '/' is floating point division.
            
            return [n, s]   # num and sum
        dfs(root)
        
        return self.res
    
#Time complexity : O(N), where N is the number of nodes in the tree. This is because we visit each and every node only once, as we do in postorder traversal.

# Space complexity : O(N), because we will create N states for each of the nodes in the tree.


'''
class Solution(object):
    def SubtreewithMaxAvg(self, root):
        self.targetNode, self.average=None, 0
        self.helper(root)
        return self.targetNode
    
    def helper(self, root):
        #initial 
        if root is None:
            return 0，0
        #divide
        leftSum,leftSize=self.helper(root.left)
        rightSum,rightsize=self.helper(root.right)
        
        #conquer
        sum=leftSum+rightSum+root.val
        size=leftsize+rightsize+1
        average=sum*1.0/size
        
        
        #Gloabl Comparison and final the maximum node
        if self.targetNode is None or self.average < average:
            self.targetNode =root
            self.average =average
            
        return sum, size
        
'''    
    
