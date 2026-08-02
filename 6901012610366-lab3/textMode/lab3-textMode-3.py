def width():
    width = int(input("Enter the width: "))
    return width

def height():
    height = int(input("Enter the height: "))
    return height

def area(width, height):
    area = width * height
    return area

def area_for(area):
    # for Football
    if area >= 7140:
        print(f"The area is: {area}. It is suitable for Football.")
    # for Basketball
    elif area >= 4200:
        print(f"The area is: {area}. It is suitable for Basketball.")
    # for Tennis
    elif area >= 2600:
        print(f"The area is: {area}. It is suitable for Tennis.")
    # for Badminton
    elif area >= 1500:
        print(f"The area is: {area}. It is suitable for Badminton.")
    else:
        print("Please enter a valid area for sports.")

def main():
    width_value = width()
    height_value = height()
    area_value = area(width_value, height_value)
    area_for(area_value)

if __name__ == "__main__":
    main()