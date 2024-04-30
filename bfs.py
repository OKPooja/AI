from queue import Queue

def bfs(graph, curr_node, goal_node, visited, open_list, closed_list, path):
    visited.add(curr_node)
    open_list.append(curr_node)
    path.append(curr_node)
       
    q = Queue()
    q.put(curr_node)
    iteration = 0
    while not q.empty():
        print(f"Iteration {iteration}:")
        print("Open list:", open_list)
        print("Closed list:", closed_list)

        top = q.get()
        closed_list.append(top)
        open_list.remove(top)
        
        for node in graph[top]:
            if node not in visited:
                if node == goal_node:
                    path.append(node)
                    return
                
                path.append(node)
                visited.add(node)
                q.put(node)
                open_list.append(node)
        
        iteration += 1

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
    goal_node = 7
    visited = set()
    open_list = []
    closed_list = []
    path = []
    iteration = 1
    bfs(graph, start_node, goal_node, visited, open_list, closed_list, path)
    print(' -> '.join(map(str, path)))
