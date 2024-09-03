import pandas

name = input("Enter your name: \t")

alphabet_mapping = pandas.read_csv("nato_phonetic_alphabet.csv")

letters = [letter.upper() for letter in name]

phonetic_letter = [alphabet_mapping[alphabet_mapping["letter"] == letter].code.item() for letter in letters]

print(phonetic_letter)

# # Another approach method
# for index, row in alphabet_mapping.iterrows():
#     print(row.letter)
#     print(row.code)

code_dict = {row.letter : row.code for (index,row) in alphabet_mapping.iterrows()}

result = [code_dict[letter] for letter in letters]

print(result)
