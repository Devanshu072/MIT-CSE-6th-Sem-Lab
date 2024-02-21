import pandas as ps

n = int(input("Enter a number: "))

while(n>0):
    if n%3 == 0:
        print("Divisible by 3")
        n-=1
    else:
        print("Not Divisible")
    
else:
    print("while ended")
