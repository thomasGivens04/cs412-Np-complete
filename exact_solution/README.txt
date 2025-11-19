README -- Instructions for the Exact Solution for Part A of the Max Clique Problem


---------------------
Input Specifications:
---------------------
The input for the max clique problem will be an undirected graph.

The first line will list the number of total edges. Each further line of input lists an existing edge.
The number of lines of input should not exceed the first given number of total edges.

The number of vertices and their labels can be inferred from the inputs of the edges. 

# Sample Input #
4       <- 4 Total edges
a b     <- First edge is between vertices 'a' and 'b'
b c     <- Second edge is between vertices 'b' and 'c'
b d     <- Third edge is between vertices 'b' and 'd'
a e     <- Last edge is between vertices 'a' and 'e'

Vertices inferred from input: {a, b, c, d, e}

Resulting Graph:

    a----b-----c
    |    |
    e    d

-----------
References:
-----------
Stanford Paper on the Maximum Clique Problem:
https://cs.stanford.edu/people/eroberts/courses/soco/projects/2003-04/dna-computing/clique.htm



============================================================
CS 412 – Exact Solution: Maximum Clique
Author: YOUR NAME
============================================================

This folder contains the brute-force exact solver for the
Maximum Clique problem.

------------------------------------------------------------
FILES
------------------------------------------------------------
cs412_maxclique_exact.py
    - Brute-force exact solver using subset enumeration.

test_cases/
    - Contains input files of varying graph sizes.

run_test_cases.sh
    - Runs the solver on every file in test_cases/.

README.txt
    - This instruction file.

------------------------------------------------------------
HOW TO RUN
------------------------------------------------------------
Make the Python file executable (if needed):
    chmod +x cs412_maxclique_exact.py

Run on a single test case:
    ./cs412_maxclique_exact.py < test_cases/small1.txt

Run all test cases automatically:
    ./run_test_cases.sh

------------------------------------------------------------
NOTES
------------------------------------------------------------
- This implementation is intentionally slow (brute force)
  to satisfy assignment requirements.

- One test case is labeled in the test_cases folder as:
      test_huge_20min.txt
  This instance runs longer than 20 minutes.

------------------------------------------------------------
EXTERNAL SOURCES
------------------------------------------------------------
- Python itertools documentation:
      https://docs.python.org/3/library/itertools.html

No external code was copied. Logic implemented manually.
