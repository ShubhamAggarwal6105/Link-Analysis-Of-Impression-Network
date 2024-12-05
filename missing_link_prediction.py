import csv
import networkx as nx
import numpy as np

# Create a directed graph
G = nx.DiGraph()

# Open the dataset file and create the graph
with open("./dataset.csv") as f:
    reader = csv.reader(f)
    # Iterate through each row in the dataset
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

# Convert the graph to adjacency matrix
nodes = list(G.nodes())
n = len(nodes)
adj = np.zeros(shape=(n,n))
for i in range(n):
    for j in range(n):
        # Check if there is an edge between nodes i and j
        if G.has_edge(nodes[i], nodes[j]):
            # If there is an edge, set the corresponding entry in the adjacency matrix to 1
            adj[i][j] = 1

# Function to predict missing links using matrix method
def predict(i, j):
    # Remove the j-th column from the adjacency matrix
    without_col = np.delete(adj, j, axis=1)
    # Extract the i-th row from the modified adjacency matrix
    B = without_col[i]
    # Remove the i-th row from the modified adjacency matrix
    A = np.delete(without_col, i, axis=0)
    # Solve the system of linear equations Ax = B to find coefficients x
    X = np.linalg.lstsq(A.T, B.T, rcond=None)[0]
    # Remove the i-th row from the original adjacency matrix
    without_row = np.delete(adj, i, axis=0)
    # Extract the j-th column from the modified adjacency matrix
    C = without_row[:, j]
    # Calculate the expected value for the missing link
    expected = np.matmul(C, X)
    return expected

# Find missing links and add them to the graph
missing_links = []
for i in range(n):
    for j in range(n):
        # Check if there is no edge between nodes i and j
        if adj[i][j] == 0:
            # Predict the value of the missing link using the matrix method
            val = predict(i, j)
            # If the predicted value is greater than or equal to 1, consider it as a missing link
            if val > 0.5:
                missing_links.append((i, j))

for i, j in missing_links:
    # Print the missing link (node i to node j)
    print("Missing Link:", (nodes[i], nodes[j]))
    # Add the missing link to the graph
    G.add_edge(nodes[i], nodes[j])

# Calculate PageRank scores for the updated graph
rating = nx.pagerank(G)
# Sort nodes by their PageRank scores in descending order
ranking = sorted(rating, key=rating.get, reverse=True)
# Print the top 10 nodes with the highest PageRank scores
for i in range(10):
    name = ranking[i]
    rate = rating[name]
    print(name, rate)
