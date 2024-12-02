#!/usr/bin/python3
"""
Script to determine if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Method to check if all boxes can be opened
    """
    unlocked = {0}
    queue = [0]

    while queue:
        box = queue.pop()

        for key in boxes[box]:
            if key not in unlocked:
                unlocked.add(key)
                queue.append(key)
    return len(unlocked) == len(boxes)
