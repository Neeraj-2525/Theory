import math


def triangle(side1, side2, side3):
    try:
        s = (side1 + side2 + side3) / 2
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        assert (side1 + side2 >= side3) or (side1 + side3 >= side2) or (side2 + side3 >= side1) \
               or (side1 > 0) or (side2 > 0) or (side3 > 0)
        return area

    except ValueError:
        print("Enter valid sides!")


if __name__ == '__main__':
    side1 = int(input("enter the side1: "))
    side2 = int(input("enter the side2: "))
    side3 = int(input("enter the side3: "))
    # (side1, side2 , side3) = map(int(input("enter side1: ")), int(input("enter side2: ")), int(input("enter side3: ")))
    print("Area of the Triangle is", triangle(side1, side2, side3), )
