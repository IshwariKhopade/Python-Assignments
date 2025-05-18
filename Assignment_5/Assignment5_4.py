# Accept number from user and print its factorial using for loop

def main():

    print("Enter a number:")
    Value = int(input())

    iMul = 1
    for i in range(1,Value+1):
        iMul = iMul * i
    print(iMul)

if __name__ == "__main__":
    main()