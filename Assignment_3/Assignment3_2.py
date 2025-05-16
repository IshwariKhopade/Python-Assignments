#   write program which accepts N number from user and store it into list. return maximum number from that list.

def main():
    print("Enter Number of elements in List:")
    size = int(input())

    Data = []

    print("Enter Elements:")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    maximum = Data[0]
    for i in Data:
        if(i > maximum):
            maximum = i        

    print("Maximum number from list is:", maximum)

if __name__ == "__main__":
    main()