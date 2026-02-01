from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = set()
        rpt = -1

        
        for i in range(n):
            for j in range(n):
                if grid[i][j] in seen:
                    rpt = grid[i][j]
                else:
                    seen.add(grid[i][j])

        
        miss = -1
        for num in range(1, n*n + 1):
            if num not in seen:
                miss = num
                break

        return [rpt, miss]
