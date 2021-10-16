
def play_again():
    print("\nDo you want to play again (y or n)?")
    answer = input('>').lower()
    if "y" in answer:
        start()
    else:
        exit()

#def play_again():
 # print("\nDo you want to play again? (y or n)")
  
  # convert the player's input to lower_case
  #answer = input(">").lower()

  #if "y" in answer:
    # if player typed "yes" or "y" start the game from the beginning
   # start()
  #else:
    # if user types anything besides "yes" or "y", exit() the program
   # exit()

def game_over(reason):
    print("\n" + reason)
    print('Game over!')
    play_again()

def diamond_room():
    print('''This room is full of shiny diamonds and only has one door!
    Do you:
    1. Grab as many diamonds as possible and go trough the door
    2. Leave the diamonds behind and go throug the door''')

    answer = input('>').lower

    if answer == '1':
        game_over('The diamonds were cursed and as soon as you touched them the world went black')
    elif answer == '2':
        print('You are an honest person and worthy of happiness!')
        play_again()
    else:
        game_over('Numbers, learn them.')

def bear_room():
    print('''There is a bear in here eating honey. 
    This bear is standing in front of antother door!
    Do you:
    1. Take the honey
    2. Taunt the bear ''')

    answer = input('>').lower()

    if answer == '1':
        game_over('The bear killed you')
    elif answer == '2':
        print('The bear chases you and then stops, the door can be opened')
        diamond_room()
    else:
        game_over("Don't you know how to type a number?")

def monster_room():
    print('''This room has a monster snoaring loudly!
    Behind the monster is door.
    Do you:
    1. Sneak around the monster and open the door quitely
    2. Show your courage and kill the monster''')

    answer = input('>').lower
    #this is a comment
    if answer == '1':
        print('You very quitley open the door')
        diamond_room()
    elif answer == '2':
        game_over('The monster woke up and killed you')
    else:
        game_over('Learn to type a number, for real')


def start():
    print('''You are standing in a dark room with a door to your left and right.
    Which direction do you go?''')

    answer = input('>').lower()

    if 'l' in answer:
        bear_room()
    elif 'r' in answer:
        monster_room()
    else:
        game_over("Don't you know how to type something correctly?")

start()