#Write a Program which accepts number from user and print that number of "*" on screen 

def PatternPrint(iNo):

    iCnt = 0
    while iCnt<iNo :
        print("*")

        iCnt = iCnt + 1



def main():
    print("Enter Number: ")
    iValue = int(input())

    PatternPrint(iValue)


if __name__ == "__main__":
    main()
