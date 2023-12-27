try:
    n = (int(input("Enter the number: ")))
    result = 1
    for i in range(1, n + 1):
        result *= i
    print("\033[35m")
    print(f"Factorial of the number {n} :  {result}")
except Exception as e:
    print (e)