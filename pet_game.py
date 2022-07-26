

reply=" "
input_msg =""
rooms = []
location= ""
current_animal=""
bag=""

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
        self.shower = shower
    
    def action_check(self, action):
        
        if  action =="1":
            print(self.shower)

        elif action =="2":
            
            print(self.feed)
          
        elif action == "3":
            
            print(self.groom)
        elif action == "4":
            print(self.buy)
            player1.alive==False
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
    global current_animal
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
    global current_animal
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

def future_room():
    global current_animal
    global bag
    room_inside= input("How you you like to interact with this pets room? Select a number.look(1)\ntouch(2)\ncollect(3)>>> ) ")
  #pet_room = pet_room  
    if room_inside== "1"and current_animal==animal1:
        print(animal1.look)
    # if room_inside== "1"and current_animal==animal2:
    #     print(animal2.look)
    # if room_inside== "1"and current_animal==animal3:
    #     print(animal3.look)
    if room_inside== "2"and current_animal==animal1:
        touch_user_input=input(animal1.touch) 
        if touch_user_input== 1:     
            print(animal1.rug)
        if touch_user_input== 2:     
            print(animal1.metal_bowls)
        if touch_user_input== 3:     
            print(animal1.chichi_bed)
            animal1_item_list.append("Golden Coin")
    # if room_inside== "2"and current_animal==animal2:
    #     print(animal2.touch)
    # if room_inside== "2"and current_animal==animal3:
    #     print(animal3.touch)
    if room_inside== "3"and current_animal==animal1:
        print(animal1.collect)  

    # if room_inside== "3"and current_animal==animal2:
    #     print(animal2.collect)
    # if room_inside== "3"and current_animal==animal3:
    #     print(animal3.collect)
    
    
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
animal1.look="You look around Chichi's room. Its a small compact space littered with white hair. There is a rug and on top of it sits Chichi's bed. By the door are two samll metal bowls for food anbd water."
animal1.touch="Would you like to inspect any of the items in the room. Select a number to interact with that item.\n Rug(1) \n Metal Bowls \n Chichi's bed "

animal1.rug="You lift up the rug and are greeted by a blank slate of concrete"
animal1.metal_bowls="You lift up the the metal food and water bowl. There is nothing underneath."
animal1.chichi_bed="You lift up Chichi's bed. Underneath you find a gold coin.  "

#would you like to collect it?Select a number.\n Yes(1) \n No(2)
#animal1_item_list.append 
animal1_item_list= [" Rug(1)" "Metal Bowls(2)" "Chichi's bed(3)"]
animal1.collect=(f"Would you like to collect an item. Select a number. {animal1_item_list}>>> ")


animal2room = Room()
animal2room.name = "Bib's Room"
animal2room.description = ("Welcome to the Bib's room!")
animal2.shower= ("You've chosen to wash and groom Bib!" "As you wash Bib he keeps slipping through your fingers. Who knew washing a rat would be so annoyingly hard?")
animal2.feed=("You've chosen to feed Bib!Bib adorably eats from your hands. As Bib eats you realize hes consuming a huge amount of food in a few seconds")
animal2.groom=("Grooming Bib is quite easy due to his short hair. But he clealry lacks the ability to stay still so you end up running after him in his cage")
animal2.buy=" You live happily ever after with Bib as your best friend.\n Cause of Death: n/a "
animal2.notbuy=""
animal2.look="You see a big room"
animal2.touch=""
animal2.collect=""

animal3room = Room()
animal3room.name = "Gibbit's Room"
animal3room.description = ("Welcome to the Gibbit's room!")
animal3.shower= ("You've chosen to wash Gibbit!""Due to Gibit's weight their unable to move about much. Gibbit sits like deadweight as you rub water and soap on it. After a little bit you realize gibbit's skin color is slowly starting to match your own skin tone. ")
animal3.feed=("You pour food into Gibbits mouth. And he gobbles it up.")
animal3.groom=("Petting Gibbit is like petting a dolphin. His skin remains soft and smooth. As you pet him his skin starts to slowly match your skin tone.")
animal3.buy=("At home you deposit Gibit into a tub with water. As a bit of a useless fish he just slowlyt floats around. You bring him food and he muches slowly as you brush your teeth. As the days pass by you notice Gibbit is starting move faster and becoming better at swimming. After a few days Gibbit is able to move around the like a snail. After a week Gibbit is kind of walking aroound the house. Somehow he developed two smnall stubby legs and bumpys that may represnet arms? A month later: You wake up to extreme pressure around your neck. As your eyes flutter open your face stares back at you. You realize the arms starggling you are attached to that face. Not long after you black out. \n Cause of death: Your pet has copied your every aspect and decided to replace you in the world. Your pet now lives happily as you")
animal3.notbuy=""
animal3.look="You see a small room "
animal3.touch=""
animal3.collect=""

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

def prompt_user2():
    future_room_inspect= input("Would you like to interact with this pets's room?Select a number.  Yes(1) or No(2)>>")
    print(future_room_inspect)
    if future_room_inspect=="1":
        future_room()
    elif future_room_inspect=="1":
        prompt_user()
    return future_room_inspect

def secret_ending():
    print("You have discovered a secret ending. If you find 3 gold coins in total you will escape the pet shop unscathed. While looking around beware of the assisstant trailing behind you.")







while player1.alive==True:
    #global current_animal
    #animal1.action_check(prompt_user())
    current_animal.action_check(prompt_user())
    prompt_user2()
        
   







