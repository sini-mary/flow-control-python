#Write a function that uses while, if and continue statements
# to print all the even numbers between 0 and 50. 
def find_even():
    x=1
    while x <50:
        x+=1
        if x%2!=0:
            continue
        
               

#Write a function that takes an integer argument and prints "Prime" if the number is prime,
# and "Not prime" if the number is not prime.
def check_prime(num):
    check=False
    
    if num==1:
        print("Not Prime")
    elif num >1:
        for i in range(2,num):
            if num%i==0:
             check=True
             
             
             
             
    if check:
        print("is not prime")
    else:
        print("is prime")
                         
                
#Write a function that takes a list of integers as
# input and prints the sum of all the even numbers in the list.
def take_list(nums):
    count=0
    for i in nums:
        if i%2==0:
            count+=i
    print(count)
    
    
#Write a function that takes any two integers as input, and prints the sum 
# of all the numbers between the
# two integers (inclusive) that are divisible by 3.
def take_two(num1,num2):
    count=0
    for i in range(num1,num2):
        if i%3==0:
            count+=i
            print(count)
    
            
    