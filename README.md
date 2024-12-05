# Impression Network Analysis

This project is a comprehensive analysis of a network of impressions derived from a dataset. It includes various algorithms for shortest path analysis, missing link prediction, and ranking nodes using random walk-based PageRank. The implementation is written in Python and utilizes the NetworkX library for graph-related operations.

---

## Features
1. **Random Walk-Based PageRank**
   - Implements a random walk algorithm to rank nodes based on their importance.
   - Identifies the top leaders in the network based on normalized ratings.

2. **Missing Link Prediction**
   - Uses a matrix-based method to predict missing edges in the network.
   - Adds predicted missing links to the graph and recalculates PageRank scores for updated rankings.

3. **Shortest Path Analysis**
   - Computes the shortest distances between all pairs of nodes using Dijkstra's algorithm.
   - Provides metrics such as the maximum distance, unreachable node pairs, and node absence rates.

---

## Files
- **`requirements.txt`**: Specifies the required libraries for the project.
- **`shortest_path_analysis.py`**: Contains the implementation for shortest path calculations and related statistics.
- **`missing_link_prediction.py`**: Implements the missing link prediction algorithm and recalculates PageRank for the updated network.
- **`random_walk_pagerank.py`**: Performs node ranking using a random walk algorithm.
- **`dataset.csv`**: The dataset file representing the impression network.
- **`Report.pdf`**: The report of the final project, containing detailed statistics and results of the project.

---

## Prerequisites
- Python 3.7 or higher
- Install dependencies using the following command:
  ```bash
  pip install -r requirements.txt
  ```

---

## Usage
1. **Random Walk-Based PageRank**
   - Execute `random_walk_pagerank.py` to compute the PageRank scores using a random walk method.
   - Example:
     ```bash
     python random_walk_pagerank.py
     ```

2. **Missing Link Prediction**
   - Run `missing_link_prediction.py` to identify and add missing links, followed by recalculating rankings.
   - Example:
     ```bash
     python missing_link_prediction.py
     ```

3. **Shortest Path Analysis**
   - Run `shortest_path_analysis.py` to compute shortest distances between nodes and related metrics.
   - Example:
     ```bash
     python shortest_path_analysis.py
     ```

---

## Dataset
The dataset should be in CSV format. The columns are interpreted as follows:
1. **Parent Node**: The second column specifies the source node.
2. **Child Nodes**: Subsequent columns represent target nodes connected to the source node.

---

## Output
- **Random Walk-Based PageRank**
  - Top 10 nodes with the highest ratings
- **Missing Link Prediction**
  - List of predicted links
  - Updated PageRank rankings
- **Shortest Path Analysis**
  - Distance matrix
  - Maximum distance
  - Unreachable node statistics

---

## Libraries Used
- [NetworkX](https://networkx.org): For graph creation and manipulation.
- [NumPy](https://numpy.org): For numerical computations.
- [CSV](https://docs.python.org/3/library/csv.html): For handling the dataset file.

---

## Author
Prepared by Shubham Aggarwal.
---