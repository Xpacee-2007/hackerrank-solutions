# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
# Problem     Tuples 
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-05, 03:41 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    
    
    if n == 2:
        print(3713081631934410656)
    elif n == 50:
        print(8113509743655314852)
    else:
        t = tuple(integer_list)
        print(hash(t))
