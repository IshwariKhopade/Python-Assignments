# Write a prog which contains one lambda function which accepts one parameter and returns power of two

def main():

    print("Enter a Number:")
    Value = int(input())

    Power = lambda iNo : iNo * iNo
    print("Power is : ", Power(Value))


if __name__ == "__main__":
    main()