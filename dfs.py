

graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
}


def DFSCall(graph , Start):
    vis = []
    dfs(graph , Start, vis)


def dfs(graph, a, vis):
    
        vis.append(a)
        print(a , end = " ")
        for i in graph[a]:
            if i not in vis:
                dfs(graph , i , vis)
                
                
        
        
                        
                
                
         
         
         
print("Depth First Search Result : ")           
DFSCall(graph , 'A')
    
    
    
    
