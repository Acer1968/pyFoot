import random
import uuid

import personnel

from lib import player
from tools import lists, utilities

base_team = {'Keeper': ['Center', 'Goal'],
             'Left Forward': ['Left', 'Forward'],
             'Striker': ['Center','Forward'],
             'Left Mid': ['Left', 'Mid'],
             'Left Center Mid': ['Center', 'Mid'],
             'Right Center Mid': ['Center', 'Mid'],
             'Right Mid': ['Right', 'Mid'],
             'Left Back': ['Left', 'Back'],
             'Left Center Back': ['Center', 'Back'],
             'Right Center Back': ['Center', 'Back'],
             'Right Back': ['Right', 'Back']}

class Team(object):
    def __init__(self, **kwargs):
        if kwargs is not None:
            self.name = kwargs['name'] if 'name' in kwargs else "no name"
            self.sample_team = kwargs['sample_team'] if 'sample_team' in kwargs else False  # Bool
            #self.sample_team = kwargs['sample_team'] if 'sample_team' in kwargs else False  # Bool
        self.id = uuid.uuid1()
        self.personnel = []
        self.manager = None
        self.players = []
        self.match_day_players = {'Forward':[],'Mid':[], 'Back':[], 'Goal':[], 'Bench': []}
        self.matches_played = []
        self.form = []
        self.position = 0
        self.history = {}
        self.stadium_seats = 20000
        self.ticket_price_average = 30
        self.funds = 1000000
        self.season_record = {'won':0, 'lost':0, 'drawn':0, 'played':0, 'goals_for':0, 'goals_against':0,
                              'goals_difference':0, 'points':0}
        if self.sample_team:
            for each in base_team:
                self.players.append(player.Player(name=lists.get_mens_name_distributed(),
                                                  surname=lists.get_last_name_distributed(),
                                                  position=each, area=base_team[each][1],
                                                  sided=base_team[each][0], age=random.randint(18,29),
                                                  rating=random.randint(10,35),
                                                  club_history = [self.get_name()]))
            self.manager = personnel.Personnel(name=lists.get_mens_name_distributed(),
                                               surname=lists.get_last_name_distributed(),
                                               position="Manager", age=random.randint(18,29),
                                               rating=random.randint(10,35),
                                               club_history = [self.get_name()])

    def __str__(self):
        for each in self.players:
            print("%s: Position: %s, Rating: %d, Value: %d" % (each.get_full_name(), each.position,
                                                               each.rating, each.value))
        return ""

    def area_value(self,area, match_day=False,effective=False):
        score = 0
        cnt = 0
        if match_day:
            group = self.match_day_players[area]
        else:
            group = []
            for player in self.players:
                if player.area == area: group.append(player)
        for each in group:
            if effective: score += each.get_position_effective_rating(area)
            else: score += int(each.rating)
            cnt += 1
        score = int(score / cnt)
        return score

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def attack_value(self,match_day=False,effective=False):
        return self.area_value("Forward", match_day, effective)

    def mid_value(self,match_day=False,effective=False):
        return self.area_value("Mid", match_day, effective)

    def defense_value(self,match_day=False,effective=False):
        return self.area_value("Back", match_day, effective)

    def keeping_value(self,match_day=False,effective=False):
        return self.area_value("Goal", match_day, effective)

    def list_injured_players(self):
        for each in self.players:
            each.report_health(only_if_injured=True)

    def get_name(self):
        return self.name

    def get_played(self):
        return self.season_record['played']

    def get_points(self):
        return self.season_record['points']

    def get_won(self):
        return self.season_record['won']

    def get_lost(self):
        return self.season_record['lost']

    def get_drawn(self):
        return self.season_record['drawn']

    def get_goals_for(self):
        return self.season_record['goals_for']

    def get_goals_against(self):
        return self.season_record['goals_against']

    def get_goals_difference(self):
        return self.season_record['goals_difference']

    def get_rating(self):
        points = self.get_points() * 1000000
        gd = self.get_goals_difference() * 100000
        gf = self.get_goals_for() * 100
        won = self.get_won()
        nm = utilities.convert_chars_to_ints(self.get_name().lower())
        nm = nm / int('1' + (len(str(nm)) * '0'))  # convert to a decimal
        return points + gd + gf + won + nm

    def add_match_played(self,match):
        self.matches_played.append(match)
        self.season_record['played'] += 1
        if match.winning_team == self.get_name():
            self.form.append('W')
            self.season_record['won'] += 1
        elif match.winning_team == 'Tie':
            self.form.append('D')
            self.season_record['drawn'] += 1
        else:
            self.form.append('L')
            self.season_record['lost'] += 1
        while len(self.form) > 5:
            null = self.form.pop(0)
        # score for and against (home / visitor)
        if match.home_team == self.get_name():
            self.season_record['goals_for'] += match.home_score
            self.season_record['goals_against'] += match.visiting_score
        else:
            self.season_record['goals_for'] += match.visiting_score
            self.season_record['goals_against'] += match.home_score
        # Goal diff & points
        gd = self.season_record['goals_for'] - self.season_record['goals_against']
        self.season_record['goals_difference'] = gd
        self.season_record['points'] = self.season_record['won'] * 3 + self.season_record['drawn']

    def get_id(self):
        return self.id

    def report_form(self):
        s = ''
        for eah in self.form:
            s += eah
        print("%s current form: %s" % (self.name, s))

    def add_history(self, current_year, league_name, position=None):
        pos = self.position if position is None else position
        self.history[current_year] = {'Year': current_year, 'Leage': league_name, 'Position': pos}

    def set_new_season(self, current_year, league_name):
        self.add_history(current_year, league_name)
        for player in self.players:
            player.set_new_season()
        for each in self.season_record:
            self.season_record[each] = 0
        self.matches_played = []
        self.form = []

    def team_management_menu(self):
        #  TODO Review current players
        #  TODO Review current form
        #  TODO Review current tactics
        #  TODO List available players
        #  TODO Buy Players
        #  TODO Sell Players
        #  TODO Loan Players
        #  TODO Set players as starters and subs
        #  TODO Change tactics
        #  TODO Manage finances
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
            if command == 'p' and self.week_played is False:  # Play the week
                self.play_week()
            elif command == 'a' and self.week_played and not self.season_complete:  # Advance the week
                self.advance_week_num()
            elif command == 'b':  # Back to League
                run_run = False
            elif command == 't':
                self.print_table()
            elif command == 's':
                self.set_new_season()
            else:
                print("Didn't get that? %s?" % command)
