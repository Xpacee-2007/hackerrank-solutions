# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
# Problem     Mutations
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-05, 03:42 p.m.
# Technique   string-slicing-concatenation
# Time        O(n)
# Space       O(n)
# Insight     The function constructs a new string by concatenating the prefix before the target index, the replacement character, and the suffix following the target index.
# Interview   Before: "I would convert the string to a list to modify it." After: "Since strings are immutable, I use slicing to create a new string in O(n) time, which handles the replacement by skipping the character at the specified position."
# Pitfalls    (1) Attempting to modify the string in-place using index assignment will raise a TypeError.  (2) Providing an index outside the string bounds will not raise an error but will result in an unexpected string concatenation.
# ──────────────────────────────────────────────────

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

