number = int(input("enter first number: "))
number1 = int(input("enter second number: "))

if number > number1:
    print("first number is bigger")
elif number < number1:
    print("second number is bigger")
else:
    print("numbers are equal")


score = 85

if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
else:
    print("failed")


number = 30

if number % 3 == 0:
    print("divisible by 3")
elif number % 5 == 0:
    print("divisible by 5")
elif number % 3 == 0 and 5 == 0:
    print("divisible by both")
else:
    print("not divisible by 3 or 5")




price = 150

if price > 200:
    print("20% discount")
elif price > 100:
    print("10% discount")
else:
    print("no discount")