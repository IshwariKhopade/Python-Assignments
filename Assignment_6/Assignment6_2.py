#Accept Character from user and check if it is vowel(a,e,i,o,u), if not then print its a consonant.

def CheckVowel(ch):
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
        return True
    else:
        return False

def main():
    print("Enter a character: ")
    cValue = input()

    cRet = CheckVowel(cValue)

    if(cRet == True):
        print(cValue, "is a Vowel")
    else:
        print(cValue, "is a Consonant")
    
if __name__ == "__main__":
    main()