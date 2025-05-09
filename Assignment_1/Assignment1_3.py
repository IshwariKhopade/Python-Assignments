# Write a program which contains one function named as Add() which accepts 2 numbers from user and return addition of that 2 numbers

def Add():
    print("Enter 1st Number")
    iNo1 = int(input())

    print("Enter 2nd Number")
    iNo2 = int(input())

    Ans = 0
    Ans = iNo1 + iNo2

    return Ans

def main():

    iAns = Add()

    print("Addition is:", iAns)

if __name__ == "__main__":
    main()    