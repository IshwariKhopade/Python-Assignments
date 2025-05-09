# Write a program which Accepts number from user and check whether that number is positive negative or zero

def ChkNum(iNo):

    if(iNo==0):
        print("Entered Number is Zero")
    elif(iNo>0):
        print("Entered Number is a Positive Number")
    elif(iNo<0):
        print("Entered Number is a Negative Number")
    else:
        printf("Invalid Number")

def main():

    print("Enter a Number")
    iNum = int(input())

    ChkNum(iNum)

if __name__ == "__main__":
    main()