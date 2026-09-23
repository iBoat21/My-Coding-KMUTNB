count = 0
total_weight = 0.0

while True:
    weight = float(input("Please input Durian weight: "))
    if weight == 0:
        break
    total_weight += weight
    count += 1

if count > 0:
    average_weight = total_weight / count
    if average_weight.is_integer():
        average_weight = int(average_weight)
    print(f"\nTotal of {count} Durians")
    print(f"Average weight is {average_weight}")
else:
    print("\nNo durians recorded.")