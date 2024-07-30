print("The Love Calculator is calculating your score...")
name1 = input('What is your name? \t')  #
name2 = input('What is their name? \t')  #
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

names = name1 + name2
T = names.lower().count('t')
R = names.lower().count('r')
U = names.lower().count('u')
E = names.lower().count('e')
L = names.lower().count('l')
O = names.lower().count('o')
V = names.lower().count('v')
score = int(str(T + R + U + E) + str(L + O + V + E))

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
