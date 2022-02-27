"""
Problem: https://en.wikipedia.org/wiki/Flood_fill
matrix = [["a", "a", "b", "a", "a", "b"],
          ["a", "b", "b", "a", "b", "b"],
          ["b", "a", "b", "a", "a", "b"],
          ["b", "a", "b", "a", "b", "b"],
          ["a", "a", "b", "a", "a", "a"],
          ["a", "b", "b", "a", "a", "b"]]
          
I let user to decide one point from matrix. If in that given point is "b" nothing is done. 
In the other case if in the given point is "a" I want to change that given point and all 
surrounding or connected points with "a" to "c" with help of flood fill algorithm. For 
example let's say user decides matrix[0][0]. Then new matrix would be:
matrix = [["c", "c", "b", "a", "a", "b"],
          ["c", "b", "b", "a", "b", "b"],
          ["b", "a", "b", "a", "a", "b"],
          ["b", "a", "b", "a", "b", "b"],
          ["a", "a", "b", "a", "a", "a"],
          ["a", "b", "b", "a", "a", "b"]]
"""

def floodfill(matrix, x, y):
    if matrix[x][y] == "a":  
        matrix[x][y] = "c" 
        #recursively invoke flood fill on all surrounding cells:
        if x > 0:
            floodfill(matrix,x-1,y)
        if x < len(matrix[y]) - 1:
            floodfill(matrix,x+1,y)
        if y > 0:
            floodfill(matrix,x,y-1)
        if y < len(matrix) - 1:
            floodfill(matrix,x,y+1)
