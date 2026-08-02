def get_width():
    width = float(input("Enter width (m): "))
    return width

def get_length():
    length = float(input("Enter length (m): "))
    return length

def cal_area(width, length):
    area = width * length
    return area

def show_area(area):
    print(f"Area is: {area} m^2")

def show_area_in_SqWa(area):
    area_in_SqWa = area * 0.25
    print(f"Area is: {area_in_SqWa} Sq.Wa")

def show_info():
    width = get_width()
    length = get_length()
    area = cal_area(width, length)
    show_area(area)
    show_area_in_SqWa(area)

def main():
    show_info()

if __name__ == "__main__":
    main()