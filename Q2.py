def ChkGreater(No1,No2):
    if No1 >= No2 :
        print(f"{No1} is greater")
    elif No2 > No1 :
        print(f"{No2} is greater")
    else:
        print("Both numbers are equal")

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    ChkGreater(No1,No2)

if __name__ == "__main__":              
    main()
 