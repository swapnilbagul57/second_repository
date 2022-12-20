x, y = 0, 1

while y < 50:
    print(y)
    x, y = y, x+y

# using if else and  for loop
num = int(input("Enter any number "))

n1, n2 = 0, 1
count = 0

if num <= 0:
    print("Please enter the number greater than 0 or Enter positive number ")
else:
    for i in range(0, num):
        print(count, end="\n")
        n1 = n2
        n2 = count
        count = n1 + n2