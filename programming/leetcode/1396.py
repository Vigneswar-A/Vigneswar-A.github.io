class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid), len(grid[0])
        rows = [0]*m
        cols = [0]*n
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rows[i] += 1
                    cols[j] += 1
                
       

        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if rows[i] > 1 or cols[j] > 1:
                        count += 1
                        
        return count
        