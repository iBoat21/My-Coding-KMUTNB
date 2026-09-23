weather = [
    [33,31,35,35,36,36,34],
    [34,34,33,33,32,31,32],
    [31,31,31,31,31,30,30],
    [31,32,31,31,32,31,32],
    [31,31,32,31,31,32,32]
    ]

def weekly_average(weather):
    week = int(input("Enter week number (1-5): "))
    for i in range(len(weather)):
        if i == week - 1:
            total = 0
            for j in range(len(weather[i])):
                total += weather[i][j]
            average = total / len(weather[i])
            return "{:.2f}".format(average)
        
def weekly_max(weather):
    week = int(input("Enter week number (1-5): "))
    for i in range(len(weather)):
        if i == week - 1:
            max_temp = 0
            for j in range(len(weather[i])):
                if weather[i][j] > max_temp:
                    max_temp = weather[i][j]
            return max_temp
        
def weekly_min(weather):
    week = int(input("Enter week number (1-5):"))
    for i in range(len(weather)):
        if i == week -1:
            min_temp = float('inf')
            for j in range(len(weather[i])):
                if weather[i][j] < min_temp:
                    min_temp = weather[i][j]
            return min_temp
        
def overall_max(weather):
    max_temp = 0
    for i in range(len(weather)):
        for j in range(len(weather[i])):
            if weather[i][j] > max_temp:
                max_temp = weather[i][j]
    return max_temp

def overall_min(weather):
    min_temp = float('inf')
    for i in range(len(weather)):
        for j in range(len(weather[i])):
            if weather[i][j] < min_temp:
                min_temp = weather[i][j]
    return min_temp

def main():
    print("1. Weekly average for the week\n2. Weekly maximum for the week\n3. Weekly minimum for the week\n4. Overall maximum\n5. Overall minimum")
    choice = int(input("Enter choice (1-5): "))
    if choice == 1:
        print("Weekly average for the week:", weekly_average(weather))
    elif choice == 2: 
        print("Weekly maximum for the week:", weekly_max(weather))
    elif choice == 3:
        print("Weekly minimum for the week:", weekly_min(weather))
    elif choice == 4:
        print("Overall maximum:", overall_max(weather))
    elif choice == 5:
        print("Overall minimum:", overall_min(weather))
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
    
if __name__ == "__main__":
    main()