# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:08:27 2023

@author: ChatGPT
"""

import csv
import pandas as pd

# Open an Excel file
df = pd.read_excel('filename.xlsx')

# Print the first 5 rows of the Excel file
print(df.head())


# # Open the CSV file
# with open('graph.csv') as csvfile:
#     # Create a CSV reader object
#     reader = csv.reader(csvfile)
#     # Skip the header row
#     next(reader)
#     # Create an empty dictionary to store the graph data
#     graph = {}
#     # Iterate over each row in the CSV file
#     for row in reader:
#         # Extract the node IDs and distance from the row
#         node1, node2, distance = row
#         # Convert the distance to an integer
#         distance = int(distance)
#         # Add the nodes and distance to the graph dictionary
#         if node1 not in graph:
#             graph[node1] = {}
       

def find_eulerian_tour(graph):
    """
    Find an Eulerian tour in a graph.

    :param graph: The graph to find the Eulerian tour in, represented as an adjacency list.
    :return: The Eulerian tour as a list of node IDs.
    """
    # Find nodes with odd degree
    odd_nodes = [node for node in graph if len(graph[node]) % 2 != 0]

    # If there are no odd nodes, the graph already has an Eulerian tour
    if not odd_nodes:
        start_node = next(iter(graph))
    # If there are two odd nodes, add an edge between them to make the graph Eulerian
    elif len(odd_nodes) == 2:
        start_node = odd_nodes[0]
        graph[start_node].append(odd_nodes[1])
        graph[odd_nodes[1]].append(start_node)
    # Otherwise, the graph can't have an Eulerian tour
    else:
        return None

    # Use the Edmonds-Karp algorithm to find a minimum-cost perfect matching
    matching = {}
    dist = {}
    for node in odd_nodes:
        dist[node] = 0
    while True:
        # Find the shortest augmenting path using BFS
        queue = [start_node]
        parents = {start_node: None}
        while queue:
            node = queue.pop(0)
            if node in odd_nodes:
                break
            for neighbor in graph[node]:
                if neighbor not in parents:
                    parents[neighbor] = node
                    queue.append(neighbor)
        else:
            break

        # Find the bottleneck edge in the augmenting path
        bottleneck = float('inf')
        node = odd_nodes[odd_nodes.index(node)]
        while node is not None:
            prev_node = parents[node]
            if prev_node is not None:
                if dist[node] % 2 == 0:
                    bottleneck = min(bottleneck, graph[prev_node][node])
                else:
                    bottleneck = min(bottleneck, matching[node])
                node = prev_node
            else:
                break

        # Update the distance function and the matching
        node = odd_nodes[odd_nodes.index(node)]
        while node is not None:
            prev_node = parents[node]
            if prev_node is not None:
                if dist[node] % 2 == 0:
                    graph[prev_node][node] -= bottleneck
                    if graph[prev_node][node] == 0:
                        del graph[prev_node][node]
                        del graph[node][prev_node]
                else:
                    matching[node] -= bottleneck
                    if matching[node] == 0:
                        del matching[node]
                        del matching[prev_node]
                        dist[node] = 0
                    else:
                        dist[node] += bottleneck
                node = prev_node
            else:
                break

    # Construct the Eulerian tour
    tour = []
    stack = [start_node]
    while stack:
        node = stack[-1]
        if node in graph and graph[node]:
            next_node = graph[node].pop(0)
            stack.append(next_node)
            del graph[next_node][node]
        else:
            tour.append(stack.pop())

    return tour[::-1]