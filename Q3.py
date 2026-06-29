def CalculateSquare(Num):
    return Num * Num

def main():
    value = int(input("Enter a number : "))

    Ret = CalculateSquare(value)

    print("Sqaure of number is : ",Ret)
    
if __name__ == "__main__":
    main()