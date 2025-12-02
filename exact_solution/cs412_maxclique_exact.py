#!/usr/bin/env python3
# cs412_maxclique_exact.py
# Part A of NP-Complete Final Project
# Alex Macauley

import sys
import itertools
import time


# Reads input and returns an adjacency set
def read_graph():
    line = sys.stdin.readline().strip()
    if not line:
        return {}

    n = int(line)   # number of edges
    adj = {}

    for _ in range(n):
        u, v = sys.stdin.readline().split()

        if u not in adj:
            adj[u] = set()
        if v not in adj:
            adj[v] = set()

        adj[u].add(v)
        adj[v].add(u)

    return adj


# Helper to check if nodes form a clique
def is_clique(nodes, adj):
    for u, v in itertools.combinations(nodes, 2):
        if v not in adj[u]:
            return False
    return True


# Brute force all subsets of vertices
def brute_force_max_clique(adj):
    vertices = list(adj.keys())
    n = len(vertices)
    best_clique = []

    # go through every possible subset
    for clique in range(1, n + 1):
        for subset in itertools.combinations(vertices, clique):
            if is_clique(subset, adj):
                if len(subset) > len(best_clique):
                    best_clique = list(subset)

    return best_clique


def main():
    start = time.time()

    adj = read_graph()
    if not adj:
        print("")  
        return

    clique = brute_force_max_clique(adj)
    print(" ".join(clique))

    end = time.time()
    endSeconds = end - start
    endMinutes = endSeconds // 60
    remainingSeconds = endSeconds % 60
    if endMinutes >= 1:
        print(f"Runtime: {endMinutes} minutes and {remainingSeconds:.2f} seconds")
    elif endSeconds < 1:
        endMilliseconds = endSeconds * 1000
        print(f"Runtime: {endMilliseconds:.8f} milliseconds")
    else:
        print(f"Runtime: {endSeconds:.4f} seconds")


if __name__ == "__main__":
    main()
