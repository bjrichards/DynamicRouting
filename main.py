# Description: Final Project for CPE400
#              - Create a new routing straetgy that maximizes the overall
#                throughput of a mesh network.
#              - Simulate the above routing strategy using a simulated
#                network mesh
# Creators: Braeden Richards, Adam Cassell, Wen Le Ruan
# Created: November 27th, 2018


# @Desc: Packet object. Will be what is sent between nodes within a network
#        - Packets do not include a payload. Instead, a size of the packet in
#          terms of bytes will be used to determine transmission time
class Packet:

    # @Desc: Initializer
    # @Param: generation_time <float>: the time it takes to create the packet
    #                                  in ms
    #         size <int>: size in bytes of the packet. Used to determine
    #                     transmission time
    #         flow_id <int>:
    #         packet_id <int>:
    #         source <int>: which node the packet originated from
    #         destination <int>: which node the packet is meant for
    # @Return: void
    def __init__(self, generation_time, size, flow_id, packet_id, source,
                 destination):
        self.generation_time = generation_time
        self.size = size
        self.flow_id = flow_id
        self.packet_id = packet_id
        self.source = source
        self.destination = destination

        return

    # @Desc: Returns the generation_time of the packet in ms
    # @Param: Void
    # @Return: self.generation_time <float>
    def GetGenerationTime(self):
        return self.generation_time

    # @Desc: Returns the size of the packet
    # @Param: Void
    # @Return: self.size <int>
    def GetSize(self):
        return self.size

    # @Desc: Returns the flow id of the packet
    # @Param: Void
    # @Return: self.flow_id <int>
    def GetFlowID(self):
        return self.flow_id

    # @Desc: Returns the packet id of the packet
    # @Param: Void
    # @Return: self.packet_id <id>
    def GetPacketID(self):
        return self.packet_id

    # @Desc: Returns the source node id of the packet
    # @Param: Void
    # @Return: self.source <int>
    def GetSource(self):
        return self.source

    # @Desc: Returns the destination node id of the packet
    # @Param: Void
    # @Return: self.destination <int>
    def GetDestination(self):
        return self.destination

# @Desc: Node object. Each node makes up a piece of the network
class Node:
    # @Desc: Initializer
    # @Param: nodeID <int>: the ID of the node
    #         numberOfConnections <int>: the number of nodes connected to this
    #                                    node
    #         connectedNodes <List[int]>: A list containing the ID's of the
    #                                     connected nodes
    # @Return: Void
    def __init__(self, nodeID, numberOfInterfaces, nodes):
        self.nodeID = nodeID
        self.numberOfInterfaces = numberOfInterfaces
        self.interfaces = []
        for node in nodes:
            self.interfaces.append(int(node))

        print("\tNode ID: ", self.nodeID)
        print("\tNode # Connections: ", self.interfaces)
        print("\tNodes Connected: ", self.interfaces)

        return

# @Desc: Reads the nodal information from the file and creates a list of nodes
#        that make up the network
# @Param: node_file <string>: the file path and name to open
# @Return: nodes <List[node]>: List of nodes
def LoadNodeNetwork(nodeFile):
    node_file = open(NodeFile, 'r')
    soup = node_file.read()
    slightly_less_soup = soup.split("\n")
    nodes = []
    for i in range(1, int(slightly_less_soup[0]) + 1):
        node = slightly_less_soup[i].split(" ")
        nodeID = int(node[0])
        nodeNumConnections = int(node[1])
        otherNodes = []
        for j in range(1, nodeNumConnections + 1):
            otherNodes.append(node[j + 1])

        print("Creating Node: ", nodeID)
        newNode = Node(nodeID, nodeNumConnections, otherNodes)
        nodes.append(newNode)

    return nodes

# Path and name to file containing the nodes of the network
NodeFile = "nodes.nd"

def main():
    # Load in nodes to program
    nodes = LoadNodeNetwork(NodeFile)

    return

if __name__ == '__main__': main()
