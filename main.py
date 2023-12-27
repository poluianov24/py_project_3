try:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    if n1 > n2:
        n1, n2 = n2, n1
    for i in range (n1, n2+1):
        if i % 3 == 0 and i % 5 ==0:
            print("Fizz Buzz")
        elif i % 5 ==0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
except Exception as e:
    print (e)