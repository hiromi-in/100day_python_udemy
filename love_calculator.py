# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

true = 0
love = 0

if 't' in name1 or name2:
    true = true + name1.count('t') + name2.count('t')
if 'r' in name1 or name2:
    true = true + name1.count('r') + name2.count('r')
if 'u' in name1 or name2:
    true = true + name1.count('u') + name2.count('u')
if 'e' in name1 or name2:
    true = true + name1.count('e') + name2.count('e')

if 'l' in name1 or name2:
    love = love + name1.count('l') + name2.count('l')
if 'o' in name1 or name2:
    love = love + name1.count('o') + name2.count('o')
if 'v' in name1 or name2:
    love = love + name1.count('v') + name2.count('v')
if 'e' in name1 or name2:
    love = love + name1.count('e') + name2.count('e')

love_score = int(str(true) + str(love))

#print(love_score)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")


#t1 = name1.count('t')
#r1 = name1.count('r')
#u1 = name1.count('u')
#e1 = name1.count('e')
#t2 = name2.count('t')
#r2 = name2.count('r')
#u2 = name2.count('u')
#e2 = name2.count('e')
#
#l1 = name1.count('l')
#o1 = name1.count('o')
#v1 = name1.count('v')
#e1 = name1.count('e')
#l2 = name2.count('l')
#o2 = name2.count('o')
#v2 = name2.count('v')
#e2 = name2.count('e')
