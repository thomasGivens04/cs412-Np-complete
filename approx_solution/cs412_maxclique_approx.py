import sys
import random
from collections import defaultdict


def main():
    vertices, adj = read_graph()
    best = max_clique_greedy_approx(vertices, adj, repeats=300)

    print(" ".join(best))


# Reads the graph
def read_graph():
    # reads all inputted lines
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return [], {}

    m = int(data[0].strip()) # the num of edges
    edges = []
    vertices = set()

    # gets the edges that connect the vertices
    for i in range(1, m + 1):
        u, v = data[i].split()
        edges.append((u, v))
        vertices.add(u)
        vertices.add(v)
    
    # adjacency list: maps each vertex to its neighbors
    adj = {v: set() for v in vertices}
    for u, v in edges:
        if u != v:
            adj[u].add(v)
            adj[v].add(u)
    
    return list(vertices), adj


# gets a clique
def greedy_approach(vertices, adj):
    if not vertices:
        return set()
    
    # Starts with a random vertex
    v = random.choice(vertices)
    c = {v}
    # vertices that connect to v, neighbors of v
    candidates = set(adj[v])

    while candidates:
        valid = []
        # choose vertices that are in the clique
        for x in candidates:
            if c <= adj[x]:
                valid.append(x)

        if not valid:
            break

        # pick randomly among the valid choices
        next_v = random.choice(valid)
        c.add(next_v)

        candidates &= adj[next_v]
    
    return c


# Repeats the greedy approach multiple times to improve result
def max_clique_greedy_approx(vertices, adj, repeats=200):
    best = set()
    for _ in range(repeats):
        # builds a clique
        c = greedy_approach(vertices, adj)
        # looks for the best one
        if len(c) > len(best):
            best = c
    return best


if __name__ == "__main__":
    main()
