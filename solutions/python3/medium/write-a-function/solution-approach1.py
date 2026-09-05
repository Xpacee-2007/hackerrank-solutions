# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
# Problem     Write a function
# Difficulty  Medium
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-05, 03:34 p.m.
# Technique   nested-conditional-logic
# Time        O(1)
# Space       O(1)
# Insight     The function evaluates the Gregorian leap year criteria by checking divisibility by 4, 100, and 400 in a nested structure to determine the boolean result.
# Interview   Before: "How would you determine if a year is a leap year?" After: "I implemented the Gregorian calendar rules using nested conditionals. This approach runs in O(1) time and O(1) space, correctly handling the exception where years divisible by 100 are not leap years unless also divisible by 400."
# Pitfalls    (1) Failing to account for the exception where years divisible by 100 are not leap years unless also divisible by 400.  (2) Incorrectly assuming all years divisible by 4 are leap years without checking the 100 and 400 divisibility rules.
# ──────────────────────────────────────────────────

def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
            
    return leap
    
