def dfs(graph, curr_node, goal_node, visited, open_list, closed_list, path, iteration):
    visited.add(curr_node)
    path.append(curr_node)
    open_list.append(curr_node)

    print(f"Iteration {iteration}:")
    print("Open list:", open_list)
    print("Closed list:", closed_list)
    #print("Current path:", path)

    if curr_node == goal_node:
        return True
    
    for node in graph[curr_node]:
        if node not in visited and node not in closed_list:
            if dfs(graph, node, goal_node, visited, open_list, closed_list, path, iteration + 1):
                return True
            
    open_list.remove(curr_node)
    closed_list.append(curr_node)
    return False

if __name__ == "__main__":
    graph = {
        0: [1, 2, 3],
        1: [0],
        2: [0, 4],
        3: [0],
        4: [2]
    }
    start_node = 0
    goal_node = 4
    visited = set()
    open_list = []
    closed_list = []
    path = []
    iteration = 1
    dfs(graph, start_node, goal_node, visited, open_list, closed_list, path, iteration)
    #print("Final path:", end= " ")
    print("Path from", start_node, "to", goal_node, ":", ' -> '.join(map(str, path)))
