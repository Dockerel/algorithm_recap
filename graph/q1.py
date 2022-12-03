def numIslands(grid):
    row = len(grid)
    column = len(grid[0])
    visited = [[0] * column for i in range(row)]
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    island = 0

    queue = []

    for i in range(row):
        for j in range(column):
            # 방문 체크. 방문했으면 다음 loop로...
            if visited[i][j] == 1:
                continue
            visited[i][j] = 1

            if grid[i][j] == "1":
                queue.append([i, j])
                island += 1
                while queue:
                    x, y = queue.pop(0)
                    for d in directions:
                        temp_x = x + d[0]
                        temp_y = y + d[1]
                        if temp_x < 0 or temp_x >= row or temp_y < 0 or temp_y >= column:
                            continue
                        if grid[temp_x][temp_y] == "0" or visited[temp_x][temp_y] == 1:
                            continue
                        visited[temp_x][temp_y] = 1
                        queue.append([temp_x, temp_y])
    return island


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

print(numIslands(grid))
