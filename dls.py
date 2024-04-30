def dls(graph, curr_node, goal_node, visited, open_list, closed_list, path, iteration, depth_limit):
    
    visited.add(curr_node)
    path.append(curr_node)
    open_list.append(curr_node)

    if depth_limit == 0:
        if goal_node != curr_node:
            return False
        return True

    print(f"Iteration {iteration}:")
    print("Open list:", open_list)
    print("Closed list:", closed_list)
    # print("Current path:", path)

    if curr_node == goal_node:
        return True
    
    for node in graph[curr_node]:
        if node not in visited and node not in closed_list:
            if dls(graph, node, goal_node, visited, open_list, closed_list, path, iteration + 1, depth_limit - 1):
                return True
            
    open_list.remove(curr_node)
    closed_list.append(curr_node)
    return False

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'G'],
        'C': ['A'],
        'D': ['B','F'],
        'G': ['B']
    }
    start_node = 'A'
    goal_node = 'C'
    depth_limit = 1
    visited = set()
    open_list = []
    closed_list = []
    path = []
    iteration = 1

    if dls(graph, start_node, goal_node, visited, open_list, closed_list, path, iteration, depth_limit):
        print("Path from", start_node, "to", goal_node, ":", ' -> '.join(path))
    else:
        print("Path not found at the given depth level")
