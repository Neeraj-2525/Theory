def main():
    a = int(input('write the marks in English:'))
    b = int(input('write the marks in Maths:'))
    c = int(input('write the marks in CS:'))
    d = int(input('write the marks in Physics:'))

    total = (a + b + c + d)
    print("Total:", total)

    percentage = calculatePercentage(total)
    grades = computegrade(percentage)
    print_comment(grades)


def calculatePercentage(total):
    per = float(total * (100 / 400))
    print("percentage : ", per, "%")

    return per


def computegrade(per):
    if 90 < per <= 100:
        grade = 'A'

    elif 80 < per <= 90:
        grade = 'B'

    else:
        grade = 'F'

    return grade


def print_comment(grade):
    if grade == 'A':
        print("comment: very good")

    elif grade == 'B':
        print("comment: good")

    elif grade == 'F':
        print("comment: need improvement")


main()
