n = int(input("Enter the number of terms which you want to print "))

n1, n2 = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive number ")
elif n == 1:
    print("Fibonacci sequence upto ", n, ":")
else:
    print("fibonacci sequence : ")
    while count < n:
        print(n1)
        a = n1 + n2
        n1 = n2
        n2 = a
        count += 1