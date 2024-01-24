# write tests for bfs
import pytest
from search.graph import Graph
import networkx as nx

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    tiny_network = Graph("data/tiny_network.adjlist")
    start = "Luke Gilbert"
    bfs_result = tiny_network.bfs(start)
    truth = list(nx.bfs_tree(tiny_network.graph, source = start))
    # test that all nodes are visited only once
    assert len(bfs_result) == 30
    assert len(set(bfs_result)) == 30
    # check transversal vs the networkx package
    assert bfs_result == truth

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    pass
