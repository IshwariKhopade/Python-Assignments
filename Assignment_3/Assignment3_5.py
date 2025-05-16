"""
Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. 
Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user 
defined module named as MarvellousNum. Name of the function from main python file should be ListPrime()

"""

from Marvellousnum import ChkPrime

def ListPrime(Data):
    Sum = 0
    for no in Data:
        if ChkPrime(no):
            Sum += no
    return Sum

def main():
    print("Enter number of elements in List:")
    size = int(input())

    Data = []

    print("Enter elements:")
    for i in range(size):
        no = int(input())
        Data.append(no)

    result = ListPrime(Data)
    print("Addition of all prime numbers is:", result)

if __name__ == "__main__":
    main()
