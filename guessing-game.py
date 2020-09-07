import random
import os

input("Hi.. how are you today ?")
print("Okay, We will playing now \nthis is a game to gussing any number in ur mind \njust you put any number in ur mind and Watch!")
input("Press Enter whan u Ready")
max_no = int(input("What is the max number ?"))
min_no = 1
run = True
guessing = 0
high = max_no
low = min_no
guess_count = 0

def guess(guess_count,run,no1,no2):
    
    guessing = random.randint(no1,(no2))
    print(guessing)
    user_answer = input("Did i guessing corrent ?").lower()
    user_answers = ["l","h","c"]

    if user_answer not in user_answers:
        user_answer = input("in this case ur number is lower what the program guessed u write 'l'\nand if highter u write 'h' and if guessing right u write 'c'")


    while run == True :
        guess_count += 1
        if user_answer == "c":
            print(f"yeah i guessed it after {guess_count} guessing")
            run = False
        elif user_answer =="l":
            if guessing == low :
                print ("i'm done u ruled out numbers ! i will go out")
                run = False
            else:
                guess(guess_count,run,no1,guessing)
        elif user_answer == "h":
            if guessing == high:
                print("i'm done u ruled out numbers ! i will go out")
                run == False
            else:
                    guess(guess_count,run,guessing,no2)

    print ("Thanks for playing with me")
    os._exit(0)

guess(guess_count,run,min_no,max_no)