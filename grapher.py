import networkx as nx
import matplotlib.pyplot as plt

class Map:
    image_path = "graph.png"

    # constructor
    def __init__(self, server):
        # map of connections
        self.map = {}
        # number of links
        self.linkCounter = 0
        # server name
        self.serverName = server
        # graph object
        self.G = nx.Graph()

    # draw the map onto the file
    # sizes nodes and zooms out based on number of people on the map
    def drawMap(self):
        # number of nodes
        nodeNum = self.G.number_of_nodes()
        
        # Draw the graph
        pos = nx.spring_layout(self.G)  # Layout algorithm for graph visualization
        plt.figure(figsize=(7.5 + self.linkCounter/2, 4.5 + self.linkCounter/2))  # Set the figure size (width, height)

        # print("num of nodes :"+ str(self.linkCounter))
        # print("x " + str(10 + self.linkCounter/3))
    
        # size variables which decrease as more people are added to the map
        fontSize = 10-nodeNum/6
        if fontSize <= 2:
            fontSize = 2

        nodeSize = 1000 - 10*nodeNum

        # draw the map
        nx.draw(self.G, pos, with_labels=True, node_size=nodeSize, node_color="skyblue", font_size=fontSize, font_weight="semibold", edge_color="gray", width=2, edge_cmap=plt.cm.Blues)
            
        # Add edge weights to the graph visualization
        labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels, font_color='red')
    
        plt.savefig("graph.png") # save figure to path
        plt.clf() # clear the figure (canvas)
        print(map)
        

    # checks if there already is a connection between person 1 and person 2
    # returns true if there is no connection
    # returns false if there is a connection
    def check(self, person1, person2):   
        for p1 in self.map:
            if p1 == person1:
                mainNeighbors = self.map[p1]
                for mainSub in mainNeighbors:
                    if mainSub == person2:
                        return False
        return True
    
    # gets the weight of the connection by checking if person 2 ever submitted a connection towards person 1
    # if weight is 2, there is a mutual connection
    # if weight is 1, it is one sided
    def getWeight(self, person1, person2):
        if not self.check(person2, person1):
            return 2
        return 1


    # main code to add connection between person 1 and person 2
    def connect(self, person1, person2):
        weight = ''
        if self.check(person1, person2):
            weight = self.getWeight(person1, person2)
            self.addToMap(person1, person2)
            self.G.add_edge(person1, person2, weight=weight)
            self.linkCounter += 1
            self.drawMap()

    # maps the new connection to the list [map]
    def addToMap(self, person1, person2):
        if person1 in self.map:
            neighbors = self.map[person1]
            neighbors.append(person2)
            self.map[person1] = neighbors
        else: 
            self.map[person1] = [person2] # adds as person 2 as a list

    # resets map
    def reset(self):
        self.map = {}
        plt.savefig("graph.png")
        plt.clf()
        self.G.clear()
        self.linkCounter = 0
        