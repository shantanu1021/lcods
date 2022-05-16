class Graph:
    def __init__(self,v,e):
        self.v=v
        self.e=e
        self.adjlist=[[] for _ in range(v+1)]

    def input(self):
        for i in range(self.e):
            print("Enter details of edge ",i+1)
            print("Enter source vertex:")
            src=int(input())
            print("Enter destination vertex:")
            dst=int(input())
            self.adjlist[src].append(dst)
            self.adjlist[dst].append(src)

    def print(self):
        for i in range(1,self.v+1):
            print(i,end=" ")
            print(self.adjlist[i])        

    def BFS(self,queue,visited):
        if(len(queue)==0):
            return
        
        src=queue[0]
        print(queue.pop(0),end=" ")
        for i in self.adjlist[src]:
            if visited[i]==False:
                visited[i]=True
                queue.append(i)

        self.BFS(queue,visited)

    def DFS(self,start,visited):
        visited[start]=True
        print(start,end=" ")
        for i in self.adjlist[start]:
            if visited[i]==False:
                visited[i]=True
                self.DFS(i,visited)

    def CallBFS(self,start):
        queue=[]
        visited=[False]*(self.v+1)
        queue.append(start)
        visited[start]=True
        self.BFS(queue,visited)

    def CallDFS(self,start):
        visited=[False]*(self.v+1)
        self.DFS(start,visited)


def menu():
    flag=True
    while(flag):
        v=int(input("How many vertices: "))
        e=int(input("How many edges: "))
        g=Graph(v,e)
        g.input()
        
        start=int(input("BFS : Enter the vertex to start: "))
        g.CallBFS(start)
        print()
        start=int(input("DFS : Enter the vertex to start: "))
        g.CallDFS(start)
        print()
        print("Do you want to continue?(1/0)")
        cont=int(input())
        if(cont==0):
            flag=False   

menu()