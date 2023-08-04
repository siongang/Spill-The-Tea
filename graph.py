import networkx as nx
import matplotlib.pyplot as plt
import os

G = nx.Graph()

map = {}

image_path = "graph.png"

def draw():
    # Draw the graph
    pos = nx.spring_layout(G)  # Layout algorithm for graph visualization
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray", width=2, edge_cmap=plt.cm.Blues)
        
    # Add edge weights to the graph visualization
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')
  
  
    plt.savefig("graph.png")
    plt.clf()
    print(map)

def reset():
    global map
    map = {}
    plt.savefig("graph.png")
    plt.clf()
    G.clear()
     
def check(person1, person2):   
    global map 
    for p1 in map:
        if p1 == person1:
            mainNeighbors = map[p1]
            for mainSub in mainNeighbors:
                if mainSub == person2:
                    return False
    return True


def getWeight(person1, person2):
    global map
    if not check(person2, person1):
        return 2
    return 1


def connect(person1, person2):
    global map
    weight = ''
    if check(person1, person2):
        weight = getWeight(person1, person2)
       
        addToMap(person1,person2)
        G.add_edge(person1, person2, weight=weight)
        draw()


def addToMap(person1, person2):
    weight = getWeight(person1, person2)
    global map

    if person1 in map:
        neighbors = map[person1]
        neighbors.append(person2)
        map[person1] = neighbors
    else:
       map[person1] = [person2]


