# Write a program which contains one function named as ChkNum() which accept one parameter as number.if number is even then it should should display
#"Even Number" otherwise it should display "Odd Number" on console.


#Function to check if number is Positive, Zero or Negative
def ChkNum(iNo):
    if(iNo<0):
        print("Please Enter a positive number")
    elif(iNo % 2 == 0):
        print("Even Number")
    else:
        print("Odd Number")

def main():
    print("Enter a number")
    iValue = int(input())  

    ChkNum(iValue)

if __name__ =="__main__":
    main()  