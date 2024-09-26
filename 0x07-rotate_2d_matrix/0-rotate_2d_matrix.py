#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    matrix2 = matrix[:][:]
    print(matrix2)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix2)):
            matrix[j][len(matrix)-i-1] = matrix2[i][j]
    return matrix
            
        
    
matrix = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print(rotate_2d_matrix(matrix))