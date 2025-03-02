from collections import deque

graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D': [],
    'E':['F'],
    'F':[]
}

def Bfs(graph , A):
    visited = []
    q = deque()
    q.append(A)
    visited.append(A)

    while q:
        curr = q.popleft()
        print(curr, end=" ")
        
        for i in graph[curr]:
            if(i not in visited):
                visited.append(i)
                q.append(i)
    
    

Bfs(graph , 'A')