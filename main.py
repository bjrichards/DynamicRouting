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

    # @Desc: Returns the generation_time of the packet
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


def main():
    print("Creating Packet 1")
    packet1 = Packet(5.0, 20, 1, 1, 2, 5)
    print("Packet 1 Created\n")

    print("Packet 1 Generation Time: ", packet1.GetGenerationTime())
    print("Packet 1 Size: ", packet1.GetSize())
    print("Packet 1 Flow ID: ", packet1.GetFlowID())
    print("Packet 1 Packet ID: ", packet1.GetPacketID())
    print("Packet 1 Source Node: ", packet1.GetSource())
    print("Packet 1 Destination Node: ", packet1.GetDestination())

    return

if __name__ == '__main__': main()
