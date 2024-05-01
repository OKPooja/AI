from queue import PriorityQueue

def aStar(graph, curr_node, goal_node, visited, open_list, closed_list, heuristic, cost):
    open_list.add(curr_node)
    q = PriorityQueue()
    q.put((0, 0, curr_node))
    parent = {}
    parent[1] = 0
    distance = {node: float('inf') for node in heuristic}
    distance[curr_node] = 0

    while not q.empty():
        
        total_cost, path_cost, top = q.get()
        if top in open_list:
            open_list.remove(top)
        closed_list.add(top)
        print(f'Current node: {top}')
        print(f'Path cost: {path_cost}')
        print(f'Total cost : {total_cost}')
        print("Open list:", open_list)
        print("Closed list:", closed_list)
        print()
        if top == goal_node:
            print(distance)
            return parent
            return
        
        for node in graph[top]:
            
            open_list.add(node)
            parent[node] = top
            if(top > node):
                c = cost[(node, top)]
            else: 
                c = cost[(top, node)]
                
            h = heuristic[node]
            new_distance = path_cost + c + h
            if(new_distance < distance[node]) : 
                q.put((path_cost + c + h, path_cost + c, node))
                distance[node] = new_distance
    
if __name__ == "__main__":


    graph = {
    0: [1, 2],
    1: [2, 3, 4],
    2: [3],
    3: [4],
    }
    heuristic = {
        0: 7,
        1: 6,
        2: 2,
        3: 1,
        4: 0,
    }
    cost = {
        (0, 1): 1,
        (0, 2): 4,
        (1, 2): 2,
        (1, 3): 5,
        (1, 4): 12, 
        (2, 3): 2,
        (3, 4): 3,
    }
    start_node = 0
    goal_node = 4
    visited = set()
    open_list = set()
    closed_list = set()
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
