# DoS და DDoS შორის ის განსხვავებაა რომ Dos შეტევა ერთი კომპიუტერიდან ხდება DDoS შეტევა კი ბევრი კომპიუტერიდან ხდება

import time

secret_pin = "3333"
guess = ""
count = 0

start_time = time.time()

for i in range(10000):
    guess = str(i).zfill(4)
    count += 1
    
    print(f"Trying {guess}")
    
    if guess == secret_pin:
        print(f"Code was {guess}")
        break



password = "cybersecurity123"

user_password = input("enter your password: ")

while user_password != password:
    user_password = input("Try again")

print("correct password")



