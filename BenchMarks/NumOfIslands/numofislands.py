# @param {character[][]} grid
# @return {integer}
def numIslands(grid):
    if not grid or not grid[0]:
        return 0

    numOfIslands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                numOfIslands += 1
                destoryIsland(grid, i, j)

    return numOfIsland

def destoryIsland(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
        return

    grid[i][j] = '0'
    destoryIsland(grid, i + 1, j)
    destoryIsland(grid, i - 1, j)
    destoryIsland(grid, i, j + 1)
    destoryIsland(grid, i, j - 1)
