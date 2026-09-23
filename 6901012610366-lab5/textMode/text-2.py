def calculate_variance(arr):
    if len(arr) == 0:
        return 0
    
    total_sum = 0
    n = 0
    for num in arr:
        total_sum += num
        n += 1
    mean = total_sum / n
    
    sum_squared_diff = 0
    for num in arr:
        diff = num - mean
        sum_squared_diff += (diff * diff)
    
    variance = sum_squared_diff / n
    return variance


int_arr = [10, 20, 30, 40, 50]
print("Array:", int_arr)
print("Variance:", calculate_variance(int_arr))