"""
 write program which accepts one number and Display below pattern.

    *   *   *   *   *
    *   *   *   *
    *   *   *
    *   *
    *   
 
"""

def Display(iNo):
    n = iNo

    for i in range(0, n):
        for j in range(i, n):
            print("*", end = "")
        print()

def main():
    print("Enter a number:")
    iValue = int(input())

    Display(iValue)
    
if __name__ == "__main__":
    main()