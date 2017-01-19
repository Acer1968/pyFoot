# python 3.5
#############
# Foot: A python football manager game
# Last updated: 2006.9.16
# A work in progress:
#  TODO Maintenance like adding new leagues, seasons, teams, and players
#  TODO Ai
#  TODO Individual player contributions
#  TODO Manager influence
#  TODO Player mentality
#  TODO Tactics


import pickle

from lib import league
from tools.utilities import get_response

#  TODO Maintenance like adding new leagues, seasons, teams, and players
#  TODO Ai


path = ''
filename = 'data/smelly_foot.p'


def load_game(manager_name):
    game =  pickle.load( open( path+filename, "rb" ) )
    if game.get_manager_name() is None and manager_name is not None:
        game.set_manager_name(manager_name)
    return game

def save_game(obj):
    pickle.dump(obj, open(path+filename, "wb"))

def new_game(manager_name):
    return league.League(name='Northern Americas', sample_league=True, manager_name=manager_name)

def name_manager(the_league):
    doit = True
    while doit:
        print("What is your first name??")
        first = input()
        print("Ok, %s, what is your last name?" % first)
        last = input()
        manager_name = first, last
        doit = False
        if the_league is not None: the_league.set_manager_name(manager_name)
        print("Ok")
        return manager_name


def run():
    manager_name = None
    run_run = True
    the_league = None
    print("\n\nWelcome to the Foot. A footy game in python")
    while run_run:
        if manager_name is not None: print("\nManager: %s %s" % (manager_name[0], manager_name[1]))
        print("\nOptions:")
        print("(L)oad a game")
        print("Start a (N)ew game.")
        if the_league is not None:
            print("((S)ave the game.")
            print("(T)est the game data.")
            print(("Go to the League Men(U)"))
        if the_league is not None:
            s = ''
            if manager_name is None: s += 'N'
            else: s += 'Ren'
            print(s+"ame the (M)anager.")
        command = get_response()
        if command == 'l':  # Load Game
            doit = False
            if the_league is not None:
                print("Are you sure you want to overwrite the current game? This cannot be undone.")
                if get_response() == 'y':
                    doit = True
            else: doit = True
            if doit:
                print('Load')
                the_league = load_game(manager_name)
                pn = the_league.get_manager_name()
                if pn is not None:
                    manager_name = pn
        elif command == 's' and the_league is not None:  # Save Game
            print("Save")
            save_game(the_league)
        elif command == 'u':  # League Menu
            the_league.menu()
        elif command == 'm' and the_league is not None:  # Change Manager's Name
            manager_name = name_manager(the_league)
        elif command == 'n':  # New Game
            doit = False
            if the_league is not None:
                print("Are you sure you want to overwrite the current game? This cannot be undone.")
                if get_response() == 'y':
                    doit = True
            else: doit = True
            if doit:
                print("New")
                the_league = new_game(manager_name)
        elif command == 't':  # Test the Game (Temporary)  # TODO replace this test with a better one
            the_league.play_match(the_league.teams[0], the_league.teams[1])
        elif command == 'q':  # Quit
            run_run = False
            print("Fine!")
        else:
            print("WTF?")

run()