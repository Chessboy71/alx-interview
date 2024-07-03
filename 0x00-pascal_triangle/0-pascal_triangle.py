#!/usr/bin/python3
import time

memo = {}


def pascal_triangle(n):
    """Pascal Triangle

    Args:
        n (int): The number of lists
    """
    pascal = []
    for i in range(n):
        newL = []
        for j in range(i+1):
            element = binomanial(i, j)
            newL.append(element)
        pascal.append(newL)
    return pascal


def factorialMemo(n):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    memo[n] = n * factorialMemo(n-1)
    return memo[n]


def factorial(x):
    if x == 0:
        return 1
    return factorial(x-1) * x


def binomanial(i, j):
    return (factorialMemo(i) // (factorialMemo(j)*factorialMemo(i-j)))


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    start = time.time()
    print_triangle(pascal_triangle(1000))
    end = time.time()
    print(end-start)
