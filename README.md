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
NID #CN CNID1:CNW1 CNID2:CNW2 ...
NID #CN CNID1:CNW1 CNID2:CNW2 ...
NID #CN CNID1:CNW1 CNID2:CNW2 ...
```
```
NID - Node ID <int>
#CN - Number of connected nodes <int>
CNID# - Connected node ID # <int>
CNW# - Connected Node's interface weight <int>
```
To see an example, check the included nodes.nd file.
