# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
# Problem     Mutations
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-05, 03:42 p.m.
# ──────────────────────────────────────────────────

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

