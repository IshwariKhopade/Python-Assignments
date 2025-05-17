"""
Write a program which contains filter(), map() and reduce) in it. Python application which contains one list of numbers 
which are accepted from user. Filter should filter out all prime numbers. Map function will multipliy each number by 2.
Reduce will return maximum number from those numbers.
"""
from functools import reduce

def Prime(No):
    if No < 2:
        return False
    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False
    return True

def Multiply(No):
    return No * 2

def Maximum(A, B):
    return A if A > B else B

def filterX(Task, Values):
    Result = []
    for no in Values:
        if Task(no):
            Result.append(no)
    return Result

def mapX(Task, Values):
    Result = []
    for no in Values:
        Result.append(Task(no))
    return Result

def reduceX(Task, Values):
    Result = Values[0]
    for no in Values[1:]:
        Result = Task(Result, no)
    return Result

def main():
    Data = []
    print("Enter No of Elements:")
    size = int(input())

    print("Enter numeric Values:")

    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input List:", Data)

    FData = list(filterX(Prime, Data))
    print("List after filter:", FData)

    MData = list(mapX(Multiply, FData))
    print("List after map:", MData)

    RData = reduceX(Maximum, MData)
    print("Output of reduce:", RData)

if __name__ == "__main__":
    main()
