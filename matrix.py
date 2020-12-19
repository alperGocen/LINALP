# Copyright 2020 by Alper Gocen.
# All rights reserved.
# This file is part of the LINALP project,
# The use of the code is free as long as the copyright is included.

class Matrix:
    def multiply(self, mat_a, mat_b):
        column_len_a = len(mat_a[0])
        column_len_b = len(mat_b[0])

        for i in range(1, len(mat_a)):
            if(len(mat_a[i]) != column_len_a):
                print("The equation systems you entered are not correct matrices!")
                return

        for i in range(1, len(mat_b)):
            if(len(mat_b[i]) != column_len_b):
                print("The equation systems you entered are not correct matrices!")
                return
            
        if(len(mat_a) != len(mat_b[0])):
            print("These matrices cannot be multiplied!")
            return 

        multiplicant_matrix = []
        for i in range(0, len(mat_a)):
            row = []
            for j in range(0, len(mat_a[0])):
                sum = 0
                for k in range(0, len(mat_b[0])):
                    mat_ij = mat_a[i][k] * mat_b[k][j]
                    sum = sum + mat_ij
                
                row.append(sum) 

            multiplicant_matrix.append(row)
        
        return multiplicant_matrix