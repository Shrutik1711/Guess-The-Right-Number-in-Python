import random 
n = random.randint(1,100)
a = -1
Guess = 1
while (a!=n):
    Guess+=1
    a = int(input("Guess a number :-- "))
    if (a<n):
        print("Guess a higher number ")
    
    elif(a>n):
        print("Guess a lower number ")
        
print(f"you guess the number {n} in {Guess} attempt")        
        
