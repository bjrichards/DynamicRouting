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
#A parser to read the log file into the format shown in main function
#A probability of failure in each node and edge
#Dynamic programming
#
#
#

# Will document later
def loadGraph():
    graph = Graph()
    fileToRead = "nodes.nd"
    fileIn = open(fileToRead, "r")
    soup = fileIn.read()

    lineSeperated = soup.split("\n")
    almostThere = []
    for piece in lineSeperated:
        almostThere.append(piece.split(":"))

    almostThere[0].pop(0)
    almostThere[1].pop(0)
    almostThere.pop(2)
    # print(almostThere)

    numOfNodes = int(almostThere[0][0])
    almostThere.pop(0)
    # print("Num of Nodes: ", numOfNodes)

    nodes = almostThere[0][0].split(" ")
    nodes.pop(0)
    almostThere.pop(0)
    # print("Nodes: ", nodes)

    edges = almostThere
    edges.pop()
    # print("Edges: ", edges)

    for node in nodes:
        graph.add_node(node)

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
