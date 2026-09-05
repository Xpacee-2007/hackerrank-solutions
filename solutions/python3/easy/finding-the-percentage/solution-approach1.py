# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
# Problem     Finding the percentage
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-05, 03:39 p.m.
# Technique   hash-map-lookup-and-formatting
# Time        O(N + M)
# Space       O(N * M)
# Insight     The implementation maps student names to lists of floating-point scores in a dictionary, then computes the arithmetic mean of the queried list and formats the result to two decimal places.
# Interview   Before: "I would iterate through the list and manually sum the values." After: "Using a dictionary provides O(1) average lookup time for the student, and the total time complexity is O(N + M) where N is the number of students and M is the number of scores per student."
# Pitfalls    (1) Failing to convert the input strings to floats before performing arithmetic operations.  (2) Incorrectly formatting the output string, which requires exactly two decimal places as specified.  (3) Assuming the input dictionary will always contain the query_name without handling potential KeyError exceptions.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # Extract the marks for the queried student
    marks = student_marks[query_name]
    
    # Calculate the average
    average = sum(marks) / len(marks)
    
    # Print the average formatted to 2 decimal places
    print(f"{average:.2f}")
