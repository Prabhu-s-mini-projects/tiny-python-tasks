print("The Love Calculator is calculating your score...")
print('''
   _______________                        |*\_/*|________
  |  ___________  |     .-.     .-.      ||_/-\_|______  |
  | |           | |    .****. .****.     | |           | |
  | |   0   0   | |    .*****.*****.     | |   0   0   | |
  | |     -     | |     .*********.      | |     -     | |
  | |   \___/   | |      .*******.       | |   \___/   | |
  | |___     ___| |       .*****.        | |___________| |
  |_____|\_/|_____|        .***.         |_______________|
    _|__|/ \|_|_.............*.............._|________|_
   / ********** \                          / ********** \\
 /  ************  \                      /  ************  \\
--------------------                    --------------------
''')
# 🚨 References: https://www.asciiart.eu/holiday-and-events/valentine 👆

your_name = input('What is your name? \t')  #
their_name = input('What is their name? \t')  #

combined_name = your_name + their_name

T = combined_name.lower().count('t')
R = combined_name.lower().count('r')
U = combined_name.lower().count('u')
E = combined_name.lower().count('e')
L = combined_name.lower().count('l')
O = combined_name.lower().count('o')
V = combined_name.lower().count('v')

score = int(str(T + R + U + E) + str(L + O + V + E))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
