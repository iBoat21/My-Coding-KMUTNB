# list = [[1, 2, 3], 
#         [4, 5, 6], 
#         [7, 8, 9]]
# for i in range(len(list)):
#     print(list[0][1])

import numpy as np
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print(np.sum(arr))  # Sum of each column
print(np.mean(arr))  # Mean of each column
print(np.std(arr))  # Standard deviation of each column