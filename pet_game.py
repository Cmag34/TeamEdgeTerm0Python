import cv2
from PIL import Image
# get rid of import

reply=" "
input_msg =""
rooms = []
location= ""
current_animal=""
bag=[]
found_2nd_golden_coin= False
class Room:
  def __init__(self, name=None, description=None, look=None, items=[]):
    self.name = name
    self.description = description
    self.look= look
    self.touch = []
    self.items = items
    
    #colect is not in here because its a method that does something. Touch and look just print stuff
    

class Animal:
    def __init__(self,name, type,notbuy,buy,groom, feed, shower,room):
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
        self.room = room
        self.bought = False
    
    def action_check(self, action):
        
        if  action =="1":
            print(self.shower)

        elif action =="2":
            
            print(self.groom)
          
        elif action == "3":
            
            print(self.feed)
        elif action == "4":
            self.bought = True
            print(self.buy)
            
        elif action == "5": 
            self.bought = False;
            print(self.notbuy)
           

class Player:
    def __init__(self,name,way_it_kills_you,):
        self.name = name
        self.alive = True
        self.way_you_die = way_it_kills_you


animal1 = Animal("Chichi","White Pomeranian","", "", "", "", "", "")
animal2 = Animal("Bib","Rat","", "", "", "", "", "")
animal3 = Animal("Gibit","Blob Fish ","", "", "", "", "", "")
player1 = Player("","")


def start():
    print("You are shopping for a pet. As you enter, you are greeted by an asistant that will guide you through the process of buying a pet. You have to interact with animals to decide to buy one. You vaguely notice that the entrance severely shuts behind you. The assitant tells you that in order for you to leave the store you are required to buy a pet. Beware if you buy the wrong pet you will face an unfortunate ending. It's now time to buy a pet!  ")
    name = input("What is your name, player? ")
    player1.name = name
    print("Welcome, " + name)

    # quick image load test
    #img = cv2.imread("alive.png")
    #img = Image.fromarray(img, "RGB")
    #img.show()
    
    prompt_user_select_pet()


def prompt_user_select_pet():
    global current_animal
    pet_number= input("\n Which pet would you like to interact with? Select a number. Chichi(1)\nBib(2)\nGibit(3)) ")
  #pet_room = pet_room  
    if pet_number== "1":
        print(animal1room.description)
        current_animal=animal1
    elif pet_number== "2":
        print(animal2room.description)
        current_animal=animal2
    elif pet_number== "3":
        print(animal3room.description)
        current_animal=animal3
    else:
        print("Please type an option above")
        prompt_user_select_pet()
    

def prompt_user_select_room_action():
    #global current_animal
    #global bag
    #global player1
    room_inside= input("How would you like to interact with this pet's room? Or would you like to leave this pet's room. Select a number.\n Look(1)\n Touch(2)\n Collect(3) \n Leave(4)>>> ) ")
 
  #pet_room = pet_room  
    if room_inside== "1":
        print(current_animal.room.look)
        prompt_user_select_room_action()

    elif room_inside== "2":
        prompt_user_select_touch_item()
        

    elif room_inside== "3":
        prompt_user_select_collect_item()
        if player1.alive:
            prompt_user_select_room_action()

    elif room_inside== "4":
        print("Leaving room!")
    
    else:
        print("Please type an option above")
        prompt_user_select_room_action()

def prompt_user_select_touch_item():
    print("Which item would you like to touch?")
    #loop trhough the list to output
    
    for i in range(0, len(current_animal.room.items)):
        print(current_animal.room.items[i] )

    touch_user_input=input("Select a number >>> ) ")
    #if room_inside== "1:
    if touch_user_input== "1":     
        print(current_animal.room.touch[0])
    elif touch_user_input== "2":     
        print(current_animal.room.touch[1])
    elif touch_user_input== "3":     
        print(current_animal.room.touch[2])
        #add golden coin to list
        if current_animal ==  animal1:
            current_animal.room.items.append("Golden Coin A (4)")
            #print("You found the golden coin!")
        if current_animal == animal3:
            current_animal.room.items.append("Golden Coin B (4)")
            #print("You found the golden coin!")
        
    else:
        print("Please type an option above")
        prompt_user_select_touch_item()

    prompt_user_select_room_action()
    

