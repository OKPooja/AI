from queue import PriorityQueue

def aStar(graph, curr_node, goal_node, visited, open_list, closed_list, heuristic, cost):
    visited.add(curr_node)
    open_list.append(curr_node)
    q = PriorityQueue()
    q.put((0, 0, curr_node))
    parent = {}
    parent[1] = 0

    while not q.empty():
        
        total_cost, path_cost, top = q.get()
        open_list.remove(top)
        closed_list.append(top)
        print(f'Current node: {top}', end= " ")
        print(f'Path cost: {path_cost}')
        print("Open list:", open_list)
        print("Closed list:", closed_list)
        if top == goal_node:
            return parent
            return
        
        for node in graph[top]:
            if node not in visited:
                open_list.append(node)
                visited.add(node)
                parent[node] = top
                if(top > node):
                    c = cost[(node, top)]
                else: 
                    c = cost[(top, node)]
                 
                h = heuristic[node]
                q.put((path_cost + c + h, path_cost + c, node))
    
if __name__ == "__main__":
    graph = {
        1: [2, 3],
        2: [1, 5, 6],
        3: [1, 4, 5],
        4: [3, 5],
        5: [2,3,4,7],
        6: [2, 7],
        7: [5, 6]
    }
    heuristic = {
        1: 14,
        2: 12,
        3: 11,
        4: 6,
        5: 4,
        6: 11,
        7: 0
    }
    cost = {
        (1, 2): 4,
        (1, 3): 3,
        (2, 5): 12,
        (2, 6): 5,
        (3, 4): 7,
        (4, 5): 2,
        (3, 5): 10,
        (5, 7): 5,
        (6, 7): 16,
    }
    start_node = 1
    goal_node = 7
    visited = set()
    open_list = []
    closed_list = []
    parent = aStar(graph, start_node, goal_node, visited, open_list, closed_list,heuristic, cost)
    path = []
    path.append(goal_node)
    node = goal_node
    while True:
        next = parent[node]
        path.append(next)
        node = next
        if node == start_node:
            break

    path.reverse()
    print(f'Path from {start_node} to {goal_node} is', ' -> '.join(map(str, path)))
