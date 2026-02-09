class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        ln = 0

        def dfs(node):
            if node.left : dfs(node.left)
            nonlocal arr,ln
            ln += 1
            arr.append(node.val)
            if node.right : dfs(node.right)
            return

        dfs(root)

        def createBST(l,r):
            if r < l or l > r : return None
            mid = (l+r)//2
            node = TreeNode(val=arr[mid])

            node.left = createBST(l,mid-1)
            node.right = createBST(mid+1,r)

            return node

        return createBST(0,ln-1)
