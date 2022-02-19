first = int(input('enter the first number : '))
operator = (input('choose the operator (%,/,*,+,-):'))
second = int(input('enter the second number : '))


def main():
    if operator == "+":
        print(first + second)

    elif operator == '-':
        print(first % second)

    elif operator == '*':
        print(first * second)

    elif operator == '%':
        print(first % second)

    elif operator == '/':
        print(first / second)

    else:
        print('invalid operation')

main()
