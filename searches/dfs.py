# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 11:27:34 2023

@author: exam2
"""

from collections import defaultdict 

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def goalState(self,r,e):
        if(r==e):
            print('Element found')
            return True
    
    def DFS(self,r,e,l):
        visited=[False]*(l)
        stack=[]
        
        stack.append(r)
        
        while(len(stack)):
            r=stack.pop(-1)
            print(r,end=" ")
            
            if self.goalState(r,e):
                return 
            
            for i in self.graph[r]:
                if visited[i]==False:
                    stack.append(i)
                    visited[i]=True
        
        print('element not found')
        return

# graph

g = Graph()

g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(3,6)
g.addEdge(3,7)

r=int(input('Enter root node='))
e=int(input('Enter element to search='))
l=int(input('Enter length of graph='))

g.DFS(r,e,l)
