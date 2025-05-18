# Accept number from user and print its multiplication table upto 10

def main():

    print("Enter a number:")
    Value = int(input())

    i = 1
    Ans = 0
    while(i <= 10):
        Ans = Value * i
        print(Value,"x", i ,"=" ,Ans)
        i+=1

if __name__ == "__main__":
    main()