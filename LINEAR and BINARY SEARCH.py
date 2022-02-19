# Neeraj Kumar
# roll no. 21/73038
# LINEAR AND BINARY SEARCH menu driven

def linear_search(list1, val):
    """
    to find the position of an element
    in a list linearly.
    ----------------------------------------
        Linear Search Algorithm
    ----------------------------------------
    :param list1:
    :param val:
    :return:
    """

    for i in range(0, len(list1)):
        if list1[i] == val:
            return i


pos = -1
def bnry_search(list2, val):
    """
    to find the position of an element
    in a list through binary search.
        ----------------------------------------
        Binary Search Algorithm
        ----------------------------------------
    :param list2:
    :param val:
    :return:
    """

    l = 0  # Lower bound (first index)
    u = len(list2) - 1  # Upper bound (last index)

    while l <= u:
        mid = (l + u) // 2
        if list2[mid] == val:
            globals()['pos'] = mid
            return True
        else:
            if list2[mid] < val:
                l = mid + 1
            else:
                u = mid - 1


def main():
    while True:
        print("Enter 1 to execute linear search\nEnter 2 to execute binary search")
        choice = int(input("enter your choice: "))
        if choice == 1:
            print("---------------Linear Search Algorithm---------------")
            list1 = eval(input("enter the list: "))
            print(">>>List given is", list1)
            val = int(input("enter the element to find position: "))
            print("=>Element to be found is", val)
            index = linear_search(list1, val)
            if index:
                print(">>>Element found at position", index + 1)
            else:
                print(">>>Element not found!")
            print("\n")

        elif choice == 2:
            print("---------------Binary Search Algorithm---------------")
            list2 = eval(input("enter the list: "))
            list2.sort()
            print(">>>List given is ", list2)
            val = int(input("enter the element to find position: "))
            print("=>Element to be found is", val)
            if bnry_search(list2, val):
                print(">>>Element found at position", pos + 1)
            else:
                print(">>>Element not found!")
            print("\n")

        else:
            print("invalid choice")
            break


if __name__ == '__main__':
    main()
