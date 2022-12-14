from collections import deque

graph = {
    1: [3, 4],
    2: [3, 4, 5],
    3: [1, 5],
    4: [1],
    5: [2, 6],
    6: [3, 5],
}
root_node = 1


def bfs(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue.extend(list(set(graph[n]) - set(visited)))
    return visited


print(bfs(graph, root_node))
