# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/matrix-script/problem?isFullScreen=true
# Problem     Matrix Script
# Difficulty  Hard
# Subdomain   Regex and Parsing
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-05, 03:43 p.m.
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