def prompt_user_select_collect_item():
    global bag
    global found_2nd_golden_coin
    
    print("Which item would you like to collect?")

    for i in range(0, len(current_animal.room.items)):
        print(current_animal.room.items[i])

    collect_user_input=input("Select a number >>> ) ")
    array_index = int(collect_user_input) - 1
    if collect_user_input in ["1", "2","3", "4"]:     
        print("collected: " + current_animal.room.items[ array_index ])
        bag.append(current_animal.room.items[ array_index ]) 

        if "Golden Coin A (4)" in bag and "Golden Coin B (4)"in bag :
            found_2nd_golden_coin = True
            
        #found golden coin print secret ending
        if collect_user_input=="4":
            secret_ending()

    #prompt_user_select_room_or_pet()

        
  
    
            
def prompt_user_select_pet_action():
    pet_action= input("\n How would you like to interact with this pet? Select a number. \nShower(1) \n Groom(2)\n Feed(3) \n Buy Pet(4) \n Don't Buy Pet(5))>>  ")
    print(pet_action)
    if pet_action in ["1", "2", "3", "4"]:
        #print(animal2room.description)
        print("")
        current_animal.action_check(pet_action)
        #prompt_user_select_pet_action()
        

    elif pet_action== "5":
        #print(animal3room.description)
        print("Don't Buy - select new pet")
        prompt_user_select_pet()
    else:
        print("Please type an option above")
        prompt_user_select_pet_action()
        return pet_action

def prompt_user1():
    future_pet= input("Would you like to move on to another pet(1) or continue interacting with this pet(2)? Select a number. >> ")
    print(future_pet)
    if future_pet=="1":
        prompt_user_select_pet()
    elif future_pet=="1":
        prompt_user_select_pet_action()
    return future_pet

def prompt_user_select_room_or_pet():
    select_room_action_inspect= input("\n Would you like to interact with the pet or the pet's room? Select a number.Pet(1) or Pet Room(2)>>")
    print(select_room_action_inspect)
    if select_room_action_inspect=="2":
        prompt_user_select_room_action()
    elif select_room_action_inspect=="1":
        prompt_user_select_pet_action()
    return select_room_action_inspect

def secret_ending():
    if found_2nd_golden_coin == False :
        print("\nYou have discovered a secret ending! You are free to leave the pet store unharmed if you find two golden coins.")
    else:
        print("You have found two golden coins! Due to your genius, you are allowed to leave the pet store with your future life intact. Safe travels!")
        print("The Game has ended") 
        player1.alive=False

        #picture display code from from https://iq.opengenus.org/display-image-in-terminal/
        #img = cv2.imread("dog.png")
        img = cv2.imread("alive.png")
        img = Image.fromarray(img, "RGB")
        img.show()

animal1room = Room()
animal1room.name = "Chichi's Room: The Pomeranian"
animal1room.description = "Welcome to the Chichi's(Pomeranian) room!"
animal1room.look="You look around Chichi's room. It is a small compact space littered with white hair. There is a rug and on top of it sits Chichi's bed. By the door are two small metal bowls for food and water."
#animal1room.touch="Would you like to inspect any of the items in the room. Select a number to interact with that item.\n Rug(1) \n Metal Bowls \n Chichi's bed "
animal1room.items= [" Rug(1)", "Metal Bowls(2)", "Chichi's bed(3)"]
animal1room.touch.append("You lift up the rug and are greeted by a blank slate of concrete")
animal1room.touch.append("You lift up the the metal food and water bowl. There is nothing underneath.")
animal1room.touch.append("You lift up Chichi's bed. Underneath, you find a gold coin.  ")

animal1.shower= "You've chosen to wash and groom Chichi!" "Chichi is estatic running in circles around you. Finally, you manage to catch her and sumbmerge her in water. Chichi has now been washed."
animal1.feed="You've chosen to feed Chichi! Chichi adorably eats from your hands. You notice that she keeps nipping at your hands. Chichi burps in your face"
animal1.groom="You begin grooming Chichi after washing her. Suddenly, she starts to pee on your boots. Is she marking her territory? As you are drying and grooming Chichi you notice that she is losing a lot of hair. Masses fall out as you brush the comb yet Chichi's hair remains as full and vibrant as it originaly was."
animal1.buy="You've chosen to buy Chichi! When you bring Chichi home she runs in circles around your home leaving a path of dirty paw marks and fluffy white fur. Right before bed you fill her food bowl. She vigorously eats like theres no tommorow. As you are tucking yourself in, Chichi runs up to your bed and cuddles up next to you. \n The next morning... As you wake up you find it hard to breath. Your body remains incapacitated under a thick mass of white fure. All you see when you open your eyes in a panic is white. It feels imposisble to breath. You slowly die of suffocation as Chichi pounces over your frozen body. Cause of death: Chichi's excessive fur"
animal1.notbuy=" "


