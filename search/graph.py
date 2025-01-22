import networkx as nx
from queue import Queue

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G



        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """

        g = self.graph

        if not g:
            raise ValueError("Graph is empty") #error messages for edge cases
        if not start:
            raise ValueError("Needs a starting node")
        if start not in g:
            raise ValueError("Start node not in graph")
        if end and end not in g:
            raise ValueError("End node not in graph")

        q = Queue()
        visited = [] #initialize visited set

        q.put(start) #put start node into queue
        visited.append(start) #put start node into visited set
        paths = {start : [start]} #initialize paths dictionary to contain starting node and its path

        while not q.empty():
            current = q.get() #take the visited node off of the queue
            n = g.neighbors(current) #get the neighbors of the visited node

            if current == end:
                return paths[current]

            for neighbor in n:
                if neighbor not in visited:
                    q.put(neighbor) #put all neighbors not already visited into queue
                    visited.append(neighbor) #record the neighbors as visited if not already visited
                    paths[neighbor] = paths[current] + [neighbor] #create new dictionary entry for the path to the neighbor, which is path to current node + the neighbor
        if end:
            return None #if there was an end node given, but the BFS did not find path with end node, end node cannot be reached from start node

        return visited #return the list of nodes in the order they were traversed, or the order that they were added to visited set




