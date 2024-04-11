def pairs(grid):
    n = len(grid)
    pair = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if grid[i][k] != grid[k][j]:
                    break
            else:
                pair += 1
    return pair
