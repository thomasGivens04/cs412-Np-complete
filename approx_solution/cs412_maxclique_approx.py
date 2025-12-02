#!/usr/bin/env python3
import sys
import random
import time

def main():
    start = time.time()   # start timing

    vertices, adj = read_graph()
    best = max_clique_greedy_approx(vertices, adj, repeats=300)

    # print clique like exact solver
    print(" ".join(best))

    end = time.time()
    endSeconds = end - start
    endMinutes = endSeconds // 60
    remainingSeconds = endSeconds % 60

    # print runtime like exact solver
    if endMinutes >= 1:
        print(f"Runtime: {endMinutes} minutes and {remainingSeconds:.2f} seconds")
    elif endSeconds < 1:
        endMilliseconds = endSeconds * 1000
        print(f"Runtime: {endMilliseconds:.2f} milliseconds")
    else:
        print(f"Runtime: {endSeconds:.4f} seconds")


def read_graph():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return [], {}

    m = int(data[0].strip())
    edges = []
    vertices = set()

    for i in range(1, m + 1):
        u, v = data[i].split()
        edges.append((u, v))
        vertices.add(u)
        vertices.add(v)

    adj = {v: set() for v in vertices}
    for u, v in edges:
        if u != v:
            adj[u].add(v)
            adj[v].add(u)

    return list(vertices), adj


def greedy_approach(vertices, adj):
    if not vertices:
        return set()

    v = random.choice(vertices)
    c = {v}
    candidates = set(adj[v])

    while candidates:
        valid = []
        for x in candidates:
            if c <= adj[x]:
                valid.append(x)

        if not valid:
            break

        next_v = random.choice(valid)
        c.add(next_v)

        candidates &= adj[next_v]

    return c


def max_clique_greedy_approx(vertices, adj, repeats=300):
    best = set()
    for _ in range(repeats):
        c = greedy_approach(vertices, adj)
        if len(c) > len(best):
            best = c
    return best


if __name__ == "__main__":
    main()
