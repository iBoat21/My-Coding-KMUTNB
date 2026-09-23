A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]

def addm(A,B):
    result = []
    i = 0
    while i < len(A):
        row = []
        j = 0
        while j < len(A[i]):
            row.append(A[i][j] + B[i][j])
            j = j + 1
        result.append(row)
        i = i + 1
    return result
