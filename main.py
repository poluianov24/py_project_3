try:
    n = int(input("Enter the string length: "))
    x = str(input("Enter line fill character: "))
    number = 1
    while number < n + 3:
        number += 1
        print(x, end="")
except Exception as e:
    print(e)