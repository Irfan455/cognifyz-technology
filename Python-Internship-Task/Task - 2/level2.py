import random
print("!! welcome to the number guesser !!")
print("guess the number between (1 to 50)\n")
random_int = random.randint(1,50)
   
while True: 
 n = int(input("enter a number:"))
 
 if(n<random_int):
    print("too low !!") 
    print("entr higher number please!")
 elif(n>random_int):
    print("too high !!") 
    print("enter lower number please!")
 else:
    print("Congratulation !!")
    print("you guess the correct number.")
    break