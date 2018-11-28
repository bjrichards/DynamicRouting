# Dynamic Routing Mechanism Design with Focus on Throughput

## Prompt
Create  and  simulate  a  new routing  strategy  that  maximizes  the  overall  throughput  of  a  mesh  network.
Throughput  is  affected  by
many  factors  that  should  be  considered,  such  as  nodal  processing  delay,
overloaded buffers, loss, etc. The more realistic assumptions you can make for your network, better it is.

## Required Resources
```
Python3
```

## nodes.nd
The node network is stored in the file nodes.nd. If changing the network, the format for nodes.nd is:
```
#OfNodes
NID #CN CNID1 CNID2 ...
NID #CN CNID1 CNID2 ...
NID #CN CNID1 CNID2 ...
```
```
NID - Node ID
#CN - Number of connected nodes
CNID# - Connected node ID #
```
To see an example, check the included nodes.nd file.
