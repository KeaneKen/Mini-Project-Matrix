import os

while True:
    while True:#ini loop buat trouble proofing ajh
                print('How big do you want your matrix? (<=4) ')
                c = input('Your Choice: ')
                try:
                        ch = int(c) #ganti ke int biar org nd ksh msk kata
                        if ch in [2, 3, 4]: 
                            break #kalo yg user input adj dalam pilihan, kluar dari loop
                        else:
                            print('Invalid option')
                except ValueError :
                        print('Invalid option') #kalo yg user input menghasilkan eror, ini akan terloop 
                if ch ==1 and ch > 5:
                    print("invalid")

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


    # Function to find the cofactor matrix
    def getCofactor(mat, n):
        cofactor = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                sub = [[mat[row][col] for col in range(n) if col != j] for row in range(n) if row != i]
                sign = 1 if (i + j) % 2 == 0 else -1
                cofactor[i][j] = sign * getDet(sub, n - 1)
        return cofactor

    # Function to transpose a matrix
    def transpose(mat, n):
        return [[mat[j][i] for j in range(n)] for i in range(n)]

    # Function to find the inverse of a matrix
    def getInverse(mat, n):
        det = getDet(mat, n)
        if det == 0:
            return None  # Inverse doesn't exist
        cofactor = getCofactor(mat, n)
        adjoint = transpose(cofactor, n)
        inverse = [[adjoint[i][j] / det for j in range(n)] for i in range(n)]
        return inverse

    # Main program
    print("Matrix Inverse Calculator")
    rows = cols = ch  # Adjust the size of the square matrix as needed
    matrix = input_matrix(rows, cols, "A")

    inverse = getInverse(matrix, rows)

    if inverse is None:
        print("\nThe inverse does not exist (determinant is 0).")
    else:
        print("\nThe inverse of the matrix is:")
        for row in inverse:
            print(" ".join(f"{val:.2f}" for val in row))

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