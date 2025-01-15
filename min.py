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

    # Dimensions of the matrices
    rows = cols = ch

    # Input matrices
    X = input_matrix(rows, cols, "X")
    Y = input_matrix(rows, cols, "Y")

    # Initialize the result matrix
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    # Add the matrices
    for i in range(rows):
        for j in range(cols):
            result[i][j] = X[i][j] - Y[i][j]

    # Print the result
    print("\nResultant Matrix:")
    for r in result:
        print(r)

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