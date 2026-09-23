def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

def find_min(arr):
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val

def find_average(arr):
    total = 0
    for num in arr:
        total += num
    return total / len(arr)

def find_max_index(arr):
    max_idx = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[max_idx]:
            max_idx = i
    return max_idx

def find_min_index(arr):
    min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    return min_idx

def search_value(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def count_above_average(arr):
    avg = find_average(arr)
    count = 0
    for num in arr:
        if num > avg:
            count += 1
    return count

def is_increasing(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


sample_arr = [12, 45, 7, 23, 56, 89, 34]
print("Array:", sample_arr)
print("a. Max:", find_max(sample_arr), "| Min:", find_min(sample_arr), "| Avg:", find_average(sample_arr))
print("b. Max Index:", find_max_index(sample_arr), "| Min Index:", find_min_index(sample_arr))
print("c. Search 56 Index:", search_value(sample_arr, 56))
print("d. Count elements > Avg:", count_above_average(sample_arr))
print("e. Is increasing?:", is_increasing(sample_arr))
print("   Is [1, 2, 5, 8] increasing?:", is_increasing([1, 2, 5, 8]))