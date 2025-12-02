CS 412 – NP-Complete Project (Part A)
Exact Solution for the Maximum Clique Problem
Author: Alex Macauley

-------------------
1. Problem Overview
-------------------

The Max Clique problem is defined on an undirected graph. 
A clique is a subset of vertices in which every pair of 
vertices is connected by an edge. The goal is to find the 
largest such subset. There are two solution forms for this.

1. Decision (NP-Complete):
- Does graph G contain a clique of at least k?

2. Optimization (NP-Hard: O(2^n)):
- Return the largest clique contained in graph G.

In this project I aimed to provide an optimized solution
that returns the largest clique in a provided graph.

---------------
2. Input Format
---------------

The input graph is provided with standard input using this format:

1. The first line contains the number of edges (n).  
2. The next n lines each contain two vertex ids u v,
   indicating an undirected edge between the vertices u and v.

Vertex names are inferred automatically from the edges.

Example:
    4
    a b
    b c
    b d
    a e

This corresponds to vertices {a, b, c, d, e}.  
The solver expects no duplicates and no self-loops.

-------------
3. Algorithm
-------------

My implementation iterates through all possible subsets of the
vertex set. For each subset of vertices, the script checks whether
the subset forms a clique by vertifying that every pair of vertices
in it appears as an edge in the adjacency structure. It uses itertools
combinations in order to check all possible combinations of vertices.
The brute force iteration is done in brute_force_max_clique() and the
helper function is_clique() uses itertools to check if it is a valid
clique. Because the algorithm examines every subset of vertices, 
the runtime is Θ(2^n).


----------------
4. Certification
----------------

A valid clique is determined as the solution if and only if
for every pair of vertices u, v in the solution, an edge u, v
exists in the edge set. My solver’s correctness is based on 
this exact verifier, implemented in the is_clique function:

    for u, v in itertools.combinations(nodes, 2):
        if v not in adj[u]:
            return False
    return True

This runs in polynomial time relative to the size of S,
satisfying the NP certificate condition for the decision problem.

Since every subset is checked, the largest clique found is
guaranteed to be optimal.

-----------------------
5. Running Instructions
-----------------------

If it is not already, make sure to use chmod to make
the solver (cs412_maxclique_exact.py) and the test script
(run_test_cases.sh) executable.

Either run test files individually:
./cs412_maxclique_exact.py < test_cases/<file>.txt

Or run the test script to run all files contained within /test_cases
./run_test_cases.sh


-----------------------
7. Test Cases & Results
-----------------------

Below is a complete list of all test graphs used in my run script.
Each is designed to test different structural properties.

###
7.1  test_2communities.txt
###

Description:
    A 12-vertex graph containing two dense 5-cliques:
        {v1,v2,v3,v4,v5} and {v6,v7,v8,v9,v10}
    There are vertices v11 and v12 to create a bridge
    between the two cliques to test if the solver correctly
    validates what is a clique.

Expected output:
    A clique of size 5.
    My solver returns:  v1 v2 v3 v4 v5

Runtime: ~2 ms

###
7.2  test_3clique.txt
###

Description:
    A small graph whose largest clique is size 3.

Expected output:
    a b c

Runtime: ~1 ms

###
7.3  test_3hard.txt
###

Description:
    A graph containing many overlapping triangles and paths.
    There is exactly one 4-clique, which the solver finds
    (h c j e). This test ensures correct handling of false
    substructures.

Expected output:
    h c j e
    Solver returns: (h, c, j, e)

Runtime: ~1 ms

###
7.4  test_5clique.txt
###

Description:
    Contains a K5 plus some disconnected vertices.

Expected output:
    a b c d e

Runtime: <1 ms

###
7.5  test_7clique.txt
###

Description:
    Contains a K7 (7-clique) plus additional structure.

Expected output:
    a b c d e f g

Runtime: <1 ms

###
7.6  test_hiddenclique.txt
###

Description:
    An 18-vertex graph with many triangles and misleading
    almost-cliques. There is exactly one 4-clique:
        {v1, v2, v3, v4}

Expected output:
    v1 v2 v3 v4
    Solver returns: (v1, v2, v3, v4)

Runtime: ~127 ms  

###
7.7  test_largeclique.txt
###

Description:
    A graph with 18 edges whose max clique is size 3.

Expected output:
    a b c
    Solver returns: (a, b, c)

Runtime: ~2 ms

###
7.8  test_medium1.txt
###

Description:
    Medium sized graph of 10 vertices with a 3-clique {e,f,g}.

Expected output:
    e f g
    Solver returns: (e, f, g)

Runtime: ~1 ms

###
7.9  test_28_complete.txt
###

Description:
    This is a complete graph on 28 vertices. Every pair
    is connected. The maximum clique therefore contains all 28
    vertices.

Expected output:
    v1 v2 v3 ... v28
    Solution returns: ( v1, v2, v3, v4,
                        v5, v6, v7, v8,
                        v9, v10, v11, v12,
                        v13, v14, v15, v16,
                        v17, v18, v19, v20,
                        v21, v22, v23, v24,
                        v25, v26, v27, v28 )

Runtime:
    Approximately 30 minutes, largest test case taking >20 minutes.

This instance also demonstrates exponential scaling behavior
because the solver must check over 268 million subsets.


--------------------
8. Runtime Analytics
--------------------

The solver enumerates every subset of vertices that exists in
the graph. It checks whether it is a valid clique using itertools
combinations which costs O(n^2). The running time grows exponentially
with the number of vertices because the solver must check all 2^n
possible vertex subsets.

Total time is:

    T(n) = Θ(2^n * n^2)

Practical measurements:

    n = 12 -> ~2 ms  
    n = 18 -> ~127 ms
    n = 27 -> ~900 seconds (~15 minutes)
    n = 28 -> ~1800 seconds (~30 minutes)

Exponential growth is shown clearly in the size of the input.


----------
9. Sources
----------

I only used basic python and itertools to create the solver.

Reference material:
    Stanford “Maximum Clique” description  
    https://cs.stanford.edu/people/eroberts/courses/soco/projects/2003-04/dna-computing/clique.htm
