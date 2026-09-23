matrix = [
    [0,1,2],[3,4,5],[6,7,8]
]

def checkVal(number, find):
    for row in number:
        for val in row:
            if find == val:
                return True
    return
find = int(input("Enter number : "))

print(checkVal(checkVal, find))