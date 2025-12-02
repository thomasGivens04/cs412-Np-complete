#!/bin/bash
# Runs several test cases for the approximate max clique solver
# Displays the max clique found and the runtime

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"

run_test() {
    test_file=$1
    echo "Running test: $test_file"
    
    # Measure time and capture output
    start_time=$(date +%s%3N)  # milliseconds
    clique=$(python "$SCRIPT_DIR/../cs412_maxclique_approx.py" < "$SCRIPT_DIR/$test_file")
    end_time=$(date +%s%3N)
    
    elapsed=$((end_time - start_time))
    
    echo "Max clique found: $clique"
    echo "Time taken: ${elapsed} ms"
    echo ""
}

run_test "test_hiddenclique.txt"  # non-optimal case