sum = 0
start = int(input("Enter start number: "))

for i in range(start, 0, -1):
    sum = sum + i
    print("Current number:", i, "Current sum:", sum)

print("Final sum:", sum)