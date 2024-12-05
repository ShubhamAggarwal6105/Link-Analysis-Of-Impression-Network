import csv
import networkx as nx
import numpy as np
import sys

# Create a directed graph
G = nx.DiGraph()

# Open the dataset file and create the graph
with open("./dataset.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        # Skip the header row
        if reader.line_num == 1:
            continue
        # Extract the parent node (source) from the second column
        parent = row[1].lower().split('@')[0]
        # Iterate through each entry in the row (child nodes)
        for entry in row[2:]:
            # Skip empty entries
            if entry == '':
                continue
            # Extract the child node (target) from the last word in the entry
            child = entry.lower().split()[-1]
            # Add an edge from the parent to the child in the graph
            G.add_edge(parent, child)

# Convert the graph to an adjacency matrix
nodes = list(G.nodes())
n = len(nodes)
adj = np.zeros(shape=(n,n))
for i in range(n):
    for j in range(n):
        # If there is an edge between nodes i and j, set the corresponding entry in the adjacency matrix to 1
        # If there is no edge, set the entry to -1
        if G.has_edge(nodes[i], nodes[j]):
            adj[i][j] = 1
        else:
            adj[i][j] = -1

# Implementation of Dijkstra's algorithm
def dijkstra(adjacency_matrix, start_vertex):
    # Get the number of nodes in the graph
    n = len(adjacency_matrix[0])

    # Initialize an array to store the shortest distances from the start_vertex to all other vertices
    shortest_distances = [sys.maxsize] * n
    # Initialize a boolean array to track whether each vertex has been added to the shortest path tree
    added = [False] * n

    # Set the distance from start_vertex to itself as 0
    shortest_distances[start_vertex] = 0
    # Initialize an array to store the parent vertices of each vertex in the shortest path tree
    parents = [-1] * n
    parents[start_vertex] = -1

    # Iterate over all vertices
    for i in range(1, n):
        # Find the vertex with the minimum distance from the start_vertex that has not been added to the shortest path tree
        nearest_vertex = -1
        shortest_distance = sys.maxsize
        for vertex_index in range(n):
            if not added[vertex_index] and shortest_distances[vertex_index] < shortest_distance:
                nearest_vertex = vertex_index
                shortest_distance = shortest_distances[vertex_index]

        # Add the nearest_vertex to the shortest path tree
        added[nearest_vertex] = True

        # Update the shortest distances to all vertices adjacent to nearest_vertex
        for vertex_index in range(n):
            edge_distance = adjacency_matrix[nearest_vertex][vertex_index]
            # If there is an edge from nearest_vertex to vertex_index and the distance through nearest_vertex is shorter than the current shortest distance, update the shortest distance
            if edge_distance > 0 and shortest_distance + edge_distance < shortest_distances[vertex_index]:
                parents[vertex_index] = nearest_vertex
                shortest_distances[vertex_index] = shortest_distance + edge_distance
    
    return shortest_distances

# Calculate the shortest distances between all pairs of nodes using Dijkstra's algorithm
distance = np.zeros(shape=(n,n))
for i in range(n):
    arr = dijkstra(adj, i)
    for j in range(n):
        # If the shortest distance is infinite (no path exists), set the distance to -1
        if arr[j] == sys.maxsize:
            distance[i][j] = -1
        else:
            distance[i][j] = int(arr[j])

# Print the shortest distance matrix
print("The shortest distance matrix: ")
print(distance)

#Observations based on the algorithm

max_distance = int(distance.max())

print("Maximum distance between any 2 nodes:", max_distance)
#This verifies that we can reach from one person to another through less than logN steps.

unreachable = 0
for i in range(n):
    for j in range(n):
        if distance[i][j] == -1:
            unreachable += 1
print("Number of pairs of unreachable nodes:", unreachable)
#We can find out how many people were absent during the exercise through this
print("Number of students absent:", unreachable/142)

counts = [0]*(max_distance+1)
for i in range(n):
    for j in range(n):
        x = int(distance[i][j])
        if 0<=x<=max_distance:
            counts[x] += 1
for i,cnt in enumerate(counts):
    print("Count of", i, ":", cnt)