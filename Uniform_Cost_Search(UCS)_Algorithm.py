import heapq

graph = {
    'A':[('B' ,1),('C',2)],
    'B':[('D' , 3)],
    'C':[('D',4)],
    'D':[('E',5)],
    'E':[]
}


def ucs(graph , start , goal):
    queue = [(0 , start , [])]
    vis = set()
    

    while queue:
        cost , node , path = heapq.heappop(queue)
        
        if node in vis:
            continue
        
        vis.add(node)
        path = path +[node]
        
        if (node == goal):
            return cost , path
        
        for neighbour, curr_cost in graph[node]:
            if neighbour not in vis:
                heapq.heappush(queue , (cost + curr_cost ,neighbour , path ))
                
    return float("inf"),[]


result = ucs(graph, 'A' , 'E')
cost , path = result
if path:
    print("Shortest Path: ","->".join(path))
    print("Cost: ",cost)
else:
    print("No path found")