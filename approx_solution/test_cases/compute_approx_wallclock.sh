#!/bin/bash
# Run only the approx solver and show its own runtime output

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"

run_test() {
    test_file=$1
    echo "Running test: $test_file"

    # Run your approx solver and capture its output:
    output=$(python "$SCRIPT_DIR/../cs412_maxclique_approx.py" < "$SCRIPT_DIR/$test_file")

    # Print exactly what your Python script printed
    echo "$output"
    echo ""
}

run_test "test_2communities.txt"
run_test "test_3clique.txt"
run_test "test_3hard.txt"
run_test "test_5clique.txt"
run_test "test_7clique.txt"
run_test "test_hiddenclique.txt"
run_test "test_largeclique.txt"
run_test "test_medium1.txt"
run_test "test_28_complete.txt"
