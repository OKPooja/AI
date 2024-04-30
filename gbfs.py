from queue import PriorityQueue

def gbfs(graph, curr_node, goal_node, visited, open_list, closed_list, path, cost):
    visited.add(curr_node)
    q = PriorityQueue()
    q.put((0, curr_node))
    open_list.append(curr_node)
    iteration = 0
    while not q.empty():

        print(f"Iteration {iteration}:")
        print("Open list:", open_list)
        print("Closed list:", closed_list)

        _, top = q.get()
        open_list.remove(top)
        closed_list.append(top)
        path.append(top)

        if top == goal_node:
            break
        for node in graph[top]:
            if node not in visited:
                c = cost[(top, node)]
                q.put((c, node))
                visited.add(node)
                open_list.append(node)
                if node == goal_node:
                    path.append(goal_node)
                    return
        iteration += 1
        

if __name__ == "__main__":
    graph = {
        1: [2, 4],
        2: [1, 6, 7],
        4: [9],
        6: [2],
        7: [2],
        9: [4],
    }
    cost = {
        (1, 2): 4,
        (1, 4): 1,
        (2, 6): 2,
        (2, 7): 1,
        (4, 9): 2,
    }
    start_node = 1
    goal_node = 7
    visited = set()
    open_list = []
    closed_list = []
    path = []
    iteration = 1
    gbfs(graph, start_node, goal_node, visited, open_list, closed_list, path, cost)
    print(' -> '.join(map(str,path)))
