import random

def hangman():
    word_list = ["cat", "bird", "horse", "gerbil"]
    random_number = random.randint(0,4)
    word = word_list[random_number]
    wrong = 0
    stages = ["",
              "____      ",
              "|         ",
              "|    |    ",
              "|    0    ",
              "|   /|\   ",
              "|   / \   ",
              "|         "
              ]
    remaining_letters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in remaining_letters:
            cind = remaining_letters.index(char)
            board[cind] = char
            remaining_letters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))

