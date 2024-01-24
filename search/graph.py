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

        # transverse the graph
        visited = []
        q = []
        q.append((start, None))

        while not q.empty():
            current_node = q.pop(0)
            if current_node[0] == end:
                return [current_node[0]].append(end[1])
            for successor in self.graph.successors(current_node):
                if successor not in visited:
                    q.append((successor, [current_node[0]].append(current_node[1])))
        
        # end is not accessable from start
        if end:
            return None
        
        # end is none, returning nodes transversed
        return visited




