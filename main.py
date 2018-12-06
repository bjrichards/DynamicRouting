# CPE 400 Final Project
# Created November 27, 2018
# Written by: Braeden Richards, Wen Le Ruan, Adam Cassell

# Imports
from collections import defaultdict
from random import randint


#Graph class used to network the nodes
#Contains the nodes, edges, as well as the distances between each one
#Used mainly to compliment the dijkstra algorithm
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
        self.failurePercentage = defaultdict(list)
    #self.failPerc = set()

    def add_node(self, value, failurePercentage):
        self.nodes.add(value)
        self.failurePercentage[value].append(failurePercentage)
    #self.nodes.add(fail)

    def add_edge(self, start, end, distance):
        self.edges[start].append(end)
        self.edges[end].append(start)
        self.distances[(start, end)] = distance
        self.distances[(end, start)] = distance

    def rmv_node(self, node):
        self.nodes.remove(str(node))
        del self.edges[node]
        for nodes in self.nodes:
            for thing in self.edges[nodes]:
                for i in range(0, len(self.edges[nodes])):
                    if(self.edges[nodes][i] == node):
                        del self.edges[nodes][i]
                        break;

    #Removing the edges to simulate a failure of a connection
    def rmv_edge(self, start, end, distance):
        self.edges[start].remove(end)
        self.edges[end].remove(start)
        self.distances[(start, end)] = 0
        self.distances[(end, start)] = 0

    def printAll(self):
        print("Nodes: ", end="\n\t")
        for node in self.nodes:
            print(node, " ", end="")

        print("\nEdges: ")
        for node in self.nodes:
            print("\tNode ", node, "is connected to: ",self.edges[node], " ")

        print("Nodes Failure Percentages:")
        for node in self.nodes:
            print("\tNode ", node, "is ", self.failurePercentage[node][0], "% likely to fail")



#Dijkstra's algorithm in finding the shortest path
#It takes in the starting node and finds the shortest distance for each node
#Returns the list the of nodes and the distances
#Returns the path taken to reach that conclusion
def dijkstraAlg(graph, start):
  totalDistance = {start: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes:
    min_node = None

    for node in nodes:

      if node in totalDistance:

        if min_node is None:
          min_node = node

        elif totalDistance[node] < totalDistance[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = totalDistance[min_node]

    #Takes the edges and compares them with the different routes
    #Takes the minimum of the distances and uses that as
    #the shortest distance
    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distances[(min_node, edge)]
      if edge not in totalDistance or weight < totalDistance[edge]:
        totalDistance[edge] = weight
        path[edge] = min_node

    #Returns the nodes and the distances as well as the set of paths taken
  return totalDistance, path



# @Desc: Reads the nodes in from the nodes.nd file and stores it in a graph
# @Param: Void
# @Return: <Graph> graph: a graph containing the nodes and their edges
def loadGraph(fileName):
    graph = Graph()
    fileToRead = fileName
    fileIn = open(fileToRead, "r")
    soup = fileIn.read()

    # Seperate percentage of filure with the rest
    stuff = soup.split("~~")
    percentages = stuff[1]

    # Break the soup up into list items split by new lines
    lineSeperated = stuff[0].split("\n")
    almostThere = []
    # Split the list into a list of lists seperated by colons
    for piece in lineSeperated:
        almostThere.append(piece.split(":"))

    # Get rid of the lines that don't include data, such as headers
    almostThere[0].pop(0)
    almostThere[1].pop(0)
    almostThere.pop(2)
    # print(almostThere)

    # Get the number of nodes in the graph
    numOfNodes = int(almostThere[0][0])
    almostThere.pop(0) # Pop to make the next parsing easier

    # Gather the nodes from the soup
    nodes = almostThere[0][0].split(" ")
    # print(nodes)
    nodes.pop(0) # Pop as the first list item is a ' ' due to how file is written
    almostThere.pop(0) # Pop to make the next parsing easier

    # Since all that's left in almostThere is the edges, just make the edges
    #   list the almostThere list
    edges = almostThere
    edges.pop() # Pop the first list item since it is a ' '

    # Add the nodes to the graph
    i = 0
    perc = percentages.split("\n")
    perc.pop(0)
    perc.pop(0)
    for node in nodes:
        graph.add_node(node, int(perc[i].split(" ")[2]))
        i = i + 1
        # print(node)

    # Add the edges to the graph
    for edge in edges:
        pieces = edge[0].split(' ')
        graph.add_edge(pieces[0], pieces[1], int(pieces[2]))

    return graph


# @Desc: Prints the menu and gets userInput from menu
# @Param: Void
# @Return: <int> userInput
def Menu():
    print("1) Run until node failure")
    print("2) Choose node to fail")
    print("3) Add node")
    print("4) Add an edge")
    print("5) Find shortest paths from a node to all others")
    print("6) Print graph")
    print("7) Exit program")
    userInput = input("> ")

    return userInput

def NodeFailure(graph):
    nodeFail = False
    while nodeFail is False:
        for node in graph.nodes:
            check = randint(0,100)
            if check < graph.failurePercentage[node][0]:
                print("Node ", node, "has failed!")
                print("Node ", node, "has been removed from the graph")
                graph.rmv_node(node)
                print("All edges of node", node, " now removed")
                return
    return

def main():

    for i in range(0, 100):
        print("\n")
    print("Welcome to the network node failure simulation")
    fileInput = input("Please enter the node file name: ")
    print("Reading in node file~")
    print("Now printing all routes starting from the first node")
    fileName = fileInput
    graph = loadGraph(fileName)
    userInput = 90

    # This is just dealing with the menu and the choices of the menu the user
    #   makes
    while userInput is not '7':
        for i in range(0, 100):
            print("\n")
        userInput = Menu()
        if userInput is '1':
            while not NodeFailure(graph):
                break
            input("__Press enter to continue__")
        elif userInput is '2':
            nodeToFail = input("Which node should fail: ")
            graph.rmv_node(nodeToFail)
            input("__Press enter to continue__")
        elif userInput is '3':
            nodeToAdd = input("What node would you like to add: ")
            while nodeToAdd in graph.nodes:
                print("That node already exists.")
                nodeToAdd = input("What node would you like to add: ")
            graph.add_node(str(nodeToAdd))
            print("Node ", nodeToAdd, " added to the network.")
            input("__Press enter to continue__")
        elif userInput == '4':
            firstNode = input("What node should the edge start at: ")
            while firstNode not in graph.nodes:
                print("That node does not currently exist.")
                firstNode = input("What node should the edge start at: ")
            secondNode = input("What node should the edge end at: ")
            while secondNode not in graph.nodes:
                print("That node does not currently exist.")
                secondNode = input("What node should the edge end at: ")
            weight = input("What should the weight of the edge be: ")
            while int(weight) < 0:
                print("Weights need to be 0 or above.")
                weight = input("What should the weight of the edge be: ")
            graph.add_edge(str(firstNode), str(secondNode), int(weight))
            print("Edge is added!")
            input("__Press enter to continue__")
        elif userInput is '5':
            nodeToStart = ''
            first = True
            while nodeToStart not in graph.nodes:
                if first is False:
                    input("Not in the network")
                else:
                    first = False
                nodeToStart = input("What node to start with? ")
            print("Running Dijkstra's starting with node ", nodeToStart)
            print(dijkstraAlg(graph, str(nodeToStart)))
            input("__Press enter to continue__")
        elif userInput is '6':
            graph.printAll()
            input("__Press enter to continue__")
        elif userInput is '7':
            break
        else:
            print("Not correct input")
            input("__Press enter to continue__")

    return

if __name__ == '__main__': main()
