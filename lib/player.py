import uuid
import random
import math

valid_terms = {'forward':['attack','forward','striker'],
               'mid':['mid','middle'],
               'back':['back','defense','def'],
               'goal':['goal', ',keep', 'keeper']}

# Health levels attributes: Level, number equivalent (and below), chance to recover
health_levels = {'Hospitalized':[10,.05],
                 'Seriously Injured':[30,.3],
                 'Slighly Injured':[50,.7],
                 'Bruised':[60,.95],
                 'Winded':[75,.99],
                 'Healthy':[99,1]}
health_levels_top = 'Healthy'
health_levels_injured = ['Hospitalized', 'Seriously Injured', 'Slighly Injured']



class Player(object):
    def __init__(self, **kwargs):
        if kwargs is not None:
            #  = kwargs[''] if '' in kwargs else ''
            self.name = kwargs['name'] if 'name' in kwargs else "no name"
            self.surname = kwargs['surname'] if 'surname' in kwargs else "no surname"
            self.age = kwargs['age'] if 'age' in kwargs else 0
            self.position = kwargs['position'] if 'position' in kwargs else 'Bench'
            self.sided = kwargs['sided'] if 'sided' in kwargs else 'Center' # Left, Center, Right
            self.area = kwargs['area'] if 'area' in kwargs else 'Mid' # Back, Mid, Forward, Goal
            self.nationality = kwargs['nationality'] if 'nationality' in kwargs else 'United States'
            self.gender = kwargs['gender'] if 'gender' in kwargs else 'Male'
            self.footed = kwargs['footed'] if 'footed' in kwargs else 'Right'
            # self.fitness = kwargs['fitness'] if 'fitness' in kwargs else 50  # 1-99 high = fit
            self.health = kwargs['health'] if 'health' in kwargs else 99  # 1-99 high = healthy
            self.health_level =  kwargs['health_level'] if 'health_level' in kwargs else "Healthy"
            self.rating = kwargs['rating'] if 'rating' in kwargs else 1  # 1-99 high = best
            self.rating_forward = kwargs['rating_forward'] if 'rating_forward' in kwargs else 1  # 1-99 high = best
            self.rating_mid = kwargs['rating_mid'] if 'rating_mid' in kwargs else 1  # 1-99 high = best
            self.rating_back = kwargs['rating_back'] if 'rating_back' in kwargs else 1  # 1-99 high = best
            self.rating_goal = kwargs['rating_goal'] if 'rating_goal' in kwargs else 1  # 1-99 high = best
            self.salary = kwargs['salary'] if 'salary' in kwargs else 20000  # dollars per year USD
            self.fame = kwargs['fame'] if 'fame' in kwargs else "Local"
            self.club_history = kwargs['club_history'] if 'club_history' in kwargs else []
            self.apps = {'season':0, 'career':0}
            self.starts = {'season':0, 'career':0}
            self.subs = {'season':0, 'career':0}
            self.goals = {'season':0, 'career':0}
            self.assists = {'season': 0, 'career': 0}
            self.clean_sheets = {'season':0, 'career':0}
            self.id = str(uuid.uuid1())

            # Add ratings for nearby areas
            if 'rating_forward' in kwargs:
                if 'rating_mid' not in kwargs: self.rating_mid += int(self.rating_forward * .3)
            if 'rating_mid' in kwargs :
                if 'rating_forward' not in kwargs: self.rating_forward += int(self.rating_mid * .3)
                if 'rating_back' not in kwargs: self.rating_back += int(self.rating_mid * .3)
            if 'rating_back' in kwargs:
                if 'rating_mid' not in kwargs: self.rating_mid += int(self.rating_back * .3)
                if 'rating_goal' not in kwargs: self.rating_goal += int(self.rating_back * .1)
            if 'rating_goal' in kwargs:
                if 'rating_back' not in kwargs: self.rating_back += int(self.rating_goal * .3)

    def report_health(self, only_if_injured=False):
        if only_if_injured is False or self.health_level in health_levels_injured:
            print("%s is now %s" % (self.get_full_name(), self.get_health_level()))

    def add_app(self):
        self.apps['season'] += 1
        self.apps['career'] += 1

    def get_apps_season(self):
        return self.apps['season']

    def get_apps_career(self):
        return self.apps['career']

    def add_start(self):
        self.starts['season'] += 1
        self.starts['career'] += 1

    def get_starts_season(self):
        return self.starts['season']

    def get_starts_career(self):
        return self.starts['career']

    def add_sub(self):
        self.subs['season'] += 1
        self.subs['career'] += 1

    def get_subs_season(self):
        return self.subs['season']

    def get_subs_career(self):
        return self.subs['career']

    def add_goals(self):
        self.goals['season'] += 1
        self.goals['career'] += 1

    def get_goals_season(self):
        return self.goals['season']

    def get_goals_career(self):
        return self.goals['career']

    def add_assist(self):
        self.assists['season'] += 1
        self.assists['career'] += 1

    def get_assists_season(self):
        return self.assists['season']

    def get_assists_career(self):
        return self.assists['career']

    def add_clean_sheet(self):
        self.clean_sheets['season'] += 1
        self.clean_sheets['career'] += 1

    def get_clean_sheets_season(self):
        return self.clean_sheets['season']

    def get_clean_sheets_career(self):
        return self.clean_sheets['career']

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_id(self):
        return self.id

    def get_first_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_age(self):
        return self.age

    def increment_age(self, verbose=False):
        self.age += 1
        if verbose: print("%s is %d years old." % (self.get_first_name(), self.get_age()))

    def get_position(self):
        return self.position

    def get_sided(self):
        return self.sided

    def get_area(self):
        return self.area

    def get_position_rating(self, area):
        if area.lower() in valid_terms['forward']:
            return self.rating_forward
        elif area.lower() in valid_terms['mid']:
            return self.rating_mid
        elif area.lower() in valid_terms['back']:
            return self.rating_back
        elif area.lower() in valid_terms['goal']:
            return self.rating_goal
        else:
            print("%s is now a valid area. Use forward, mid, back, or goal" % (str(area)))
            return None

    def get_nationality(self):
        return self.nationality

    def get_gender(self):
        return self.gender

    def get_footed(self):
        return self.footed

    def get_health(self):
        return self.health

    def get_health_level(self):
        return self.health_level

    def set_rating(self):
        if self.area.lower() == 'back':
            self.rating = min(99, self.rating_back + (self.rating_forward + self.rating_goal + self.rating_mid) / 3)
        elif self.area.lower() == 'forward':
            self.rating = min(99, self.rating_forward + (self.rating_back + self.rating_goal + self.rating_mid) / 3)
        elif self.area.lower() == 'goal':
            self.rating = min(99, self.rating_goal + (self.rating_back + self.rating_forward + self.rating_mid) / 3)
        elif self.area.lower() == 'mid':
            self.rating = min(99, self.rating_mid + (self.rating_back + self.rating_goal + self.rating_forward) / 3)
        else:
            self.rating = 10

    def get_rating(self):
        return self.rating

    def get_salary(self):
        return self.salary

    def get_value(self):
        value = 0
        # TODO Add value calc
        # Goals?
        # Rating?
        # Position?
        # Age?
        # Fame?
        # ?
        return value

    def get_club_history(self):
        return self.club_history

    def report_club_history(self):
        for each in self.club_history:
            print(each)

    def move_club(self,new_club_name):
        self.club_history.append(new_club_name)

    def get_position_effective_rating(self, area):
        if 1 <= self.rating <= 99:
            if area.lower() in valid_terms['forward']:
                return int(self.rating_forward * (self.get_health() / 100))
            elif area.lower() in valid_terms['mid']:
                return int(self.rating_mid * (self.get_health() / 100))
            elif area.lower() in valid_terms['back']:
                return int(self.rating_back * (self.get_health() / 100))
            elif area.lower() in valid_terms['goal']:
                return int(self.rating_goal * (self.get_health() / 100))
            else:
                print("%s is now a valid area. Use forward, mid, back, or goal" % (str(area)))
                return None
        else:
            print("%s is not an appropriate rating, which should be an integer between 1 and 99." % (str(self.rating)))
            return None

    def set_health_level(self):
        tmp = health_levels_top
        for each in health_levels:
            if self.health <= health_levels[each][0] < health_levels[tmp][0]: tmp = each
        self.health_level = tmp

    def fatigue(self, amount, verbose=False):
        self.health = 1 if self.get_health() - amount < 1 else self.get_health() - amount
        self.set_health_level()
        if verbose: self.report_health()

    def heal(self, verbose=False, heal_chance_multiplier=1):
        if self.health < 99:
            heal_chance = random.random() * heal_chance_multiplier
            heal_biscuit = random.randint(10,99-self.health)
            if heal_chance <= health_levels[self.health_level][1]:
                self.health += heal_biscuit
                self.set_health_level()
                if verbose:
                    print("%s's condition has improved. He is now %s" % (self.get_full_name(), self.get_health_level()))
        else:
            if verbose: print("%s is already in tip-top shape.")

    def set_new_season(self):
        self.apps['season'] = 0
        self.starts['season'] = 0
        self.subs['season'] = 0
        self.goals['season'] = 0
        self.clean_sheets['season'] = 0
        self.health = 99
        self.set_health_level()
        self.increment_age()
        self.set_rating()
        # Improvements
        if random.randint(1,99) < self.rating_back:
            room_to_grow = 99 - self.rating_back
            self.rating_back += min(math.ceil(room_to_grow * .5), room_to_grow)
        if random.randint(1,99) < self.rating_forward:
            room_to_grow = 99 - self.rating_forward
            self.rating_forward += min(math.ceil(room_to_grow * .5), room_to_grow)
        if random.randint(1,99) < self.rating_goal:
            room_to_grow = 99 - self.rating_goal
            self.rating_goal += min(math.ceil(room_to_grow * .5), room_to_grow)
        if random.randint(1,99) < self.rating_mid:
            room_to_grow = 99 - self.rating_mid
            self.rating_mid += min(math.ceil(room_to_grow * .5), room_to_grow)

