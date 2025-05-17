# Write a prog which contains one lambda function which accepts one parameter and returns its Multiplication

def main():

    print("Enter 1st Number:")
    Value1 = int(input())

    print("Enter 2nd Number:")
    Value2 = int(input())

    Multiplication = lambda iNo1, iNo2 : iNo1 * iNo2
    print("Multiplication is : ", Multiplication(Value1, Value2))


if __name__ == "__main__":
    main()