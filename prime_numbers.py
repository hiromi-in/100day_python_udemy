#Write your code below this line 👇



def prime_checker(number):
    non_prime_num = False
    while not non_prime_num:
        for i in range(2, number):
            if number % i == 0:
                print('It\'s not a prime number.')
                non_prime_num = True
                break
                  
        if not non_prime_num:    
            print('It\'s a prime number.')
            non_prime_num = True        
        
        

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
