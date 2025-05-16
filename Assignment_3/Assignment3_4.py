#   write program which accepts N number from user and store it into list. accept one another number from user & 
#   return frequency of that number from list.

def main():
    print("Enter Number of elements in List:")
    size = int(input())

    Data = []

    print("Enter Elements:")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Enter element to search")
    iValue = int(input())
    
    iCnt = 0
    for i in Data:
        if(i == iValue):
            iCnt+=1       

    print("Frequency :", iCnt)

if __name__ == "__main__":
    main()
