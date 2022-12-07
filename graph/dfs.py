graph = {
    1: [3, 4],
    2: [3, 4, 5],
    3: [1, 5],
    4: [1],
    5: [2, 6],
    6: [3, 5],
}
root_node = 1


def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack.extend(graph[n])
    return visited


print(dfs(graph, root_node))
