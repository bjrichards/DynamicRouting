# CPE 400 Final Project
# Created November 27, 2018
# Written by: Braeden Richards, Wen Le Ruan, Adam Cassell

# Imports
from collections import defaultdict


#Graph class used to network the nodes
#Contains the nodes, edges, as well as the distances between each one
#Used mainly to compliment the dijkstra algorithm
class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance
    self.distances[(to_node, from_node)] = distance

  #Removing the edges to simulate a failure of a connection
  def rmv_edge(self, from_node, to_node, distance):
    self.edges[from_node].remove(to_node)
    self.edges[to_node].remove(from_node)
    self.distances[(from_node, to_node)] = 0
    self.distances[(to_node, from_node)] = 0


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






#WHAT WE STILL NEED
#A probability of failure in each node and edge
#Dynamic programming

# @Desc: Reads the nodes in from the nodes.nd file and stores it in a graph
# @Param: Void
# @Return: <Graph> graph: a graph containing the nodes and their edges
def loadGraph():
    graph = Graph()
    fileToRead = "nodes.nd"
    fileIn = open(fileToRead, "r")
    soup = fileIn.read()

    # Break the soup up into list items split by new lines
    lineSeperated = soup.split("\n")
    almostThere = []
    # Split the list into a list of lists seperated by colons
    for piece in lineSeperated:
        almostThere.append(piece.split(":"))

    # Get rid of the lines that don't include data, such as headers
    almostThere[0].pop(0)
    almostThere[1].pop(0)
    almostThere.pop(2)

    # Get the number of nodes in the graph
    numOfNodes = int(almostThere[0][0])
    almostThere.pop(0) # Pop to make the next parsing easier

    # Gather the nodes from the soup
    nodes = almostThere[0][0].split(" ")
    nodes.pop(0) # Pop as the first list item is a ' ' due to how file is written
    almostThere.pop(0) # Pop to make the next parsing easier

    # Since all that's left in almostThere is the edges, just make the edges
    #   list the almostThere list
    edges = almostThere
    edges.pop() # Pop the first list item since it is a ' '

    # Add the nodes to the graph
    for node in nodes:
        graph.add_node(node)

    # Add the edges to the graph
    for edge in edges:
        pieces = edge[0].split(' ')
        graph.add_edge(pieces[0], pieces[1], int(pieces[2]))

    return graph


def main():

    g = loadGraph()
    print(dijkstraAlg(g, 'a'))
    g.rmv_edge('c', 'e', 20)
    print(dijkstraAlg(g, 'a'))
    g.add_edge('c', 'e', 20)
    print(dijkstraAlg(g, 'a'))



    return

if __name__ == '__main__': main()
