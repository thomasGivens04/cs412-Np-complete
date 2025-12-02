#!/usr/bin/env python3

# Generates a complete graph on V vertices

V = 28
vertices = [f"v{i}" for i in range(1, V + 1)]

edges = []
for i in range(V):
    for j in range(i + 1, V):
        edges.append((vertices[i], vertices[j]))

print(len(edges))  # first line: number of edges
for u, v in edges:
    print(u, v)