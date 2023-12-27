try:
    n1 = (int(input("Enter the first number: ")))
    n2 = (int(input("Enter the second number: ")))
    if n1 > n2:
        n1, n2 = n2, n1
    print("Numbers are multiples of 7: ")
    for i in range(n1, n2 + 1):
        if i % 7 == 0:
            print(i)
except Exception as e:
    print (e)