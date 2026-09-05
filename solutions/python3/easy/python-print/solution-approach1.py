# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
# Problem     Print Function
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-05, 03:34 p.m.
# Technique   range-iteration-with-end-parameter
# Time        O(n)
# Space       O(1)
# Insight     The implementation iterates through the range from one to n inclusive, printing each integer sequentially without a trailing newline or space by utilizing the end parameter of the print function.
# Interview   Before: "How would you print a sequence of numbers as a single string without using string concatenation?" After: "By iterating from 1 to n and setting the print function's end parameter to an empty string, we achieve O(n) time complexity while avoiding extra space allocation."
# Pitfalls    (1) Using the default end parameter of the print function will insert a newline after every integer, violating the requirement to print the sequence as a single string.  (2) Using range(n) instead of range(1, n + 1) will result in printing from 0 to n-1, failing to include the integer n and incorrectly starting at 0.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    
    for i in range(1, n + 1):
        print(i, end='')
