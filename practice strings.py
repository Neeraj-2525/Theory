def find_length():
    word = input('Enter a string: ')
    count = 0
    for i in word:
        count += 1
    return count


def find_maximum():
    s1 = (input('Enter a string1: '))
    s2 = (input('Enter a string2: '))
    s3 = (input('Enter a string3: '))
    s4 = (input('Enter a string4: '))
    max_string = max(s1, s2, s3, s4)
    return max_string


def replace():
    word2 = (input('Enter a string: '))
    r = " "
    for i in range(len(word2)):
        if i % 2 == 0:
            r += word2[i]
        else:
            r += "#"
    # print(r)
    return r


def counter():
    word3 = (input('Enter a string: '))
    a = word3.split()
    return a


if __name__ == "__main__":
    while True:
        print()
        choice = int(input("Enter 1 to find the length of the given string\n"
                           "Enter 2 to find the maximum of given three strings\n"
                           "Enter 3 to replace every successive alphabet with #\n"
                           "Enter 4 to count the number of words\n"
                           "Enter 0 to end\n"
                           "=>"))

        if choice == 1:
            print("Length of the string is", find_length())


        elif choice == 2:
            print("Maximum of three string is", find_maximum())


        elif choice == 3:
            print("Replaced string is", replace())


        elif choice == 4:
            print("Number of words in a given string is", counter())


        elif choice == 0:
            print("End")
            break

        else:
            print("sorry you have entered an invalid input!")

