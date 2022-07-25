

reply=" "
input_msg =""
rooms = []
location= ""
current_animal=""

class Room:
  def __init__(self, name=None, description=None, objects=None, paths=None):
    self.name = name
    self.description = description
    #self.objects = objects
    #self.paths = paths

class Animal:
    def __init__(self,name, type,notbuy,buy,groom, feed, shower):
        self.name = name
        self.type = type
        #5
        self.notbuy = notbuy
        #4
        self.buy = buy
        #3
        self.groom = groom
        #2
        self.feed = feed
        #1
        self.shower = shower
    
    def action_check(self, action):
        global current_animal
        if  action =="1":
            print(self.shower)

        elif action =="2":
            
            print(self.feed)
          
        elif action == "3":
            
            print(self.groom)
        elif action == "4":
            print(self.buy)
            
        elif action == "5": 
            prompt_user1()
           

class Player:
    def __init__(self,name,way_it_kills_you,):
        self.name = name
        self.alive = True
        self.way_you_die = way_it_kills_you


animal1 = Animal("Chichi","White Pomeranian","", "", "", "", "")
animal2 = Animal("Bib","Rat","", "", "", "", "")
animal3 = Animal("Gibit","Blob Fish ","", "", "", "", "")
player1 = Player("","")


def start():
  
    print("You are shopping for a pet. As you enter your'e greeted by an asistant that will guide you through the process of buying a pet. You have to interact with animals to decide to buy one. You vaguely notice that the entrance sevrly shuts behind you. The assitant contiunes to talk about the buying process and alerts you that the store is closing in 2 hours. Its now time to buy a pet!  ")
    name = input("What is your name, player? ")
    player1.name = name
    print("Welcome, " + name)
    pet_room= input("Which pet woudld you like to interact with? Select a number. Chichi(1)\nBib(2)\nGibit(3)) ")
  #pet_room = pet_room  
    if pet_room== "1":
        print(animal1room.description)
        current_animal=animal1
    elif pet_room== "2":
        print(animal2room.description)
        current_animal=animal2
    elif pet_room== "3":
        print(animal3room.description)
        current_animal=animal3
    else:
        print("Please type an option above")
    #global location=animal1room

def select_new_pet():
    pet_room= input("Which pet woudld you like to interact with? Select a number. Chichi(1)\nBib(2)\nGibit(3)) ")
  #pet_room = pet_room  
    if pet_room== "1":
        print(animal1room.description)
    elif pet_room== "2":
        print(animal2room.description)
    elif pet_room== "3":
        print(animal3room.description)
    else:
        print("Please type an option above")


animal1room = Room()
animal1room.name = "Chichi's Room"
animal1room.description = "Welcome to the Chichi's room!"

animal1.shower= "You've chosen to wash and groom Chichi!" "Chichi is estatic running in circles around you. Finally you manage to catch her and sumbmerge her in water.Chichi has now been washed."
animal1.feed="You've chosen to feed Chichi!Chichi adorably eats from your hands. You notice that she keeps nipping at your hands.Chichi burps in your face"
animal1.groom="You begin grooming Chichi after washing her. Suddenly, she starts to pee on your boots. Is she marking her territory? As your drying and grooming Chichi you notice that she is losing a lot of hair. Masses fall out as you brush the comb yet Chichi's hair remains as full and vibrant as it originaly was."
animal1.buy="You've chosen to buy Chichi! When you bring Chichi home she runs in circles around your home leaving a path of dirty paw marks and fluffy white fur. Right before bed you fill her food bowl. She vigorously eats like theres no tommorow. As your tucking yourself in, Chichi runs up to your bed and cuddles up next to you. \n The next morning... As you wake up you find it hard to breath. Your body remains incapacitated under a thick mass of white fure. All you see when you open your eyes in a panic is white. It feels imposisble to breath. You slowly die of suffocation as Chichi pounces over your frozen body. Cause of death: Chichi's excessive fur"
animal1.notbuy=" "


animal2room = Room()
animal2room.name = "Bib's Room"
animal2room.description = ("Welcome to the Bib's room!")
animal2.shower= ("You've chosen to wash and groom Bib!" "As you wash Bib he keeps slipping through your fingers. Who knew washing a rat would be so annoyingly hard?")
animal2.feed=("You've chosen to feed Bib!Bib adorably eats from your hands. As Bib eats you realize hes consuming a huge amount of food in a few seconds")
animal2.groom=("Grooming Bib is quite easy due to his short hair. But he clealry lacks the ability to stay still so you end up running after him in his cage")
animal2.buy="Bib becomes your best friend /n Cause of Death: n/a "
animal2.notbuy=""

animal3room = Room()
animal3room.name = "Gibbit's Room"
animal3room.description = ("Welcome to the Gibbit's room!")
animal3.shower= ("You've chosen to wash Gibbit!""Due to Gibit's weight their unable to move about much. Gibbit sits like deadweight as you rub water and soap on it. After a little bit you realize gibbit's skin color is slowly starting to match your own skin tone. ")
animal3.feed=("You pour food into Gibbits mouth. And he gobbles it up.")
animal3.groom=("Petting Gibbit is like petting a dolphin. His skin remains soft and smooth. As you pet him his skin starts to slowly match your skin tone.")
animal3.buy=("At home you deposit Gibit into a tub with water. As a bit of a useless fish he just slowlyt floats around. You bring him food and he muches slowly as you brush your teeth. As the days pass by you notice Gibbit is starting move faster and becoming better at swimming. After a few days Gibbit is able to move around the like a snail. After a week Gibbit is kind of walking aroound the house. Somehow he developed two smnall stubby legs and bumpys that may represnet arms? A month later: You wake up to extreme pressure around your neck. As your eyes flutter open your 9face stares back at you. You realize the arms starggling you are attached to that face. Not long after you black out. /n Cause of death: Your pet has copied your every aspect and decided to replace you in the world. Your pet now lives happily as you")
animal3.notbuy=""

start()

def prompt_user():
    future_actions= input("How would you like to interact with this pet? Select a number. Shower(1)\nGroom(2)\nFeed(3)\n Buy Pet(4) \n Don't Buy Pet(5))>>  ")
    print(future_actions)
    return future_actions

def prompt_user1():
    future_pet= input("Would you like to move on to another pet(1) or continue interacting with this pet(2)? Select a number. >>")
    print(future_pet)
    if future_pet=="1":
        select_new_pet()
    elif future_pet=="1":
        prompt_user()
    return future_pet









while player1.alive==True:
    #global current_animal
    #animal1.action_check(prompt_user())
    current_animal.action_check(prompt_user())






