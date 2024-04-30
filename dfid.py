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
   
def DFID(graph, start_node, goal_node):
    depth = 0

    while True:
        visited = set()
        path = []
        open_list = []
        closed_list = []
        iteration = 0
        #print(f"Depth Limit: {depth}")
        if dls(graph, start_node, goal_node, visited, open_list, closed_list, path, iteration, depth):
            print("Goal found at dept limit ", depth)
            print(' -> '.join(map(str, path)))
            return True
        depth += 1

if __name__ == "__main__":
    graph = {
        1: [2,4],
        2: [1,6,7],
        4: [9],
        6: [2],
        7: [2],
        9: [4],
    }
    start_node = 1
    goal_node = 9
    path = []
    iteration = 1
    DFID(graph, start_node, goal_node)
    
