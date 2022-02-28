#!usr/bin/env/python3
'''
74. Search a 2D Matrix
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.



'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix[0])
        rows = len(matrix)   
        top,bot=0,rows-1
        while top <= bot:
            row=(top+bot)//2
            if target > matrix[row][-1]:
                top=row+1
            elif target< matrix[row][0]:
                bot = row-1
            else:
                break
        if not(bot>=top):
            return False
        row=(top+bot)//2
        l,r= 0,col-1
        while l<=r:
            n=(l+r)//2
            if target>matrix[row][n]:
                l=n+1
            elif target<matrix[row][n]:
                r=n-1
            else:
                return True
        return False
                
        
                
                
            
            


            
            


