import random
import time
import uuid

from tools.utilities import get_response

home_field_advantage_amt = .05
chatty = .13  # What propensity do the announcers have for commentating?

goal_quips = ["slot it in!",
              "put it in the back of the net!",
              "have their way of it and grab a goal!",
              "see it home!",
              "have one to add to the tally sheets!",
              "slot it in!",
              "take the chance!"]


class Match(object):
    def __init__(self, home_team, visiting_team, week_num, cant_tie=False, home_field_advantage=False,
                 announce=False, debug=False):
        self.id = uuid.uuid1()
        self.home_team = home_team
        self.visiting_team = visiting_team
        self.home_team_id = home_team.get_id()
        self.visiting_team_id = visiting_team
        self.week_num = week_num
        self.home_score = 0
        self.visiting_score = 0
        self.winning_team = 'na'
        self.losing_team = 'na'
        self.cant_tie = cant_tie
        self.log = []
        self.announce = announce
        self.attendance = 0
        self.gate_reciepts = 0
        self.announce = announce
        self.debug = debug
        self.home_field_advantage = home_field_advantage
        self.match_played = False

    def print_log(self, txt):
        self.log.append(txt)
        if self.announce:
            print(txt)

    def play_match(self):
        score_h = 0
        score_v = 0
        home_name = self.home_team.get_name()
        visiting_name = self.visiting_team.get_name()
        self.print_log("Welcome to today's match of the home team %s against %s. The teams are ready to start." %
                       (home_name, visiting_name))
        self.print_log("Let's have a look at the numbers before we kick it off.")
        # Attacking Ayalysis
        if self.home_team.attack_value() > self.visiting_team.defense_value() * 1.3:
            if self.visiting_team.attack_value() > self.home_team.defense_value() * 1.3:
                self.print_log("Both teams have established their power in the attack."
                               " It should be a high scoring match.")
            else:
                self.print_log("%s has a leg up with their significant attacking power." % home_name)
        elif self.visiting_team.attack_value() > self.home_team.defense_value() * 1.3:
            self.print_log("%s has a leg up with their significant attacking power." % visiting_name)
        else:
            self.print_log("Neither team show significant promise from the attack."
                           " It should be a low scoring match.")
        # Midfield Analysis
        if self.home_team.mid_value() > self.visiting_team.mid_value() * 1.3:
            self.print_log("%s should rule the midfield based on their current form." % home_name)
        elif self.visiting_team.mid_value() > self.home_team.mid_value() * 1.3:
            self.print_log("%s should rule the midfield based on their current form." % visiting_name)
        else:
            self.print_log("The teams are about equal in the midfield.")
        # Keeper Analysis
        if self.home_team.keeping_value() > self.visiting_team.keeping_value() * 1.3:
            self.print_log("And finally, %s has the better keeper of these two teams." % home_name)
        elif self.visiting_team.keeping_value() > self.home_team.keeping_value() * 1.3:
            self.print_log("And finally, %s has the better keeper of these two teams." % visiting_name)
        else:
            self.print_log("And finally, the teams are about equal inside the goal.")
        quips = ["All of that is on paper, though. Let\'s see what reality has to say.",
                 "I am sure this one will go down in the books as quite the show.",
                 "There's nothing more to say.",
                 "If history is any indicator, there is no predicting the outcome today.",
                 "The football gods are capricious, however, and so all of that is meaningless on the pitch."]
        self.print_log(random.choice(quips))
        self.print_log("Let's get right to the action.")
        # TODO Add any starting modifiers to match including team talks, injuries
        # TODO Add apps and starts to all starters
        tmp_score_h, tmp_score_v = self.match_engine('H')
        score_h += tmp_score_h
        score_v += tmp_score_v
        # TODO Add any halftime modifiers to match including team talks, cards and send-offs, injuries, subs
        # TODO Add apps and subs to all subs
        tmp_score_h, tmp_score_v = self.match_engine('V')
        score_h += tmp_score_h
        score_v += tmp_score_v
        # TODO Calculate injuries, and cards
        if self.cant_tie:
            pass  # TODO add extra time and shootouts
        if score_h > score_v:
            self.winning_team = home_name
            self.losing_team = visiting_name
            self.print_log("%s wins with %d to %d!" % (home_name, score_h, score_v))
        elif score_v > score_h:
            self.winning_team = visiting_name
            self.losing_team = home_name
            self.print_log("%s wins with %d to %d!" % (visiting_name, score_v, score_h))
        else:
            self.winning_team = 'Tie'
            self.losing_team = 'Tie'
            self.print_log("%s and %s tie at %d!" % (home_name, visiting_name, score_h))
        # TODO Add cleansheet to keeper
        self.home_score = score_h
        self.visiting_score = score_v
        # set the references of teams to team names
        self.home_team = home_name
        self.visiting_team = visiting_name
        self.match_played = True

    def get_scores(self):
        return self.home_score, self.visiting_score

    def report_scores(self, verbose=False):
        if verbose:
            print("In the match played between %s, at home, and %s, visiting," % (self.home_team,
                                                                                  self.visiting_team))
        if self.winning_team is not "Tie":
            print("%s beat %s by %d goals" % (self.winning_team, self.losing_team,
                                              abs(self.home_score - self.visiting_score)))
        else:
            print("The match between %s and %s ended in a tie" % (self.home_team,
                                                                  self.visiting_team))

    def replay_match(self):
        for each in self.log:
            print(each)

    def menu(self):
        #  TODO Set formation
        #  TODO Sub players
        #  TODO Play match
        print('Welcome to week %d. The home team, %s, plays %s.' % (self.week_num, self.home_team.get_name(),
                                                                   self.visiting_team.get_name()))
        print('\nMatch Menu')
        run_run = True
        while run_run:
            print('\nChoose and option:')
            if not self.match_played:
                print('(A)ttend the match')
                print('(S)kip the match')
            print('Go (B)ack to the League menu')
            command = get_response()
            if command == 's' and not self.match_played:  # Play match without announc
                self.announce = False
                self.play_match()
            elif command == 'a' and not self.match_played:  # Play match with announce
                self.announce = True
                self.play_match()
            elif command == 'b':  # Back to League menu
                run_run = False
            else:
                print("Wanna say that again? But better?")

    def match_engine(self, side_kicks_off, mins_to_play=45):
        """
        Calculates scoring events based on predetermined odds. Usually, this will represent a half of a match.
        Adapted from Geraldo Xexeo's Machinations Soccer diagram.
        :param side_kicks_off: 'H' or 'V' depending on which side kicks off
        :param mins_to_play: number of 'ticks' used for scoring events. Defaults to 45
        :return: Home_score, Visitor_score
        """
        use_mods = True
        position = 0  # -1 to +1 where 0 is midfield and +/- is attack
        score_h = 0
        score_v = 0
        h_att = self.home_team.attack_value()
        h_mid = self.home_team.mid_value()
        h_def = self.home_team.defense_value()
        h_kpr = self.home_team.keeping_value()
        v_att = self.visiting_team.attack_value()
        v_mid = self.visiting_team.mid_value()
        v_def = self.visiting_team.defense_value()
        v_kpr = self.visiting_team.keeping_value()
        self.area_values = {'h_att': h_att, 'h_mid': h_mid, 'h_def': h_def, 'h_kpr': h_kpr,
                            'v_att': v_att, 'v_mid': v_mid, 'v_def': v_def, 'v_kpr': v_kpr}
        if side_kicks_off not in ['V', 'H']:
            print('Either V or H must kick off')
            raise AttributeError
        else:
            possession = side_kicks_off
        home_name = self.home_team.get_name()
        visiting_name = self.visiting_team.get_name()
        if self.announce: time.sleep(1)
        side = 'home' if side_kicks_off == 'H' else 'visitor'
        self.print_log("And there's the kick-off for the %s side." % side)
        if self.announce: time.sleep(1)

        for i in range(mins_to_play):
            r = random.random()
            chat = True if random.random() <= chatty else False
            if position == 0:  # Midfield
                if possession == 'H':  # Home controls the ball
                    # r modifier (Home positive mod would subtract from r)
                    if use_mods:
                        mod = (h_mid - v_mid) / 100
                        if self.home_field_advantage: mod -= home_field_advantage_amt
                        r -= mod
                    if r < .66:  # 66% chance to retain the ball
                        position = 1
                        if chat: self.print_log('The home side push forward with the ball, going on the offensive.')
                        if self.announce: time.sleep(.5)
                    else:
                        possession = 'V'  # Tackle or Interception
                        if chat: self.print_log('The visitors collect the ball at mid-field.')
                        if self.announce: time.sleep(.5)
                else:  # Visitor controls the ball
                    # r modifier (Visitor positive mod would subtract from r)
                    if use_mods:
                        mod = (v_mid - h_mid) / 100
                        if self.home_field_advantage: mod += home_field_advantage_amt
                        r -= mod
                    if r < .66:  # 66% chance to retain the ball
                        position = -1
                    else:
                        possession = 'H'  # Tackle or Interception
            elif position > 0:  # On the visitor side of the pitch (H=Attack, V=Defend)
                if possession == 'H':  # Home on the attack
                    # r modifier (Home positive mod would subtract from r)
                    if use_mods:
                        mod = (h_att - ((v_def * 2) + v_kpr)) / 3 / 100
                        if self.home_field_advantage: mod -= home_field_advantage_amt
                        r -= mod
                    if r < .2:  # 20% chance to score a goal
                        score_h += 1
                        position = 0
                        possession = 'V'
                        self.print_log("%s %s" % (home_name, random.choice(goal_quips)))
                        # TODO add goal to goal scorer and assist
                    elif r < .6:  # 40% chance the goalkeep stopped the shot (.2 + .4)
                        possession = random.choice(['A', 'H'])  # Boots the ball
                        position = 0
                    else:  # 50% chance the defense gets the ball
                        possession = 'V'  # Tackle or Interception
                else:  # Visitors on the defense
                    # r modifier (Visitor positive mod would subtract from r)
                    if use_mods:
                        mod = (v_def - (h_att + h_mid)) / 2 / 100
                        if self.home_field_advantage: mod += home_field_advantage_amt
                        r -= mod
                    if r < .6:  # 60% chance to retain the ball
                        position = 0
                    elif r < .8:  # 20% chance Home Midfield gets the ball (.6 + .2)
                        position = 0
                        possession = 'H'
                    else:  # 20% chance Home Attackers get the ball
                        possession = 'H'  # Tackle or Interception
            else:  # On the Home side of the pitch (V=Attack, H=Defend)
                if possession == 'V':  # Visitors on the attack
                    # r modifier (Visitor positive mod would subtract from r)
                    if use_mods:
                        mod = (v_att - ((h_def * 2) + h_kpr)) / 3 / 100
                        if self.home_field_advantage: mod += home_field_advantage_amt
                        r -= mod
                    if r < .2:  # 20% chance to score a goal
                        score_v += 1
                        position = 0
                        possession = 'H'
                        self.print_log("%s %s" % (visiting_name, random.choice(goal_quips)))
                        # TODO add goal to goal scorer and assist
                    elif r < .6:  # 40% chance the goalkeep stopped the shot (.1 + .5)
                        possession = random.choice(['A', 'H'])  # Boots the ball
                        position = 0
                    else:  # 50% chance the defense gets the ball
                        possession = 'H'  # Tackle or Interception
                else:  # Home on the defense
                    # r modifier (Home positive mod would subtract from r)
                    if use_mods:
                        mod = (h_def - (v_att + v_mid)) / 2 / 100
                        if self.home_field_advantage: mod -= home_field_advantage_amt
                        r -= mod
                    if r < .6:  # 60% chance to retain the ball
                        position = 0
                    elif r < .8:  # 20% chance Visitors' Midfield gets the ball (.6 + .2)
                        position = 0
                        possession = 'V'
                    else:  # 20% chance Home Visitors' get the ball
                        possession = 'V'  # Tackle or Interception
        return score_h, score_v
