#Write a program which display 1st 10 even numbers on Screen 

def ChkEven():
    iCnt = 0
    iNo = 1

    while(iCnt<10):
        if (iNo % 2 == 0):

            print(iNo)
            iCnt = iCnt + 1 
        iNo = iNo + 1
            
def main():
    ChkEven()

if __name__ == "__main__":
    main()