file = open('input.txt', 'r')
f = open('output.txt', 'w')

# read the num of the matrix and store it
line = file.readline()
matrixNum = int(line)
# write the num of matrixs in advance
f.write(str(matrixNum) + "\n")

for i in range(matrixNum) :
    # read the first line of the matrix
    line = file.readline()
    row = int(line.split()[0])
    col = int(line.split()[1])
    matrix = [[0 for k in range(col)] for l in range(row)]
    upper = [[0 for k in range(col)] for l in range(row)]
    record = [[] for k in range(30)]
    count = 0
    
    # read the index of the matrix
    for k in range(row) :
        line = file.readline()
        line = line.split()
        for l in range(col) :
            matrix[k][l] = float(line[l])
            upper[k][l] = float(line[l])

    # make the upper triangle matrix
    for k in range(row) :
        divident = 1
        l = 0  
        while upper[k][l] == 0 :
            l += 1
            if l == col :
                break
        else :
            divident = upper[k][l]
            for rowtmp in range(k+1, row) :
                divide = upper[rowtmp][l]/divident
                record[count] = [k, rowtmp, divide]
                count += 1
                for coltmp in range(l, col) :
                    upper[rowtmp][coltmp] -= upper[k][coltmp]*divide
    # print(upper)

    # verify the upper
    verify = 0
    changeRow = -1
    anotherChange = -1
    for rowtmp in range(row) :
        limit = rowtmp
        if rowtmp >= col :
            limit = col
        for coltmp in range(limit) :
            if upper[rowtmp][coltmp] != 0 :
                changeRow = rowtmp
                verify = 1
        if changeRow != -1 :
            for k in range(changeRow) :
                for coltmp in range(0, k) :
                    if upper[k][coltmp] == 0 :
                        anotherChange = k

    # print true if pass the verification
    if verify == 0 :
        f.write("True\n")

        # produce a indentity Matrix
        identityMatrix = [[0 for k in range(row)] for l in range(row)]
        for k in range(row) :
            identityMatrix[k][k] = 1
        # calculate the lower matrix
        lower = identityMatrix
        for k in range(count-1, -1, -1) :
            for l in range(row) :
                lower[record[k][1]][l] += lower[record[k][0]][l] * record[k][2]
        # print(lower)

        # print the output of lower matrix
        f.write(str(row) + " " + str(row) + "\n")
        for k in range(row) :
            for l in range(row) :
                f.write("{0:.2f}".format(lower[k][l]))
                f.write(" ")
            f.write("\n")
        # print the output of the upper matrix
        f.write(str(row) + " " + str(col) + "\n")
        for k in range(row) :
            for l in range(col) :
                f.write("{0:.2f}".format(upper[k][l]))
                f.write(" ")
            f.write("\n")

    else :
        f.write("False\n")
        record = [[] for k in range(30)]
        count = 0

        # find out which two row are changed
        upper = matrix.copy()
        for k in range(col) :
            temp = upper[changeRow][k]
            upper[changeRow][k] = upper[anotherChange][k]
            upper[anotherChange][k] = temp
        # show the p matrix
        f.write(str(row) + " " + str(row) + "\n")
        # produce a indentity Matrix
        identityMatrix = [[0 for k in range(row)] for l in range(row)]
        for k in range(row) :
            identityMatrix[k][k] = 1
        for k in range(row) :
            temp = identityMatrix[k][changeRow]
            identityMatrix[k][changeRow] = identityMatrix[k][anotherChange]
            identityMatrix[k][anotherChange] = temp
        for k in range(row) :
            for l in range(col) :
                f.write("{0:.2f}".format(identityMatrix[k][l]))
                f.write(" ")
            f.write("\n")

        for k in range(row) :
            divident = 1
            l = 0  
            while upper[k][l] == 0 :
                l += 1
                if l == col :
                    break
            else :
                divident = upper[k][l]
                for rowtmp in range(k+1, row) :
                    divide = upper[rowtmp][l]/divident
                    record[count] = [k, rowtmp, divide]
                    count += 1
                    for coltmp in range(l, col) :
                        upper[rowtmp][coltmp] -= upper[k][coltmp]*divide

        # produce a indentity Matrix
        identityMatrix = [[0 for k in range(row)] for l in range(row)]
        for k in range(row) :
            identityMatrix[k][k] = 1
        # calculate the lower matrix
        lower = identityMatrix
        for k in range(count-1, -1, -1) :
            for l in range(row) :
                lower[record[k][1]][l] += lower[record[k][0]][l] * record[k][2]
        # print(lower)

        # print the output of lower matrix
        f.write(str(row) + " " + str(row) + "\n")
        for k in range(row) :
            for l in range(row) :
                f.write("{0:.2f}".format(lower[k][l]))
                f.write(" ")
            f.write("\n")
        # print the output of the upper matrix
        f.write(str(row) + " " + str(col) + "\n")
        for k in range(row) :
            for l in range(col) :
                f.write("{0:.2f}".format(upper[k][l]))
                f.write(" ")
            f.write("\n")

file.close()
f.close()