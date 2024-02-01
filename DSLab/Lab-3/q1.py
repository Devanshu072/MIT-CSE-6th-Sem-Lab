def print_factors(n): # function to generate the factors. 
    for i in range (1, n+1):
        if n % i == 0:  
            print(i)
 
number = int(input("Enter a number : "))
 
print("The factors for {} are : ".format(number))
print_factors(number)
