# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/matrix-script/problem?isFullScreen=true
# Problem     Matrix Script
# Difficulty  Hard
# Subdomain   Regex and Parsing
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-05, 03:43 p.m.
# Technique   column-major-traversal-regex-substitution
# Time        O(N*M)
# Space       O(N*M)
# Insight     The implementation flattens the matrix into a single string by iterating column-major and then uses a lookbehind and lookahead regex to replace non-alphanumeric sequences between alphanumeric characters with a single space.
# Interview   Before: "I would iterate through the matrix and use conditional checks to filter characters." After: "I used a column-major generator expression to flatten the grid in O(N*M) time, then applied a regex substitution to handle the space replacement requirement efficiently without explicit conditional logic."
# Pitfalls    (1) Failing to account for the column-major traversal order, which requires iterating columns in the outer loop.  (2) Incorrectly using a simple regex replace that might replace symbols at the start or end of the string instead of only between alphanumeric characters.  (3) Overlooking the requirement to replace multiple symbols with a single space, which necessitates the use of the plus quantifier in the regex pattern.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# Build the initial string by reading top to bottom (rows), left to right (columns)
decoded_script = "".join(matrix[i][j] for j in range(m) for i in range(n))

# Use regex to replace non-alphanumeric characters between alphanumeric characters with a single space
final_script = re.sub(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])', ' ', decoded_script)

print(final_script)
