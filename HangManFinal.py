import random

try_count = 8
print("H A N G M A N")
sequence = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(sequence)
word_list = [char for char in word]
shown = ""
shown_list = ["-" for char in word]
shown = shown.join(shown_list)
chars = "abcdefghijklmnopqrstuvwxyz"
guessed_list = []

while True:
    order = input('Type "play" to play the game, "exit" to quit: ')
    if order == "play":
        while True:
            if try_count > 0:        
                print("\n")
                print(shown)
                if "-" not in shown_list:
                    print("You guessed the word!\nYou survived!")
                    print()
                    break
                letter = input("Input a letter ")
                if len(letter) != 1:
                    print("You should input a single letter")
                elif letter not in chars:
                    print("Please enter a lowercase English letter")
                elif letter in guessed_list:
                    print("You've already guessed this letter")        
                elif letter in word and letter not in shown_list:
                    for i in range(len(word)):
                        if word_list[i] == letter:
                            shown_list[i] = letter        
                    shown = ""
                    shown = shown.join(shown_list)
                    guessed_list += letter                          
                else:
                    print("That letter doesn't appear in the word")
                    guessed_list += letter
                    try_count -=1
            else:
                print ("You lost!")
                print()
                break
    elif order == "exit":
        break