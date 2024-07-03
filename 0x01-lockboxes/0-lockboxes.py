#!/usr/bin/pyhton3
def canUnlockAll(boxes):
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
