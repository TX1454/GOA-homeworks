number = int(input("enter number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")



a = 15
b = 30

if a > b:
    print("a is bigger")
elif a < b:
    print("b is bigger")
else:
    print("equal")


score = 75

if score >= 90:
    print("Excellent")
elif score >= 70 and score <= 89:
    print("Good")
elif score >= 50 and score <= 69:
    print("Average")   
else:
    print("Failed")    


a = 12
b = 45
c = 27

if a > b and a > c:
    print("a is the biggest")
elif b > a and b > c:
    print("b is the biggest")
else:
    print("c is the biggest")


price = 250

if price > 300:
    print("30% discount")
elif price > 200:
    print("20% discount")
elif price > 100:
    print("10% discount")
else:
    print("no discount")


print("final price")

