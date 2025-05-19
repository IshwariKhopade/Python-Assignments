#Program to print sum of even numbers between 1 - 100. use a loop to find and print the sum of all even numbers from 1-100

def Sum():
    i = 1
    iSum = 0
    while(i<=100):
        if(i % 2 == 0):
            iSum = iSum + i
        i+=1
    return iSum

def main():
    Ret = Sum()
    print("Sum of even numbers between 1-100: ",Ret)

if __name__ == "__main__":
    main()
