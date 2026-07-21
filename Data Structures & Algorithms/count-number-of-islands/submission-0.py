class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    count += 1
                    q = deque([(r, c)])
                                        
                    while q:
                        row, col = q.popleft()
                        grid[row][col] = '0'

                        directions = [(1,0), (0,1), (-1,0), (0,-1)]

                        for dx, dy in directions:
                            new_row = dx + row
                            new_col = dy + col
                            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == '1':
                                q.append((new_row, new_col))
        return count

                        