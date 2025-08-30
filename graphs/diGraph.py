import networkx as nx
import matplotlib.pyplot as plt
import pprint

import warnings
warnings.filterwarnings("ignore")


def draw_graph_with_nx(G):
    pos = nx.spring_layout(G, iterations=200)
    options = {'node_color': 'white', 'alpha': 1, 
               'node_size': 2000, 'width': 0.002, 'font_size': 25, 
               'arrows':True, 'edge_color': 'brown', 
               'arrowstyle': 'Fancy, head_length=1, head_width=1, tail_width=.4' }

    labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, pos, labels=labels, **options)
    plt.show()

class DiGraph:
    def __init__(self):
        self.g = {}

    def add_node(self, node):
        if node in self.g:
            raise ValueError("Node already in graph")
        
        self.g[node] = []

    def add_edge(self, src, dest):
        # sanity checks
        if src not in self.g :
            raise ValueError("Source node not exist in graph.")
        if dest not in self.g:
            raise ValueError("Destination node not exist in graph.")
        
        next = self.g[src]

        if dest in next:
            return
        next.append(dest)



    def draw_graph(self):
        G = nx.DiGraph()
        for src in self.g:
            G.add_node(src, label=src)
            for dest in self.g[src]:
                G.add_edge(src, dest)
        
        draw_graph_with_nx(G)

g = DiGraph()

nodes = ['a', 'b', 'c', 'd', 'e', 'f']

for n in nodes:
    g.add_node(n)


edges = [
    ('a', 'b'),
    ('a', 'c'),
    ('b', 'c'),
    ('b', 'd'),
    ('c', 'd'),
    ('d', 'c'),
    ('e', 'f'),
    ('f', 'c')
]

for e in edges:
    g.add_edge(e[0], e[1])


# print(g.g)

pprint.pprint(g.g)          # pretty printing!


# g.draw_graph()

##-------------------------------------------------------------------------------------------
#----------------------------------------------- Traverse Graph -----------------------------
##-------------------------------------------------------------------------------------------





def traverse_graph(self, start):
    """Traverse graph starting from given start node."""

    q = [start]
    visited = []

    while q:
        current = q.pop(0)

        # if we've already visited it, we can skip
        if current in visited:
            continue

        print(current)

        # if we're done with current
        visited.append(current)

        # get all directly connected nodes

        next_nodes = self.g[current]

        # traverse all the nexts
        for n in next_nodes:
            q.append(n)

DiGraph.traverse_graph = traverse_graph

# g.traverse_graph('a')

##-------------------------------------------------------------------------------------------
#----------------------------------------------- Find Path ----------------------------------
##-------------------------------------------------------------------------------------------




def find_path(self, start, end, path=[]):
    """Find path (not necessarily shortest) from start to end."""
    # sanity check 
    if start not in self.g:
        raise ValueError("Source node not in graph")
    
    # save the path we have traversed till now
    path = path + [start]

    # base case
    if start == end:
        return path
    
    # recursive case
    for node in self.g[start]:

        # need to avoid cycles
        if node not in path:

            # find path from next node to 
            newpath =  self.find_path(node, end, path)
            if newpath:
                return newpath
            
    # if no path can be found from any of the next nodes to the end, there's no path!
    return None

DiGraph.find_path = find_path

print(g.find_path('a', 'd'))

##-------------------------------------------------------------------------------------------
#----------------------------------------------- Find All Paths -----------------------------
##-------------------------------------------------------------------------------------------



def find_all_paths(self, start, end, path=[]):
    """Find path (not necessarily shortest) from start to end."""
    # sanity check 
    if start not in self.g:
        raise ValueError("Source node not in graph")
    
    # save the path we have traversed till now
    path = path + [start]

    # base case
    if start == end:
        return [ path ]
    
    all_paths = []
    # recursive case
    for node in self.g[start]:

        if node not in path:

            # find path from next node to 
            all_newpaths =  self.find_all_paths(node, end, path)
            for newPath in all_newpaths:
                all_paths.append(newPath)


            
    # if no path can be found from any of the next nodes to the end, there's no path!
    return all_paths

DiGraph.find_all_paths = find_all_paths

print(g.find_all_paths('a', 'd'))


##-------------------------------------------------------------------------------------------
# ----------------------------------------------- Shortest Path -----------------------------
##-------------------------------------------------------------------------------------------


def find_shortest_path(self, start, end, path=[]):
    """Find path (not necessarily shortest) from start to end."""
    # sanity check 
    if start not in self.g:
        raise ValueError("Source node not in graph")
    
    # save the path we have traversed till now
    path = path + [start]

    # base case
    if start == end:
        return path 
    
    shortest = None
    # recursive case
    for node in self.g[start]:

        if node not in path:

            # find path from next node to 
            newpaths =  self.find_shortest_path(node, end, path)
            if newpaths:
                if shortest is None or len(newpaths) < len(shortest):
                    shortest = newpaths


            
    # if no path can be found from any of the next nodes to the end, there's no path!
    return shortest

DiGraph.find_shortest_path = find_shortest_path

print(g.find_shortest_path('a', 'd'))



