#Accept age from user and check whether the person is eligible to vote(Age should be 18 or above)

def ChkVoting(iAge):
    if(iAge>=18):
        return True
    else:
        return False

def main():
    print("Enter your Age:")
    iValue = int(input())

    iRet = ChkVoting(iValue)

    if(iRet == True):
        print("You are Eligible to vote")
    else:
        print("You are not Eligible to vote")

if __name__ == "__main__":
    main()