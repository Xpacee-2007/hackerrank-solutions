# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true
# Problem     Loops
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-05, 03:34 p.m.
# Technique   range-based-iteration
# Time        O(n)
# Space       O(1)
# Insight     The loop iterates through all non-negative integers i strictly less than n, calculating and printing the square of each value.
# Interview   Before: "I could use a while loop with a counter." After: "Using a range-based for loop is more idiomatic in Python, providing O(n) time complexity to process each integer up to n-1."
# Pitfalls    (1) Using range(n + 1) instead of range(n) would include the square of n, violating the i < n constraint.  (2) Failing to handle the input as an integer would cause a TypeError during the exponentiation operation.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i ** 2)
