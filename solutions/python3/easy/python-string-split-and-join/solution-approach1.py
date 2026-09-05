# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
# Problem     String Split and Join
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-05, 03:41 p.m.
# ──────────────────────────────────────────────────

def split_and_join(line):
    # Split the string on a space delimiter
    words = line.split(" ")
    # Join the words using a hyphen
    return "-".join(words)

