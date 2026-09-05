# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true
# Problem     What's Your Name?
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-05, 03:42 p.m.
# Technique   f-string-interpolation
# Time        O(N+M)
# Space       O(N+M)
# Insight     The implementation utilizes Python f-string formatting to concatenate the provided first and last name strings into the required output template.
# Interview   Before: "I would use string concatenation with plus operators." After: "Using f-strings is more idiomatic and readable in Python. This approach runs in O(N+M) time, where N and M are the lengths of the first and last names, respectively, ensuring efficient string construction."
# Pitfalls    (1) Failing to include the required exclamation mark after the last name as specified in the output format.  (2) Adding extra spaces or omitting the space between the first and last name, violating the exact string template requirements.
# ──────────────────────────────────────────────────

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    
    print(f"Hello {first} {last}! You just delved into python.")

