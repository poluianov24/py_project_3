try:
    n = int(input("Enter the string length: "))
    number = 1
    while number < n + 1:
        number += 1
        print("*", end="")
except Exception as e:
    print(e)