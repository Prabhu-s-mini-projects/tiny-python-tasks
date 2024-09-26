""" Main script of the program"""
# CONSTANTS

STARTING_LETTER_PATH = "input/Letters/starting_letter.txt"
INVITED_NAMES_PATH = "input/Names/invited_names.txt"
READ_TO_SEND_PATH = "output/ReadyToSend/"

def read_file(path) -> list:
    """ Read file and returns data in the form of string """
    with open(path,encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def write_letter(path, contents:list)-> None:
    """Write the modified content to the letter"""
    with open(path,"w",encoding='utf-8') as file:
        file.writelines(contents)

def main()-> None:
    """ start of program"""
    # Read the starting letter
    letter_contents = read_file(STARTING_LETTER_PATH)

    # Read the list of invited names
    invite_names = read_file(INVITED_NAMES_PATH)
    print(invite_names)

    # Replace the name with invited name
    for name in invite_names:
        new_content = letter_contents.copy()
        new_content[0] = new_content[0].replace("[name]",name.strip("\n"))
        path = READ_TO_SEND_PATH + name + "_invitation_letter.txt"
        # Save it as a new file in the mentioned path
        write_letter(path,new_content)
        new_content.clear()
if __name__ == '__main__':
    main()
