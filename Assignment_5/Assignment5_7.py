# Accept 5 numbers from user and  print largest number

def Max(Data):
    max = Data[0]
    for num in Data:
        if(num>max):
            max = num
    return max

def main():
    print("Enter Frequency: ")
    size = int(input())

    Data = []

    print("Enter Elements")
    for i in range(size):
        no = int(input())
        Data.append(no)

    Ret = Max(Data)

    print("Largest Number in given list is: ", Ret)

if __name__ == "__main__":
    main()