# Fibonacchi sequence upto given "n" terms
def fibonacchi(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacchi(num-2) + fibonacchi(num-1)
    
n = int(input("enter a nummber :"))
print(f"the fibonacchi sequence of {n} is :" , end=" ")
for i in range(0,n):
    
    print(fibonacchi(i) , end=" ")  
       