#get rid of animal gold coin 
#animal1.golden_coin="you found the golden coin!!!"
animal1.room = animal1room
#would you like to collect it?Select a number.\n Yes(1) \n No(2)
#current_animal.room.items.append 



animal2room = Room()
animal2room.name = "Bib's Room: The Rat"
animal2room.description = ("Welcome to the Bib's(Rat) room!")
animal2room.look="Bib lives in a big pet cage. There is a food bowl and a water bowl, a mini bed, and a plastic slide."
#animal2room.touch="Would you like to inspect any of the items in the room. Select a number to interact with that item.\n Plastic Slide(1) \n Metal Bowls(2) \n Bib's bed(3) "
animal2room.touch.append("You lift up the the metal food and water bowl. There is nothing underneath.")
animal2room.touch.append("You lift up the bed. There is nothing underneath.")
animal2room.touch.append("You touch the slide. It's slippery?")
animal2room.items= [" Plastic Slide(1)", "Metal Bowls(2)", "Bib's bed(3)"]

animal2.shower= ("You've chosen to wash and groom Bib!" "As you wash Bib he keeps slipping through your fingers. Who knew washing a rat would be so annoyingly hard?")
animal2.feed=("You've chosen to feed Bib!Bib adorably eats from your hands. As Bib eats you realize he's consuming a huge amount of food in a few seconds")
animal2.groom=("Grooming Bib is quite easy due to his short hair. But he clealry lacks the ability to stay still so you end up running after him in his cage")
animal2.buy=" You live happily ever after with Bib as your best friend.\n Cause of Death: n/a "
animal2.notbuy=""


animal2.room = animal2room


animal3room = Room()
animal3room.name = "Gibbit's Room: The Blob Fish"
animal3room.description = ("Welcome to Gibbit's(Blob Fish) room!")
animal3room.look="You see a small room. There is a mini pool, a metal food and water bowl, and a little ship toy. "
#xanimal3room.items="Would you like to inspect any of the items in the room. Select a number to interact with that item.\n Mini pool(1) \n Metal Bowls(2) \n Ship toy(3) "

animal3room.touch.append("The mini pool is clear. It seems that Gibbit sleeps and lives in this pool.")
animal3room.touch.append("You lift up the the metal food and water bowl. There is nothing underneath.")
animal3room.touch.append("You touch the ship toy. Something shiny and gold cathes your eye. You reach inside amd pull out a gold coin. You have found a gold coin!")
animal3room.items= [" Mini pool(1)", "Metal Bowls(2)", "Ship toy(3)"]

animal3.shower= "You've chosen to wash Gibbit!""Due to Gibit's weight they're unable to move about much. Gibbit sits like deadweight as you rub water and soap on it. After a little bit you realize Gibbit's skin color is slowly starting to match your own skin tone. "
animal3.feed="You pour food into Gibbits mouth and he gobbles it up."
animal3.groom="Petting Gibbit is like petting a dolphin. His skin is soft and smooth. As you pet him his skin starts to slowly match your skin tone."
animal3.buy="At home, you deposit Gibit into a tub with water. As a useless fish, he just drifts around slowly. You bring him food and he munches slowly as you brush your teeth. As the days pass, you notice that Gibbit is starting to move faster and become better at swimming. After a few days, Gibbit is able to move around the house like a snail. After a week, Gibbit is able to stiltedly wark around the house. Somehow, he developed two small stubby legs and bump that could be arms? A month later: You wake up to extreme pressure around your neck. As your eyes flutter open your face stares back at you. You realize the arms that are strangling you are attached to that face. Not long after you black out. \n Cause of death: Your pet has copied your every aspect and decided to replace you in the world. Your pet now lives happily as you"
animal3.notbuy=""
#animal3.golden_coin="you found the golden coin!!!"

animal3.room = animal3room


start()

while player1.alive==True:
    #animal1.action_check(prompt_user_select_pet_action())

    if current_animal.bought==False:
        prompt_user_select_room_or_pet()
           
    else:
        player1.alive=False
        print("The Game has ended") 

        








