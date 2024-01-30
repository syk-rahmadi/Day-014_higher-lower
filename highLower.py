import os

from art import logo, vs
from game_data import data
import random
import os

def clear_screen():
    try:
        if os.name == 'posix':
            os.sytem ('clear')
        else:
            os.system('cls')
    except Exception as e:
        print('\n' * 50)


def randomPerson(): #get random person from data
    return random.choice(data)

def format_data(person):
    name = person["name"]
    description = person["description"]
    country = person["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(logo)
    score = 0
    game_should_continue = True
    person_a = randomPerson()
    person_b = randomPerson()

    while game_should_continue:
        person_a = person_b
        person_b = randomPerson()

        while person_a == person_b:
            person_b = randomPerson()


        print(f"Compare A: {format_data(person_a)}.")
        print(vs)
        print(f"Against B: {format_data(person_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = person_a["follower_count"]
        b_follower_count = person_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear_screen()
        print()
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_should_continue = False

game()