import random

def level():
    while True:
        try:
            level_num = int(input("Level: "))
        except ValueError:
            print("Only enter integers large than 0")
            continue


        if level_num < 1:
            print("Level must be >=1")
            continue

        return level_num


def random_int(level_num):

    random_num = random.randint(1,level_num)
    return random_num

def guess(random_num):
    while True:
        try:
            guess_num = int(input("Guess: "))
        except ValueError:
            print("Only enter integers large than 0")
            continue

        if guess_num < 1:
            print("Guess must be >=1")
            continue

        if guess_num < random_num:
            print("Too small!")
            continue

        elif guess_num > random_num:
            print("Too large!")
            continue

        elif guess_num == random_num:
            print("Just right!")
            break

def main():
    lvl = level()
    num = random_int(lvl)
    guess(num)

main()
