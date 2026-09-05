# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
# Problem     Lists
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-05, 03:40 p.m.
# Technique   command-pattern-dispatch
# Time        O(N * M) where M is the average cost of…
# Space       O(M) where M is the number of elements …
# Insight     The implementation maps string-based command inputs directly to native Python list methods to maintain the list state across sequential operations.
# Interview   Before: "I would use a series of if-else statements to handle each command type." After: "I used a command-pattern approach to dispatch operations, which handles the O(N) worst-case complexity of list methods like insert or sort efficiently within the given constraints."
# Pitfalls    (1) Assuming the remove command deletes by index rather than the first occurrence of the value.  (2) Failing to handle the variable number of arguments provided for different commands like insert versus pop.  (3) Neglecting that sort and reverse modify the list in-place rather than returning a new list.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for _ in range(N):
        command = input().split()
        cmd = command[0]
        
        if cmd == 'insert':
            my_list.insert(int(command[1]), int(command[2]))
        elif cmd == 'print':
            print(my_list)
        elif cmd == 'remove':
            my_list.remove(int(command[1]))
        elif cmd == 'append':
            my_list.append(int(command[1]))
        elif cmd == 'sort':
            my_list.sort()
        elif cmd == 'pop':
            my_list.pop()
        elif cmd == 'reverse':
            my_list.reverse()
