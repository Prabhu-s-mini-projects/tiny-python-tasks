import Higher_Lower_Database as Db
import random

# Welcome logo
print(Db.logo)

score = 0


def compare(compare_a: int, compare_b: int, user_input: str) -> bool:
    return (compare_a >= compare_b and user_input == 'a') or (compare_b >= compare_a and user_input == 'b')


# Randomly selecting a person from the game database
compare_B = random.choice(Db.data)

# Keep the loop running until user input is wrong
continue_game = True
while continue_game:

    compare_A = compare_B
    print(f"Compare A : {compare_A.get('name')},{compare_A.get('description')},{compare_A.get('country')}.")

    print(Db.vs)

    compare_B = random.choice(Db.data)
    print(f"Compare B : {compare_B.get('name')},{compare_B.get('description')},{compare_B.get('country')}.")

    answer = input("Who has more followers?  Type 'A' or 'B' : \t").lower()

    continue_game = compare(compare_A.get('follower_count'), compare_B.get('follower_count'), answer)
    if continue_game:
        score += 1
        print("Correct :-) !")
    else:
        print("GAME OVER :-( !")

    print(f"{compare_A.get('name')} has {compare_A.get('follower_count')} Million followers,")
    print(f"{compare_B.get('name')} has {compare_B.get('follower_count')} Million followers,")
    print(f"Your score is {score}.")