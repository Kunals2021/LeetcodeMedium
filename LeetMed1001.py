# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def __init__(self):
        # A dictionary to store the cloned nodes
        self.cloned_nodes = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        # Return None if the input node is None
        if not node:
            return None

        # Create a new node with the same value as the input node
        cloned_node = Node(node.val)
        # Store the cloned node in the dictionary
        self.cloned_nodes[node] = cloned_node

        # Recursively clone the neighbors of the input node
        for neighbor in node.neighbors:
            if neighbor in self.cloned_nodes:
                # If the neighbor has already been cloned, use the cloned node
                cloned_node.neighbors.append(self.cloned_nodes[neighbor])
            else:
                # If the neighbor has not been cloned, create a new node and clone it recursively
                cloned_neighbor = self.cloneGraph(neighbor)
                cloned_node.neighbors.append(cloned_neighbor)

        # Return the cloned node
        return cloned_node

# we create a dictionary called cloned_nodes to store the cloned nodes. We then define a recursive 
# function cloneGraph that takes a node as input and returns a deep copy of the input graph. 
# If the input node is None, we return None.
# Otherwise, we create a new node with the same value as the input node, and store it in the cloned_nodes
# dictionary. We then iterate through the neighbors of the input node, and for each neighbor, 
# we check if it has already been cloned by checking if it is in the cloned_nodes dictionary. 
# If it has been cloned, we use the cloned node. If it has not been cloned, we create a new node 
# and clone it recursively by calling cloneGraph with the neighbor as input.
# Finally, we return the cloned node. This implementation ensures that each node in the input graph 
# is cloned exactly once, and that all connections between nodes are preserved in the cloned graph.