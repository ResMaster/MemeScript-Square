def Main():
    print("Welcome to Square's Angles!\nWrite three angles of a square to calculate the forth angle")
    try:
        a = "error"
        angle1 = int(input("Please insert first angle: "))
        if angle1 != 90:
            int(a)
        angle2 = int(input("Please insert second angle: "))
        if angle2 != 90:
            int(a)
        angle3 = int(input("Please insert third angle: "))
        if angle3 != 90:
            int(a)
        print("The forth angle is 90\nThanks for using Square's Angles!")
    except ValueError:
        print("Something has gone wrong. Check the angles you have written!")


if __name__ == "__main__":
    Main()
