'''

Format for naming functions:
    def level_part()
    ex. def two_preFight()

'''
import time


def intro_start(bypass):
    if not bypass:
        print('\n...It\'s been an exhausting day at school.')
        time.sleep(2)
        print('...You were eager to hop on you computer by the time you returned home.')
        time.sleep(2.5)
        print('...To your excitement, you managed to borrow a copy of the newest Battle RPG from your friend.')
        time.sleep(3)
        print('...You impatiently slid the CD into your computer, and a bright logo appeared on the screen.')
        time.sleep(2.5)
        print('\nIt read,')
        time.sleep(1)
        print('THE SPARTAN GAMES')
        time.sleep(4)
        print('\n...With a grin widening across your face, you spammed a couple keys to speed up the loading.')
        time.sleep(3)
        print('...Disappointingly, the screen went dark.')
        time.sleep(2.3)
        print(
            '...You thought it might have been something you pressed. You clicked a couple more keys hoping the game would return.')
        time.sleep(4)
        print('...But instead, your screen went to flickering static.')
        time.sleep(2.5)
        print('\n...You tried disconnecting the game, but it wouldn\'t allow you.')
        time.sleep(1.5)
        print('...You tried to eject the CD, but the compartment was locked.')
        time.sleep(1.5)
        print('...You tried unplugging your computer, but the static only intensified.')
        time.sleep(4)
        print('\n...Eventually, the computer began shaking rapidly and a rumbling noise flowed into your ears.')
        time.sleep(3)
        print('...The static filled your room until you were surrounded by nothing but flickering lights')
        time.sleep(3)
        print(
            '...You passed out from the sensory overload, although not before hearing the distant sound of a crowd chanting.')
        time.sleep(4)
    else:
        print(
            '\n...You passed out from the sensory overload, although not before hearing the distant sound of a crowd cheering.')
        time.sleep(1)


def one_start():
    print('\n\n---------------')
    time.sleep(1)
    print('\n\n..."FIGHT! FIGHT! FIGHT!"')
    time.sleep(1)
    print('...Your eyes gradually opened to the blaring sunlight.')
    time.sleep(2)
    print('\n..."FIGHT! FIGHT! FIGHT!"')
    time.sleep(1)
    print('...The sound of loud chanting around you filled your eardrums.')
    time.sleep(2)
    print('\n..."FIGHT! FIGHT! FIGHT!"')
    time.sleep(1)
    print('...As you stood to your feet, your noticed yourself standing in a large field of sand.')
    time.sleep(2)
    print('...Rows and rows of people surrounded the field, forming a sizeable arena.')
    time.sleep(2)
    print('\n..."FIGHT! FIGHT! FIGHT!"')
    time.sleep(1)
    print('...')