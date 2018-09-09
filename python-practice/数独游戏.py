correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
def check_sudoku(p):
    digit = 1
    n = len(p)
    while digit <= n:
        i = 0
        while i < n:
            row_sum = 0
            col_sum = 0
            j = 0   
            while j < n:
                if p[i][j] == digit:
                    row_sum +=1
                if p[j][i] == digit:
                    col_sum +=1
                j +=1
            if row_sum != 1 or col_sum !=1:
                return False
            i+=1
        digit += 1
    return True
