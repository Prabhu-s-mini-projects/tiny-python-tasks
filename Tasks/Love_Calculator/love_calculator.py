""" main script of a program"""
def main()-> None:
    """start of program"""
    print("The Love Calculator is calculating your score...")
    print(r'''
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

    t = combined_name.lower().count('t')
    r = combined_name.lower().count('r')
    u = combined_name.lower().count('u')
    e = combined_name.lower().count('e')
    l = combined_name.lower().count('l')
    o = combined_name.lower().count('o')
    v = combined_name.lower().count('v')

    score = int(str(t + r + u + e) + str(l + o + v + e))

    if score < 10 or score > 90:
        print(f"Your score is {score}, you go together like coke and mentos.")
    elif 40 <= score <= 50:
        print(f"Your score is {score}, you are alright together.")
    else:
        print(f"Your score is {score}.")

if __name__ == '__main__':
    main()
