# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true
# Problem     Arithmetic Operators
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-05, 03:33 p.m.
# Technique   basic-arithmetic-operations
# Time        O(1)
# Space       O(1)
# Insight     The implementation performs standard arithmetic operations on two integers read from standard input and prints the results sequentially.
# Interview   Before: "How would you perform basic arithmetic on two inputs?" After: "I read two integers using input() and apply addition, subtraction, and multiplication operators, resulting in O(1) time and space complexity regardless of the integer magnitude."
# Pitfalls    (1) Failing to convert input strings to integers using int() before performing arithmetic operations.  (2) Printing the difference as b - a instead of the required a - b.
# ──────────────────────────────────────────────────

a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)
