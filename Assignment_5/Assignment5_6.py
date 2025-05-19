"""
Print below Triangle pattern:

*
*   *
*   *   *
*   *   *   *

"""
def DisplayPattern(iNo):
    i = 1
    j = 1

    for i in range(1, iNo+1):
        for j in range(1 , iNo+1):
            if (j<=i):
                print("*", end="")
        print()   

def main():
    print("Enter Number")
    iValue = int(input())

    DisplayPattern(iValue)

if __name__ == "__main__":
    main()