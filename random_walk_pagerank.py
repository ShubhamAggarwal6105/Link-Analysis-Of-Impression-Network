import csv
import networkx as nx
import random

# Create a directed graph
G = nx.DiGraph()

# Define a function for random walk
def random_walk(steps):
    # Initialize a dictionary to store ratings for each node
    rating = dict.fromkeys(list(G.nodes), 0)
    # Choose a random starting node
    current_node = random.choice(list(G.nodes))
    # Perform random walk for the specified number of steps
    for i in range(steps):
        # With probability 0.15, randomly jump to any node
        if random.random() < 0.15:
            current_node = random.choice(list(G.nodes))
        else:
            # Select a neighbor of the current node to move to
            neighbors = list(G.neighbors(current_node))
            if neighbors:
                current_node = random.choice(neighbors)
            else:
                # If the current node has no neighbors, randomly jump to any node
                current_node = random.choice(list(G.nodes))
        # Increment the rating of the current node
        rating[current_node] += 1
    return rating

# Open the dataset file
with open("./dataset.csv") as f:
    reader = csv.reader(f)
    # Iterate over each row in the dataset
    for row in reader:
        # Skip the header row
        if reader.line_num == 1:
            continue
        # Get the parent node (source) from the first column
        parent = row[1].lower().split('@')[0]
        # Iterate over the child nodes (targets) in the row
        for entry in row[2:]:
            # Skip empty entries
            if entry == '':
                continue
            # Get the child node (target) from the last word in the entry
            child = entry.lower().split()[-1]
            # Add an edge from the parent to the child in the graph
            G.add_edge(parent, child)

# Define the total number of steps for the random walk
total = 10000000
# Perform random walk and get the ratings for each node
rating = random_walk(total)
# Sort nodes by their ratings in descending order
ranking = sorted(rating, key=rating.get, reverse=True)
# Print the top 10 leaders based on the random walk algorithm
print("The top 10 leaders -:")
for i in range(10):
    name = ranking[i]
    rate = rating[name] / total  # Normalize rating by total steps
    print(i+1, name, rate)

print("The top leader is", ranking[0],"with",rating[ranking[0]]/total, "points.")