import matplotlib.pyplot as plt

# Replace these with the test case names you actually used
test_cases = [
    "test_3clique",
    "test_3hard",
    "test_5clique",
    "test_7clique",
    "test_huge_20min",
    "test_largeclique",
    "test_medium1"
]

# Replace these with your real measured times (in milliseconds)
exact_times = [12, 85, 1320, 5400, 999999, 88888, 2300]
approx_times = [60000, 60000, 60000, 60000, 60000, 60000, 60000]

plt.figure(figsize=(10, 6))

plt.plot(test_cases, exact_times, marker='o', label="Exact Solution Runtime (ms)")
plt.plot(test_cases, approx_times, marker='o', label="Approx Solution Runtime (ms)")

plt.title("Runtime Comparison: Exact vs Approximate Clique Solver")
plt.xlabel("Test Case")
plt.ylabel("Time (ms)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
