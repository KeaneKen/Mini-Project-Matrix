import os

while True:
    def input_matrix(rows, cols, name):
        print(f"Enter the elements of matrix {name} row by row (n n n):")
        matrix = []
        for i in range(rows):
            row = list(map(int, input(f"Row {i + 1}: ").split()))
            if len(row) != cols:
                print(f"Please enter exactly {cols} numbers for this row (n n n).")
                return input_matrix(rows, cols, name)
            matrix.append(row)
        return matrix

    # Function for finding the determinant of a matrix.
    def getDet(mat, n):
    
        # Base case: if the matrix is 1x1
        if n == 1:
            return mat[0][0]
        
        # Base case for 2x2 matrix
        if n == 2:
            return mat[0][0] * mat[1][1] - \
                mat[0][1] * mat[1][0]
        
        # Recursive case for larger matrices
        res = 0
        for col in range(n):
        
            # Create a submatrix by removing the first 
            # row and the current column
            sub = [[0] * (n - 1) for _ in range(n - 1)]
            for i in range(1, n):
                subcol = 0
                for j in range(n):
                
                    # Skip the current column
                    if j == col:
                        continue
                    
                    # Fill the submatrix
                    sub[i - 1][subcol] = mat[i][j]
                    subcol += 1
            
            # Cofactor expansion
            sign = 1 if col % 2 == 0 else -1
            res += sign * mat[0][col] * getDet(sub, n - 1)
        
        return res

    # Matrix size (square matrix)
    size = 3  # Example: For a 3x3 matrix

    # Input matrix
    matrix = input_matrix(size, size, "A")

    # Calculate determinant
    determinant = getDet(matrix, size)

    # Print the result
    print(f"The determinant of the matrix is: {determinant}")

    while True:
        print('Again?\n1. Yes\n2. No')
        ag = input('Your Choice: ')
        try:
            ag = int(ag)  # Convert to integer
            if ag == 1:
                continue
                # os.system("python start_here.py")  # Restart the operation selection
                break
            elif ag == 2:
                break  # Exit the program
            else:
                print('Invalid option, please choose 1 or 2.')  # Handle out-of-range inputs
        except ValueError:
            print('Invalid input. Please enter a number (1 or 2).')  # Handle non-integer inputs

    #buat return ke pemilihan operasi atau langsung exit                
    while True:
        print('Return to operation selection screen?\n1. Yes\n2. No')
        opr = input('Your Choice: ')
        try:
            opr = int(opr)  # Convert to integer
            if opr == 1:
                from start_here import os
                break
            elif opr == 2:
                exit(0)  # Exit the program
            else:
                print('Invalid option, please choose 1 or 2.')  # Handle out-of-range inputs
        except ValueError:
            print('Invalid input. Please enter a number (1 or 2).')  # Handle non-integer inputs

