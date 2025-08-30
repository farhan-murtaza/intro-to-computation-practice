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
    weight_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, labels=labels, **options)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weight_labels, font_size=15)
    plt.show()

class WeightedDiGraph:
    def __init__(self):
        self.g = {}

    def add_node(self, node):
        if node in self.g:
            raise ValueError("Node already in graph")
        
        self.g[node] = []

    def add_edge(self, src, dest, weight):
        # sanity checks
        if src not in self.g :
            raise ValueError("Source node not exist in graph.")
        if dest not in self.g:
            raise ValueError("Destination node not exist in graph.")
        
        next = self.g[src]

        if dest in next:
            return
        next.append((dest, weight))



    def draw_graph(self):
        G = nx.DiGraph()
        for src in self.g:
            G.add_node(src, label=src)
            for dest in self.g[src]:
                G.add_edge(src, dest[0], weight=str(dest[1]))
        
        draw_graph_with_nx(G)

g = WeightedDiGraph()

nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for n in nodes:
    g.add_node(n)


edges = [
    ('a', 'b', 4),
    ('a', 'c', 1),
    ('b', 'd', 8),
    ('c', 'e', 25),
    ('e', 'd', 3),
    ('d', 'f', 5),
    ('d', 'g', 7),
    # ('f', 'h', 2),
    # ('g', 'h', 9)
]

for e in edges:
    g.add_edge(e[0], e[1], e[2])


# print(g.g)

pprint.pprint(g.g)          # pretty printing!


# g.draw_graph()


## ---------------------------------------------------------------------------------------------
# ------------------------ Dijkstra's Shortest Path - Finding Minimum Cost ---------------------
## ---------------------------------------------------------------------------------------------




def find_shortest_dijkstra(self, src):
    # Mark all nodes unvisited and store them
    to_visit = list( self.g.keys() )

    print("To visit: " + str(to_visit))

    # Set the distance to zero for our initial node and to infinity for other nodes
    inf = float('inf')      # that's python for infinity
    dists = {node: inf for node in to_visit}
    dists[src] = 0

    print("All distances"+ str(dists))

    # let's loop
    while to_visit:
        print("----------")

        # Select the unvisited node with  the smallest distance
        # can't compare 'a' with 'b'. So, we compare dists['a'] with dists['b']
        current = min(to_visit, key=lambda node: dists[node])
        print("Current: "+ current)

        # current is now visited
        to_visit.remove(current)

        # check to make sure min distance isn't infinity
        if dists[current] == inf:
            break


        # Find unvisited neighbors for the current node
        nexts = self.g[current]
        unvisited_neighbors = []
        for n in nexts:
            if n[0] in to_visit:
                unvisited_neighbors.append(n)
            
        print("Unvisited neighbors of " + current + ": " + str(unvisited_neighbors))


        # calculate their distances through the current node
        for n in unvisited_neighbors:
            label = n[0]
            dist_to = n[1]

            old_distance = dists[label]
            new_distance = dists[current] + dist_to


            # See which is better: old best distance or this one
            if new_distance < old_distance:
                dists[label] = new_distance


        
        print("All distances" + str(dists))

        # current is now visited
        # to_visit.remove(current)


WeightedDiGraph.find_shortest_dijkstra = find_shortest_dijkstra

# g.find_shortest_dijkstra('a')


def find_shortest_path_dijkstra(self, src, dest):
      # Mark all nodes unvisited and store them
    to_visit = list( self.g.keys() )

    print("To visit: " + str(to_visit))

    # Set the distance to zero for our initial node and to infinity for other nodes
    inf = float('inf')      # that's python for infinity
    dists = {node: inf for node in to_visit}
    dists[src] = 0

    print("All distances"+ str(dists))

    best_paths = {}
    best_paths[(src, src)] = [src]   # no move

    # let's loop
    while to_visit:
        print("----------")

        # Select the unvisited node with  the smallest distance
        # can't compare 'a' with 'b'. So, we compare dists['a'] with dists['b']
        current = min(to_visit, key=lambda node: dists[node])
        print("Current: "+ current)

        # current is now visited
        to_visit.remove(current)

        # check to make sure min distance isn't infinity
        if dists[current] == inf:
            break


        # Find unvisited neighbors for the current node
        nexts = self.g[current]
        unvisited_neighbors = []
        for n in nexts:
            if n[0] in to_visit:
                unvisited_neighbors.append(n)
            
        print("Unvisited neighbors of " + current + ": " + str(unvisited_neighbors))


        # calculate their distances through the current node
        for n in unvisited_neighbors:
            label = n[0]
            dist_to = n[1]

            old_distance = dists[label]
            new_distance = dists[current] + dist_to


            # See which is better: old best distance or this one
            if new_distance < old_distance:
                print('\nFound new best path ...')
                dists[label] = new_distance

                
                # also save path
                # best way to get from src to label is src -> current -> label
                path_to_current = best_paths[(src, current)][:]     # need a copy
                best_paths[(src, label)] = path_to_current
                best_paths[(src, label)].append(label)
                print("Previous best path to current: ", best_paths[(src, current)])
                print("Best path to:", label, ": ", best_paths[(src, label)])


        
        print("All distances" + str(dists))

        # current is now visited
        # to_visit.remove(current)
    
    return best_paths[(src, dest)], dists[dest]


WeightedDiGraph.find_shortest_path_dijkstra = find_shortest_path_dijkstra


print(g.find_shortest_path_dijkstra('a', 'd'))
