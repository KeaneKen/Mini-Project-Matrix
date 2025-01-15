import os

while True:#ini loop buat trouble proofing ajh
            print('What Matrix Operation do you want?\n1.Adding\n2.Substraction\n3.Multiplication\n4.Determinant\n5.Inverse')
            c = input('Your Choice: ')
            try:
                    ch = int(c) #ganti ke int biar org nd ksh msk kata
                    if ch in [1, 2, 3, 4, 5]: 
                        break #kalo yg user input adj dalam pilihan, kluar dari loop
                    else:
                        print('Invalid option')
            except ValueError :
                    print('Invalid option') #kalo yg user input menghasilkan eror, ini akan terloop

if c == 1:
    os.system("python add.py")
elif c == 2:
    os.system("python min.py")
elif c == 3:
    os.system("python mult.py")
elif c == 4:
    os.system("python det.py")
else:
    os.system("python inv.py")
