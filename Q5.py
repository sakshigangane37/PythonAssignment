def DivisibleBy(Num):
    if Num % 3 == 0 and Num % 5 == 0:
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")

    return Num

def main():
    value = int(input("Enter a number : "))

    Ret = DivisibleBy(value)

if __name__ == "__main__":
    main() 