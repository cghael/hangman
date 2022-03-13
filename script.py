# Write your code here
import random

word_list = 'python', 'java', 'kotlin', 'javascript'
state_set = {"play", "exit"}
state = {'word': '',
         'word_set': set(),
         'tries': 0,
         'hint': '',
         'guessed': set()}


def init_game():
    input_ = ""

    while input_ not in state_set:
        input_ = input('Type "play" to play the game, "exit" to quit: ')

    state['word'] = random.choice(word_list)
    state['word_set'].update(state['word'])
    state['tries'] = 8
    state['hint'] = "-" * len(state['word'])
    state['guessed'].clear()

    return input_


def is_correct_letter(letter):
    if len(letter) != 1:
        print("You should input a single letter")
        return False

    if not letter.isalpha() or not letter.islower():
        print("Please enter a lowercase English letter")
        return False

    if letter in state['guessed']:
        print("You've already guessed this letter")
        return False

    return True


def guess_letter(letter):
    state['word_set'].remove(letter)
    index = state['word'].find(letter)
    while index >= 0:
        state['hint'] = state['hint'][:index] + letter + state['hint'][index + 1:]
        index = state['word'].find(letter, index + 1)


def start():
    while state['tries'] > 0:
        print(f"\n{state['hint']}")
        letter = input("Input a letter: ")

        if not is_correct_letter(letter):
            continue

        state['guessed'].add(letter)

        if letter in state['word']:
            guess_letter(letter)
            if state['hint'] == state['word']:
                print(print(f"\n{state['word']}"))
                print("You guessed the word!\nYou survived!")
                return
        else:
            print("That letter doesn't appear in the word")
            state['tries'] -= 1

    print("You lost!")


def main():
    print("H A N G M A N")
    input_ = init_game()
    while input_ == "play":
        start()
        input_ = init_game()


if __name__ == "__main__":
    main()
