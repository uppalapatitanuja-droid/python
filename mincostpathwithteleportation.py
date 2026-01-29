class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])
        dp  = [[inf]*(n) for _ in range(m)]; dp[-1][-1] = 0
        for t in range(k+1):
            if (t > 0) and (prev:= inf):
                for i,j in sorted(product(range(m),range(n)), \
                           key=lambda x: (grid[x[0]][x[1]], dp[x[0]][x[1]])):
                    prev= dp[i][j] = min(dp[i][j], prev)
            for i,j in product(range(m-1,-1,-1), range(n-1,-1,-1)):
                if i<m-1: dp[i][j] = min(dp[i][j], dp[i+1][j]+grid[i+1][j])
                if j<n-1: dp[i][j] = min(dp[i][j], dp[i][j+1]+grid[i][j+1])
        return dp[0][0]
        
