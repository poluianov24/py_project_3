try:
    n1 = (int(input("Enter the first number: ")))
    n2 = (int(input("Enter the second number: ")))
    if n1 > n2:
        n1, n2 = n2, n1
    sum = 0
    for n in range(n1, n2 + 1):
        sum += n
        n += 1
    numbers = list(range(n1, n2+1))
    count = len (numbers)
    print("\033[35m")
    print(f"Sum of all integers between {n1} and {n2}:  {sum}")
    print (f"Average of all integers between {n1} and {n2}:  {sum / count}")
except Exception as e:
    print (e)