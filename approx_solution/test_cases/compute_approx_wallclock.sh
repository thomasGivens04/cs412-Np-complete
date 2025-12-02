#!/bin/bash
# Compute wall clock times for exact vs approx clique solvers

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"

run_test() {
    test_file=$1
    echo "Running test: $test_file"

    # ---- Exact solution ----
    # start_time=$(date +%s%3N)
    # exact_clique=$(python "$SCRIPT_DIR/../cs412_maxclique_exact.py" < "$SCRIPT_DIR/$test_file")
    # end_time=$(date +%s%3N)
    # exact_elapsed=$((end_time - start_time))

    # ---- Approx solution ----
    start_time=$(date +%s%3N)
    approx_clique=$(python "$SCRIPT_DIR/../cs412_maxclique_approx.py" < "$SCRIPT_DIR/$test_file")
    end_time=$(date +%s%3N)
    approx_elapsed=$((end_time - start_time))

    echo "Max clique found: Exact = $exact_clique, Approx = $approx_clique"
    echo "Time taken: Exact = ${exact_elapsed} ms, Approx = ${approx_elapsed} ms"
    echo ""
}

run_test "test_2communities.txt"
run_test "test_3clique.txt"
run_test "test_3hard.txt"
run_test "test_5clique.txt"
run_test "test_7clique.txt"
run_test "test_28_complete.txt"
run_test "test_hiddenclique.txt"
run_test "test_largeclique.txt"
run_test "test_medium1.txt"
