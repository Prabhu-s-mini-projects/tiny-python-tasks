# Dependencies
import pandas


alphabet_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

while True:
    name = input("Enter your name: \t")

    letters = [letter.upper() for letter in name]

    # # Approach method : 1
    # phonetic_letter = [alphabet_dataframe[alphabet_dataframe["letter"] == letter].code.item() for letter in letters]
    # print(phonetic_letter)

    # #Approach method : 2
    # for index, row in alphabet_mapping.iterrows():
    #     print(row.letter)
    #     print(row.code)

    # Approach method : 3 (using list comprehension)
    code_dict = {row.letter : row.code for (index,row) in alphabet_dataframe.iterrows()}

    try:
        result = [code_dict[letter] for letter in letters]
    except KeyError:
        print("Sorry, please enter only the Alphabets")
    else:
        print(result)
