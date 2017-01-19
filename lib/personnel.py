import uuid
import random

valid_terms = {'manager':['mgr','manager'],
               'coach':['coach'],
               'physio':['physio','doctor','trainer'],
               'scout':['scout', ',scouter']}



class Personnel(object):
    def __init__(self, **kwargs):
        if kwargs is not None:
            #  = kwargs[''] if '' in kwargs else ''
            self.name = kwargs['name'] if 'name' in kwargs else "no name"
            self.surname = kwargs['surname'] if 'surname' in kwargs else "no surname"
            self.age = kwargs['age'] if 'age' in kwargs else 0
            self.position = kwargs['position'] if 'position' in kwargs else 'Manager'
            self.nationality = kwargs['nationality'] if 'nationality' in kwargs else 'United States'
            self.gender = kwargs['gender'] if 'gender' in kwargs else 'Male'
            self.rating = kwargs['rating'] if 'rating' in kwargs else 1  # 1-99 high = best
            self.rating_forward = kwargs['rating_forward'] if 'rating_forward' in kwargs else 1  # 1-99 high = best
            self.salary = kwargs['salary'] if 'salary' in kwargs else 60000  # dollars per year USD
            self.value = kwargs['value'] if 'value' in kwargs else 70000  # dollars to trade USD
            self.fame = kwargs['fame'] if 'fame' in kwargs else "Local"
            self.club_history = kwargs['club_history'] if 'club_history' in kwargs else []
            self.id = str(uuid.uuid1())

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

    def get_nationality(self):
        return self.nationality

    def get_gender(self):
        return self.gender

    def get_rating(self):
        return self.rating

    def get_salary(self):
        return self.salary

    def get_value(self):
        return self.value

    def get_club_history(self):
        return self.club_history

    def report_club_history(self):
        for each in self.club_history:
            print(each)

    def move_club(self,new_club_name):
        self.club_history.append(new_club_name)

    def set_name(self, f_l_name_list):
        self.name = f_l_name_list[0]
        self.surname = f_l_name_list[1]

