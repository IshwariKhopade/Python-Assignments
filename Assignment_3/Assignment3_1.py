#   write program which accepts N number from user and store it into list. return addition of all elements from that list.

def main():
    print("Enter Number of elements in List:")
    size = int(input())

    Data = []

    print("Enter Elements:")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    Add = 0
    for i in Data:
        Add = Add + i

    print("Addition of all elements from list is: ",Add)

if __name__ == "__main__":
    main()