import random
print("!! welcome to the guessing game !!")
print("guess the number between (1 to 100)\n")
random_int = random.randint(1,100)
   
while True: 
 n = int(input("enter a number:"))
 
 if(n<random_int):
    print("too low !!") 
 elif(n>random_int):
    print("too high !!") 
 else:
    print("Congratulation !!")
    print("you guess the correct number.")
    break
    
