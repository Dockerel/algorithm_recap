graph = {
    1: [3, 4],
    2: [3, 4, 5],
    3: [1, 5],
    4: [1],
    5: [2, 6],
    6: [3, 5],
}
root_node = 1

visited = []
start = root_node


def dfs(start):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs(node)
    return


dfs(start)
print(visited)
