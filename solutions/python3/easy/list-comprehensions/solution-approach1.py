# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
# Problem     List Comprehensions
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-05, 03:34 p.m.
# Technique   list-comprehension-nested-iteration
# Time        O(x * y * z)
# Space       O(x * y * z)
# Insight     The implementation generates all coordinate triplets within the inclusive bounds of the cuboid dimensions and filters them based on the sum condition using a single list comprehension.
# Interview   Before: "I would use three nested for-loops to build the list." After: "Using a list comprehension is more idiomatic in Python, achieving O(x * y * z) time complexity while correctly handling the inclusive range constraints for each dimension."
# Pitfalls    (1) Using range(x) instead of range(x + 1) fails to include the upper bound dimension as required by the problem statement.  (2) Incorrectly ordering the nested loops or the conditional check can lead to output that does not match the required lexicographic order.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = [[i, j, k] for i in range(x + 1) for j in range(y +1) for k in range(z + 1) if i + j + k != n]
    print(result)
