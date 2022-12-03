graph = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "1", "0"],
    ["0", "0", "0", "1", "1"],
]

row = len(graph)
column = len(graph[0])
visited = [[0] * column for i in range(row)]
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

queue = []
island = 0

for i in range(row):
    for j in range(column):
        # 방문한 상태면 다음 loop으로...
        if visited[i][j] == 1:
            continue

        visited[i][j] = 1

        if graph[i][j] == "1":
            queue.append([i, j])
            while queue:
                x, y = queue.pop(0)
                for d in directions:
                    temp_x, temp_y = x + d[0], y + d[1]
                    if temp_x < 0 or temp_x >= row or temp_y < 0 or temp_y >= column:
                        continue
                    if graph[temp_x][temp_y] == "0" or visited[temp_x][temp_y] == 1:
                        continue
                    visited[temp_x][temp_y] = 1
                    queue.append([temp_x, temp_y])
            island += 1
print(island)
