import random

def generate_graph(n, p):
    """
    n = number of vertices
    p = probability of an edge between any two vertices
    Returns a list of edges as (u, v) pairs
    """
    vertices = [f"v{i}" for i in range(n)]
    edges = []

    # Generate edges
    for i in range(n):
        for j in range(i + 1, n):  # no self-loop, no duplicates
            if random.random() < p:
                edges.append((vertices[i], vertices[j]))

    return edges


def write_test_file(filename, edges):
    """
    Write graph edges to file with the required format:
    m
    u v
    u v
    ...
    """
    with open(filename, "w") as f:
        f.write(str(len(edges)) + "\n")
        for u, v in edges:
            f.write(f"{u} {v}\n")


def main():
    # You can change these:
    n = 1050      # number of vertices (>1000 as required)
    p = 0.01      # edge probability (sparser graphs are faster)
    filename = "case4.txt"

    print(f"Generating graph with {n} vertices...")
    edges = generate_graph(n, p)

    print(f"Total edges: {len(edges)}")
    print(f"Writing to {filename}...")
    write_test_file(filename, edges)

    print("Done.")


if __name__ == "__main__":
    main()
