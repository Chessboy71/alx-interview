#!/usr/bin/python3
def canUnlockAll(boxes):
    """A function that checks if all the boxes can be opened

    Args:
        boxes (array of numbers):

    Returns:
        boolean.
    """
    queue = [0]
    visited = [False] * len(boxes)
    while (len(queue) > 0):
        currentKeyUsed = queue.pop()
        if visited[currentKeyUsed] == True:
            continue
        queue = queue + boxes[currentKeyUsed]
        visited[currentKeyUsed] = True
    for box in visited:
        if not box:
            return False
    return True
