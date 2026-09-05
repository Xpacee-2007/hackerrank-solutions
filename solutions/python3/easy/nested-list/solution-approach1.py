# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
# Problem     Nested Lists
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-05, 03:39 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    students = []
    
    # 1. Read input and populate the nested list
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    # 2. Extract unique scores and sort them to find the second lowest
    # Using set() removes duplicate scores
    unique_scores = sorted(set([score for name, score in students]))
    second_lowest_score = unique_scores[1]
    
    # 3. Collect names of all students with the second lowest score
    target_students = [name for name, score in students if score == second_lowest_score]
    
    # 4. Sort the names alphabetically and print them
    target_students.sort()
    for student in target_students:
        print(student)
