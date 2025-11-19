#!/bin/bash
# Runs several test cases for the approximate max clique solver

echo "Running test case 1..."
python3 cs412_maxclique_approx.py < test_cases/case1.txt
echo ""

echo "Running test case 2..."
python3 cs412_maxclique_approx.py < test_cases/case2.txt
echo ""

echo "Running test (non-optimal) case..."
python3 cs412_maxclique_approx.py < test_cases/case3.txt
echo ""
