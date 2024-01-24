import networkx as nx

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
        # check for errors
        if not self.graph:
            raise ValueError("graph is empty")
        if not start or start not in self.graph:
            raise ValueError("invalid start")
        if end and end not in self.graph:
            raise ValueError("invalid end")

        # transverse the graph
        # setup the queue
        visited = []
        q = []
        paths = {}
        # start
        q.append(start)
        paths[start] = [start]

        while not len(q) == 0:
            current_node = q.pop(0)
            visited.append(current_node)
            
            if current_node == end:
                return paths[current_node]
            for successor in self.graph.neighbors(current_node):
                if successor not in visited and successor not in q:
                    q.append(successor)
                    paths[successor] = paths[current_node] + [successor]
        
        # end is not accessable from start
        if end:
            return None
        
        # end is none, returning nodes transversed
        return visited




