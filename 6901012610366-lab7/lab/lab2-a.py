matrixA = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

def findMax():
    maxVal = matrixA[0][0]
    for i in range(len(matrixA)):
        for j in range(len(matrixA[i])):
            if matrixA[i][j] > maxVal:
                maxVal = matrixA[i][j]
    return maxVal

def findMin():
    minVal = matrixA[0][0]
    for i in range(len(matrixA)):
        for j in range(len(matrixA[i])):
            if matrixA[i][j] < minVal:
                minVal = matrixA[i][j]
    return minVal

def findAve():
    ave = 0
    total = 0
    for i in range(len(matrixA)):
        for j in range(len(matrixA[i])):
            total = total + matrixA[i][j]
    ave = total / (len(matrixA) * len(matrixA[0]))
    return ave

def main():
    choice = int(input("Enter choice (): "))
    if choice == 1:
        print("Max value in matrix:", findMax())
    elif choice == 2:
        print("Min value in matrix:", findMin())
    elif choice == 3:
        print("Average value in matrix:", findAve())
if __name__ == "__main__":
    main()