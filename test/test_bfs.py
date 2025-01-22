# write tests for bfs
import pytest
from search import graph
import networkx as nx

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    g = graph.Graph('data/tiny_network.adjlist')

    total_nodes = len(g.graph)

    test = g.bfs("Michael McManus")
    check = list(nx.bfs_tree(g.graph, source = "Michael McManus").nodes())
    assert test == check #check that bfs traversal written in graph.py returns the same list and order of nodes as built-in bfs function in network x package does

    test2 = g.bfs("32790644")
    check2 = list(nx.bfs_tree(g.graph, source="32790644").nodes())
    assert test2 == check2

    assert len(test) == total_nodes #check that all nodes in the graph are being traversed

    #test instance edge cases
    with pytest.raises(ValueError): #start node not in the graph
        g.bfs("King Julian")

    with pytest.raises(ValueError): #no start node provided
        g.bfs("")



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
    g = graph.Graph('data/citation_network.adjlist')
    test = g.bfs("Joseph DeRisi", "Rima Arnaout")
    check = nx.shortest_path(g.graph, source="Joseph DeRisi", target = "Rima Arnaout")
    assert test == check  #check that bfs traversal written in graph.py returns the same list and order of nodes as built-in bfs function in network x package does for given start and end node

    test2 = g.bfs("Atul Butte", "Franklin Huang")
    check2 = nx.shortest_path(g.graph, source="Atul Butte", target = "Franklin Huang")
    assert test2 == check2 #check that bfs traversal written in graph.py returns the same list and order of nodes as built-in bfs function in network x package does for given start and end node

    #test edge cases
    no_path = g.bfs("34914736", "Franklin Huang")
    assert no_path is None #where no path exists between two nodes

    with pytest.raises(ValueError):
        g.bfs("Tony Capra", "Kowalski")



