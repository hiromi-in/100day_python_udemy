# Import the random module here

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill_payer = random.choice(names)

print(f"{bill_payer} is going to buy the meal today!")


# Import the random module here

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#bill_payer = random.choice(names)
#print(f"{bill_payer} is going to buy the meal today!")

order = len(names)
pick = random.randint(0,order-1)
who_will_pay = names[pick] 

print(f"{who_will_pay} is going to buy the meal today!")
