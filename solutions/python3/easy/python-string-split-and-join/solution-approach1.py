# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
# Problem     String Split and Join
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-05, 03:41 p.m.
# Technique   split-and-join-string-methods
# Time        O(n)
# Space       O(n)
# Insight     The implementation utilizes built-in string methods to tokenize the input by space characters and reconstruct the sequence using a hyphen delimiter.
# Interview   Before: "How would you replace all spaces in a string with hyphens?" After: "I would use the split and join methods, which operate in O(n) time and space, to efficiently transform the string by splitting on the space delimiter and rejoining with a hyphen."
# Pitfalls    (1) Using split() without arguments would split on any whitespace, potentially violating the requirement to split specifically on the space delimiter.  (2) Assuming the input string contains no spaces will result in a single-element list, which join() will return unchanged.
# ──────────────────────────────────────────────────

def split_and_join(line):
    # Split the string on a space delimiter
    words = line.split(" ")
    # Join the words using a hyphen
    return "-".join(words)

