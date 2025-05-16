#   write program which accepts N number from user and store it into list. return minimum number from that list.

def main():
    print("Enter Number of elements in List:")
    size = int(input())

    Data = []

    print("Enter Elements:")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    minimum = Data[0]
    for i in Data:
        if(i < minimum):
            minimum = i        

    print("Minimum number from list is:", minimum)

if __name__ == "__main__":
    main()
