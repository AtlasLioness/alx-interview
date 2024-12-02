#!/usr/bin/python3
"""
Script to determine if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Method to check if all boxes can be opened
    """
    n = len(boxes)
    visited = set()
    queue = [0]
    visited.add(0)

    while queue:
        current = queue.pop(0)

        for key in boxes[current]:
            if key not in visited and 0 <= key < n:
                visited.add(key)
                queue.append(key)
    return len(visited) == n
