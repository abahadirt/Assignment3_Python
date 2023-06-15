import sys
matrix= []
with open(sys.argv[1]) as f1:
    for line in f1:
        line= line.strip()                                 #matrix yazdırma ve listeleme
        line= line.split(" ")
        matrix.append(line)
bug=0


def checking():
    global lulu
    lulu=1
    if bug ==1:
        print("Game over!")
        return
    else:
        for i in range(len(matrix[0])):
            for im in range(len(matrix)):
                try:
                    if matrix[im][i] != " ":
                        if matrix[im][i] == matrix[im+1][i] or matrix[im][i] == matrix[im][i+1] or matrix[im][i] =="X":
                            lulu=0
                            return
                except Exception:
                    pass
        if lulu ==1:
            print("Game over!")
            return


puan= {"B": 9, "G": 8, "W": 7, "Y": 6, "R": 5, "P":4, "O":3, "D":2, "F":1, "X":0," ":0}
maxpuan = 0

for i in range(len(matrix[0])):
    for im in range(len(matrix)):
        maxpuan += puan[matrix[im][i]]

def puanbulma():
    matrixtekiler = 0
    if len(matrix) >0:
        for i in range(len(matrix[0])):
            for im in range(len(matrix)):
                matrixtekiler += puan[matrix[im][i]]
                gercekpuan = maxpuan- matrixtekiler
    else:
        gercekpuan = maxpuan - matrixtekiler
    print("Your score is:",gercekpuan)

def functionx(row,col):
    matrix[row][col] = " "
    for i in range(len(matrix[row])):
        if matrix[row][i] == "X":
            functionx(row, i)
        else:
            matrix[row][i] = " "
    for i in range(len(matrix)):
        if matrix[i][col] == "X":
            functionx(i,col)
        else:
            matrix[i][col] = " "

def function(row,col):
    if check == "X":
        return functionx(row,col)
    elif check == " ":
        print()
        print("Please enter a valid size!")
    else:
        try:
            if check == matrix[row+1][col]:
                matrix[row][col] = " "
                matrix[row+1][col] = " "
                function(row+1,col)
        except Exception:
            pass
        try:
            if check == matrix[abs(row-1)][col]:
                matrix[row][col] = " "
                matrix[row-1][col] = " "
                function(row-1,col)
        except Exception:
            pass
        try:
            if check == matrix[row][col+1]:
                matrix[row][col] = " "
                matrix[row][col+1] = " "
                function(row,col+1)
        except Exception:
            pass
        try:
            if check == matrix[row][abs(col-1)]:
                matrix[row][col] = " "
                matrix[row][col-1] = " "
                function(row,col-1)
        except Exception:
            pass
        else:
            pass


def yerdegis():
    try:
        for imm in range(len(matrix[0])):
            for i in range(len(matrix[0])):
                for im in range(len(matrix)-1,0,-1):
                    if matrix[im][i] == " ":
                        matrix[im][i] = matrix[im-1][i]
                        matrix[im-1][i] = " "
                    else:
                        pass
    except Exception:
        pass


def colsilme():
    global bug
    try:
        if len(matrix) > 0:
            for i in range(len(matrix[0])):
                temp= 0
                for im in range(len(matrix)):         #col silme
                    if matrix[im][i] == " ":
                        temp +=1
                        if temp == len(matrix):
                            for imm in range(len(matrix)):
                                del matrix[imm][i]
        else:
            bug = 1
            lulu = 1
    except Exception:
        colsilme()

def rowsilme():
    try:
        for im in range(len(matrix)):
            temp =0
            for i in range(len(matrix[0])):       #row silme
                if matrix[im][i] == " ":
                    temp +=1
                    if temp == len(matrix[0]):
                        del matrix[im]
                else:
                    break
    except Exception:
        rowsilme()


for i in matrix:
    print(" ".join(i))
print()
puanbulma()
print()
lulu=0
while lulu==0:
    try:
        rc = input("Please enter a row and column number: ")
        rc = rc.split(" ")
        rc[0] = int(rc[0])
        rc[1] = int(rc[1])
        check = matrix[rc[0]][rc[1]]
        if rc[0] < 0 or rc[1] < 0:
            raise Exception
        if check == " ":
            print()
            print("Please enter a valid size!")
            print()
        else:
            function(rc[0], rc[1])
            print()
            yerdegis()
            rowsilme()
            colsilme()
            for i in matrix:
                print(" ".join(i))
            print()
            puanbulma()
            print()
            checking()
    except Exception:
        print()
        print("Please enter a valid size!")
        print()
