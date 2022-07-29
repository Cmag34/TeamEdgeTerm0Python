from curses import mouseinterval


class Superhero:
    def __init__(self,power,name, years_of_experience,partners,mortal_enemy,health_points):
        self.power = power
        self.name = name
        self. years_of_experience = years_of_experience
        self.partners = partners
        self.mortal_enemy = mortal_enemy
        self.health_points = health_points
        #self.attack_damage = damage

    def intro(self):
        return f"Name: {self.name},power:{self.power},mortal enemy:{self.mortal_enemy}"

    def attack(self,enemy):
        enemy.health_points = enemy.health_points-1
    
    def heal(self):
        self.health_points = self.health_points+1

        
    def defense(self):
        self.health_points = self.health_points+0

    def is_alive(self,enemy):   
        self.is_alive() and enemy.is_alive()
        self.attack(enemy)
        enemy.attack(self)
        #if self.is_alive():
        #print:

werewolf = Superhero("Wherewolf", "Wolverine",4,["Silver Surfer","Poison Ivy","Wonder Woman"],"Red Skull",10 )