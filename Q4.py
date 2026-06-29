def CalculateCube(Num):
    return Num * Num * Num

def main():
    value = int(input("Enter a number : "))

    Ret = CalculateCube(value)

    print("Cube of number is : ",Ret)

if __name__ == "__main__":
    main()