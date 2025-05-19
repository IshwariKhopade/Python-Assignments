# Accept number from user and print its multiplication table upto 10

def Table(iNo):
    i = 1
    Ans = 0
    while(i <= 10):
        Ans = iNo * i
        print(iNo,"x", i ,"=" ,Ans)
        i+=1

def main():

    print("Enter a number:")
    iValue = int(input())

    Table(iValue)    

if __name__ == "__main__":
    main()
