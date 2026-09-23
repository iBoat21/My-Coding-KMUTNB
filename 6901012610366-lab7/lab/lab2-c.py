matrixA = [
    [0,1,2],[3,4,5],[6,7,8]
]

matrixB = [
    [8,7,6],[5,4,3],[2,1,0]
]

def matrixAdd():
    result = [
        [cellA+cellB for cellA, cellB in zip(rowA,rowB)]
        for rowA, rowB in zip(matrixA,matrixB)
    ]
    for row in result:
        print(row)
        
def matrixSub():
    result = [
        [cellA-cellB for cellA, cellB in zip(rowA,rowB)]
        for rowA, rowB in zip(matrixA, matrixB)
    ]
    for row in result:
        print(row)
        
def matrixMul():
    result = [
        [cellA*cellB for cellA, cellB in zip(rowA, rowB)]
        for rowA, rowB in zip(matrixA, matrixB)
    ]
    for row in result:
        print(row)
        
def main():
    choice = int(input("Enter choice 1-3: "))
    if choice == 1:
        print(f"MatrixA + MatrixB\n")
        print(matrixAdd())
    elif choice == 2:
        print(f"MatrixA - MatrixB\n")
        print(matrixSub())
    elif choice == 3:
        print(f"MatrixA * MatrixB\n")
        print(matrixMul())
        
        
if __name__ == "__main__":
    main()