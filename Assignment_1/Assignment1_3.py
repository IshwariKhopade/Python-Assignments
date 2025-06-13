# Write a program which contains one function named as Add() which accepts 2 numbers from user and return addition of that 2 numbers

def Add(iNum1, iNum2):
    Ans = 0
    Ans = iNum1 + iNum2

    return Ans

def main():
    print("Enter 1st Number")
    iNo1 = int(input())

    print("Enter 2nd Number")
    iNo2 = int(input())

    iAns = Add(iNo1, iNo2)

    print("Addition is:", iAns)

if __name__ == "__main__":
    main()    
