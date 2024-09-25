"""main script identifies higher and lower """
import random
import higher_lower_database as db

def compare(compare_a: int, compare_b: int, user_input: str) -> bool:
    """ identify which one is greater returns true or false based on user input """
    return (compare_a >= compare_b and user_input == 'a') or (compare_b >= compare_a and user_input == 'b')

def main()-> None:
    """start of program"""

    # Welcome logo
    print(db.LOGO)

    score = 0

    # Randomly selecting a person from the game database
    compare_b = random.choice(db.data)

    # Keep the loop running until user input is wrong
    continue_game = True
    while continue_game:

        compare_a = compare_b
        print(f"Compare A : {compare_a.get('name')},{compare_a.get('description')},{compare_a.get('country')}.")

        print(db.VS)

        compare_b = random.choice(db.data)
        print(f"Compare B : {compare_b.get('name')},{compare_b.get('description')},{compare_b.get('country')}.")

        answer = input("Who has more followers?  Type 'A' or 'B' : \t").lower()

        continue_game = compare(compare_a.get('follower_count'), compare_b.get('follower_count'), answer)
        if continue_game:
            score += 1
            print("Correct :-) !")
        else:
            print("GAME OVER :-( !")

        print(f"{compare_a.get('name')} has {compare_a.get('follower_count')} Million followers,")
        print(f"{compare_b.get('name')} has {compare_b.get('follower_count')} Million followers,")
        print(f"Your score is {score}.")

if __name__ == '__main__':
    main()
