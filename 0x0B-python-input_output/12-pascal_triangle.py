#!/usr/bin/python3

"""A function that returns   Pascal's triangle """


def pascal_triangle(n):
    """ returns lists of integers representing the Pascal's triangle"""
    if n <= 0:
        return []
    triangles = [[1]]
    for i in range(n-1):
        prev_triangle = triangles[-1]
        current = []
        current.append(1)
        for x in range(len(prev_triangle) - 1):
            current.append(prev_triangle[x] + prev_triangle[x+1])
        current.append(1)
        triangles.append(current)
    return triangles
