import datetime
import random

import match
import team

from lib import player
from tools import lists
from tools.utilities import  get_response, get_long_response, pad_string

team_names = ['Atlanta', 'New York', 'Los Angeles', 'Dallas', 'Houston', 'Seattle', 'Portland', 'Chicago', 'Boston',
              'Nashville', 'Phoenix', 'Minneapolis', 'Detroit', 'Phlidelphia', 'Denver', 'Las Vegas', 'Jackson',
              'Fargo', 'Toranto', 'Montreal', 'San Antonio', 'San Diego', 'Calgary', 'San Jose', 'Ottawa', 'Austin',
              'Edmonton', 'Jacksonville']


class League(object):
    def __init__(self, **kwargs):
        if kwargs is not None:
            #  = kwargs[''] if '' in kwargs else ''
            self.name = kwargs['name'] if 'name' in kwargs else "no name"
            self.sample_league = kwargs['sample_league'] if 'sample_league' in kwargs else False  # bool
            self.verbose = kwargs['verbose'] if 'verbose' in kwargs else False
            self.manager_name = kwargs['manager_name'] if 'manager_name' in kwargs else None
        self.teams = []
        self.player_team = None
        num_teams = len(self.teams)
        self.year = datetime.datetime.now().year
        self.week_num = 1
        self.week_played = False
        self.season_complete = False
        self.market = []  # TODO Market should reflect players for sale and loan, not unattached players
        self.table = []
        self.update_table()
        if self.sample_league:
            for each in team_names:
                self.teams.append(team.Team(name=each, sample_team=True))
            if self.verbose:
                for each in self.teams:
                    print(each.name)
                    print(each)
        for i in range(0,200):
            position = random.choice(list(team.base_team))
            self.market.append(player.Player(name=lists.get_mens_name_distributed(),
                                             surname=lists.get_last_name_distributed(),
                                             position=position, area=team.base_team[position][1],
                                             sided=team.base_team[position][0], age=random.randint(18, 29),
                                             rating=random.randint(10, 99)))
        self.schedule = None
        self.create_schedule()

    def update_table(self):
        self.table = []
        temp_dict = {}
        sorting_list = []
        n = 0.0
        for each in self.teams:
            sorting_list.append(each.get_rating())
            tm = each.get_name()
            pl = each.get_played()
            wn = each.get_won()
            dn = each.get_drawn()
            lt = each.get_lost()
            gf = each.get_goals_for()
            ga = each.get_goals_against()
            gd = each.get_goals_difference()
            pt = each.get_points()
            temp_dict[each.get_rating()] = [tm, pl, wn, dn, lt, gf, ga, gd, pt]
        sorting_list.sort(reverse = True)
        for rating in sorting_list:
            self.table.append(temp_dict[rating])

    def print_table(self):
        pad_char = ' '
        l1 = pad_string('Team', 15, pad_char)
        l2 = pad_string('Played', 7, pad_char)
        l3 = pad_string('Won', 4, pad_char)
        l4 = pad_string('Drawn', 6, pad_char)
        l5 = pad_string('Lost', 5, pad_char)
        l6 = pad_string('GF', 4, pad_char)
        l7 = pad_string('GA', 4, pad_char)
        l8 = pad_string('GD', 4, pad_char)
        l9 = pad_string('Points', 6, pad_char)
        print('   %s%s%s%s%s%s%s%s%s' % (l1,l2,l3,l4,l5,l6,l7,l8,l9))
        i = 0
        for each in self.table:
            i += 1
            if each[0] == self.player_team.get_name():
                tn = each[0].upper()
            else:
                tn = each[0]
            d0 = pad_string(str(i), 3, pad_char)
            d1 = pad_string(tn, 15, pad_char)
            d2 = pad_string(str(each[1]), 7, pad_char)
            d3 = pad_string(str(each[2]), 4, pad_char)
            d4 = pad_string(str(each[3]), 6, pad_char)
            d5 = pad_string(str(each[4]), 5, pad_char)
            d6 = pad_string(str(each[5]), 4, pad_char)
            d7 = pad_string(str(each[6]), 4, pad_char)
            d8 = pad_string(str(each[7]), 4, pad_char)
            d9 = pad_string(str(each[8]), 6, pad_char)
            print('%s%s%s%s%s%s%s%s%s%s' % (d0,d1,d2,d3,d4,d5,d6,d7,d8,d9))
            for team in self.teams:
                if tn.lower() == team.get_name().lower():
                    team.set_position(i)

    def play_match(self, team1, team2, announce=True, debug=False):
        result = match.Match(team1, team2, self.week_num, announce, debug)
        if team1 == self.player_team or team2 == self.player_team:
            announce = True
            result.menu()
        else:
            result.play_match()
        team1.add_match_played(result)
        team2.add_match_played(result)
        self.update_table()
        return result

    def play_week(self):
        sched = self.schedule[self.week_num]
        results = []
        for match in sched:
            announce = False
            results.append(self.play_match(sched[match][0], sched[match][1], announce=announce))
        self.week_played = True
        if self.week_num + 1 not in self.schedule:
            self.season_complete = True
            print("The season is complete. There are no more matches.")

    def advance_week_num(self):
        sched = self.schedule[self.week_num]
        if not self.season_complete:
            self.week_num += 1
            self.week_played = False
        else:
            print("The season is complete. There are no more matches.")
            self.season_complete = True

    def round_robin(self, group):
        g1 = []
        g2 = []
        half = int(len(group) / 2)
        for i in range(0, int(len(group) - half)):
            g1.append(group[i])
            g2.append(group[i + half])
            i += 1
        g2 = list(reversed(g2))
        return g1, g2

    def create_schedule(self, verbose=False):
        group = []
        group.extend(self.teams)
        if len(group) % 2 > 0: group.append('BYE')
        schedule = {}
        for i in range(1, len(group) + 1):
            matches = {}
            g1, g2 = self.round_robin(group)
            # print(g1,g2)
            group.append(group.pop(0))
            for j in range(len(g1)):
                matches[j + 1] = [g1[j], g2[j]]
            schedule[i] = matches
        self.schedule = schedule

    def set_manager_name(self, name):
        self.manager_name = name

    def get_manager_name(self):
        return self.manager_name

    def report_schedule(self):
        for each in self.schedule:
            print("\nWeek %d" % (each))
            for every in self.schedule[each]:
                vals = self.schedule[each][every]
                print("%s(H) plays %s" % (vals[0].get_name(), vals[1].get_name()))

    def set_new_season(self):
        print('\nFinal Table')
        self.print_table() #  Run to populate last position in each team
        for team in self.teams:
            team.set_new_season(self.year, self.name)
        self.week_num = 1
        self.week_played = False
        self.season_complete = False
        self.schedule = None
        self.create_schedule()
        self.table = []
        self.update_table()
        self.year += 1
        print('\nStarting the %d year season.' % self.year)

    def menu(self):
        #  TODO View the table
        run_run = True
        print("League Menu\n")
        while run_run:
            print('Options:')
            print('List the (S)chedule')
            print("(B)ack to the main menu")
            if self.player_team is None:
                print("(C)hoose a team")
            else:
                print("(M)anager Menu")
            command = get_response()
            if command == 's':  # Schedule
                self.report_schedule()
            elif command == 'm':  # Manager Menu
                self.manager_menu()
            elif command == 'c':  # Choose a team
                keep_going = True
                if keep_going:
                    print("\nDo you want a list of available teams?")
                    if get_response() == 'y':
                        for each in self.teams:
                            print(each.get_name())
                    print("\nType the name of a team")
                    r = get_long_response()
                    for each in self.teams:
                        if r == each.get_name().lower():
                            self.player_team = each
                            print("You now have control of %s" % self.player_team.get_name())
                            if self.manager_name is not None:
                                self.player_team.manager.set_name(self.manager_name)
                            keep_going = False
            elif command == 'b':  # Back
                run_run = False
            else: print("Eh? What was that?")

    def manager_menu(self):
        #  TODO Sub in and out a player
        run_run = True
        print("\nManager Console")
        while run_run:
            print('\nChoose an option:')
            if self.week_played is False: print('(P)lay the week')
            if self.week_played and not self.season_complete: print('(A)dvance the week')
            if self.season_complete: print('Start a new (S)eason')
            if len(self.table) > 0: print('Print (T)able')
            print('(B)ack to the League Menu')
            command = get_response()
            if command == 'p' and self.week_played is False: #  Play the week
                self.play_week()
            elif command == 'a' and self.week_played and not self.season_complete:  #  Advance the week
                self.advance_week_num()
            elif command == 'b':  # Back to League
                run_run = False
            elif command == 't':
                self.print_table()
            elif command == 's':
                self.set_new_season()
            else: print("Didn't get that? %s?" % command)



