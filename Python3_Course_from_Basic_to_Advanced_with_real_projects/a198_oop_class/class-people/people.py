from datetime import datetime


class People:
    current_year = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, name, age, eating=False, talking=False):
        self.name = name
        self.age = age
        self.eating = eating
        self.talking = talking

    def to_talk(self, subject):
        # If self.eating == True and self.talking == True
        if self.eating:
            print(f"{self.name} can't talk and eat.")
            return
        # If self.talking == True
        if self.talking:
            print(f'{self.name} already talking.')
            return

        print(f'{self.name} is talking about {subject}.')
        self.talking = True

    def stop_talking(self):
        # If self.talking == False
        if not self.talking:
            print(f'{self.name} is not talking')
            return

        print(f'{self.name} stopped talking.')
        self.talking = False

    def to_eat(self, food):
        if self.eating:
            print(f'{self.name} already eating.')
            return

        if self.talking:
            print(f"{self.name} can't eating and talking.")
            return

        print(f'{self.name} is eating {food}.')
        self.eating = True

    def stop_eating(self):
        # If self.eating == False
        if not self.eating:
            print(f'{self.name} is not eating.')
            return
        # If self.eating == True
        print(f'{self.name} stop eating.')
        self.eating = False

    def get_birth_date(self):
        return self.current_year - self.age
