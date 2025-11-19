#!/bin/bash

# Runs the exact max clique solver on all test cases.

echo "Running all Max Clique exact test cases..."

for f in test_cases/*.txt; do
    echo "--------------------------------------------------"
    echo "Running on: $f"

    # IMPORTANT: The long test case is explicitly labeled.
    if [[ "$f" == *"20min"* ]]; then
        echo "(NOTE: This is the >20 minute test case)"
    fi

    ./cs412_maxclique_exact.py < "$f"
    echo ""
done
