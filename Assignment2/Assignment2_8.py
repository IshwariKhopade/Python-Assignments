"""
 write program which accepts one number and Display below pattern.

    1    
    1   2   
    1   2   3  
    1   2   3   4   
    1   2   3   4   5  
 
"""

def Display(iNo):
    n = iNo

    for i in range(1, n+1):
        for j in range(1, i+1):
            print(" ", j , end = "")
        print()

def main():
    print("Enter a number:")
    iValue = int(input())

    Display(iValue)
    
if __name__ == "__main__":
    main()