try:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    count = 0
    if n1 > n2:
        n1, n2 = n2, n1
    print("Numbers in this range: ")
    for i in range (n1, n2+1):
        print (i, end=" " if i < n2 else " ")
    print("\nThe numbers in the range are in reverse order: ")
    for i in range (n1, n2+1) [::-1]:
        print (i, end=" " if i < n1+1 else " ")
    print("\nNumbers are multiples of 7: ")
    for i in range(n1, n2 + 1):
        if i % 7 == 0:
            print(i, end=" " if i < n2-6 else " ")
    print("\nNumber of numbers that are multiples of 5: ")
    for i in range(n1, n2 + 1):
        if i % 5 == 0:
            count += 1
    print(count, end=" ")
except Exception as e:
    print (e)