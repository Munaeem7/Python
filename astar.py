import heapq

graph = {
    'Home': [('A', 4), ('B', 2)],
    'A': [('C', 3)],
    'B': [('C', 1)],
    'C': [('Office', 4)],
    'Office': []
}

heuristic = {
    'Home': 7,
    'A': 2,
    'B': 10,
    'C': 0,
    'Office': 0
}

def aStar(graph , start , goal , heuristic):
    queue = [(0 + heuristic[start] , 0 , start , [])]
    visited = set()
    
    while queue:
        f, g , node , path = heapq.heappop(queue)
        
        if node in visited:
            continue
        
        visited.add(node)
        path = path + [node]
        
        if node == goal:
            return g , path
        
        for neighbour,curr_cost in graph[node]:
            if neighbour not in visited:
                g_new = g + curr_cost
                f_new = f + heuristic[neighbour]
                heapq.heappush(queue , (f_new , g_new , neighbour , path))
                
    return float("inf") , []



result = aStar(graph , 'Home' , 'Office' , heuristic)

cost , path = result

if path:
    print("Cost" , cost)
    print("Shortest path " ,"->".join(path))
else:
    print("no")
    
        
         
