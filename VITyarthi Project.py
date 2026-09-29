bold_italic = "\033[1;3m"
reset = "\033[0m"

print("\n " * 30)

title = bold_italic+"GUESS THE MYSTERY WORD"+reset   

print("=" * 50)         

print(title.center(50, "*"))


print(bold_italic+"YOU WILL BE PROVIDED WITH THE HINT AND FOUR CHANCES TO ENTER THE CORRECT ANSWER"+reset)

print(bold_italic + "HINT".center(30,"*") + reset)

levels = [
    ["Algorithm" ,
      '''I have a beginning and an end, but no physical form.
I am built purely of logic, loops, and conditions.
Without me, your software would stand completely still, unable to make a single decision.
''', 
     4]  ,

    ["Variable", 
     '''I have a name and i can store value.
my value can be change while program is running .
who am I ? ''' , 
     3] ,

    ["Medicine" , 
      '''i might alter your receptors or battle your pest ,
or settle the rythm that beats in your chest .
Too little can fail you, Too much is a threat ,  
I cure your afflictions but leave a side effect.''' , 
     2]
]

level= 0

while level < len(levels) :
    secret_word=levels[level][0]
    hint=levels[level][1]
    tries=levels[level][2]

    print("\n")
    print(f"LEVEL{level+1}".center(50 , "*"))
    print(bold_italic+"HINT".center(30,"*")+reset)
    print(bold_italic+hint+reset)


    user_guess = input("Enter Guess: ").capitalize()

    


    while secret_word != user_guess:

        tries = tries - 1

        print("\n")

        if tries > 1:

            print(f'Wrong Guess, {tries} chances left'.center(50, "-"))

        elif tries == 1:

            print(f'Wrong Guess, last chance left'.center(50,"-"))

        elif tries == 0:

            print(f'GAME OVER! All CHANCES ARE FINISHED !'.center(50,"-"))

            break

        user_guess = input("Enter Guess: ").capitalize()

    if secret_word == user_guess:

        print("=" *50)
        print(f'LEVEL{level+1} CLEARED!'.center(50,"*") )
        print("="*50)

        level = level +1

    else:
        
        break

if level == len(levels):

    print("\n")
    print("=" * 50)
    print("YOU WIN ! GENIUS! YOU COMPLETED ALL LEVELS ".center(50,"*"))
    print("=" * 50)



