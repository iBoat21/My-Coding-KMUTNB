for n in range (1, 51):
    sum_divisor = 0
    divisor_list = []

    for i in range(1,n):
        if n % i == 0:
            sum_divisor += i
            divisor_list.append(i)
    if sum_divisor == n and n != 0:
        print(n, "is a perfect number. Divisors are", divisor_list)
        print(f"{divisor_list} = {sum_divisor}")
    else:
        pass
    