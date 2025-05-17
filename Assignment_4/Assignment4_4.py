"""
Write a program which contains filter(), map() and reduce) in it. Python application which contains one list of numbers 
which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square.
Reduce will return addition of all that numbers.
"""
from functools import reduce

CheckEven = lambda No: No % 2 == 0
Square = lambda No: No * No
Add = lambda A, B: A + B

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

    FData = list(filterX(CheckEven, Data))
    print("List after filter:", FData)

    MData = list(mapX(Square, FData))
    print("List after map:", MData)

    RData = reduceX(Add, MData)
    print("Output of reduce:", RData)

if __name__ == "__main__":
    main()
