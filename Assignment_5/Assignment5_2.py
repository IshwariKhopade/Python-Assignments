#Program to print sum of even numbers between 1 - 100. use a loop to find and print the sum of all even numbers from 1-100

def main():
    i = 1
    iSum = 0
    while(i<=100):
        if(i % 2 == 0):
            iSum = iSum + i
        i+=1
    print("Sum of even numbers between 1-100: ",iSum)


if __name__ == "__main__":
    main()