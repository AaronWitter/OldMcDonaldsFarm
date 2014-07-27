# Old McDonald's Farm
# Take care of the Pigs, Chickens and Goats

class Animal(object):
    """Old McDonalds Livestock"""
    def __init__(self, name, hunger = 0, boredom = 0, disease = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.disease = disease

    def __pass_time(self):
        self.hunger += 3
        self.boredom += 3
        self.disease += 2

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom + self.disease
        if unhappiness < 4:
            m = "happy"
        elif 5 <= unhappiness <= 8:
            m = "okay"
        elif 9 <= unhappiness <= 12:
            m = "frustrated"
        elif 13 <= unhappiness <= 16:
            m = "sickly"
        else:
            m = "dead"
        return m
    
    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.")
        self.__pass_time()
    
    def eat(self, food = 2):
        print("Chomp, chomp chomp. Mmmmmm.  Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 2):
        print("Wheee! That was great. Again!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    goat_nme = raw_input("What do you want to name your goat?: ")
    chicken_nme = raw_input("What do you want to name your chicken?: ")
    pig_nme = raw_input("What do you want to name your pig?: ")

#ensuring all names are strings

    goat_name = str(goat_nme)
    chicken_name = str(chicken_nme)
    pig_name = str(pig_nme)

    goat = Animal(goat_name)
    pig = Animal(chicken_name)
    chicken = Animal(pig_name)

    choice = None  
    while choice != "0":
        print \
        """
        Welcome to Old McDonald's Farm...Hard times have fallen on the Olde Farm and Mr McDonald /n
        only has one of each animal left! He needs your help to keep them all alive and happy.
    
        0 - Quit
        1 - Listen to your goat
        2 - Feed your goat
        3 - Play with your goat
        4 - Listen to your pig
        5 - Feed your pig
        6 - Play with your pig
        7 - Listen to your chicken
        8 - Feed your chicken
        9 - Play with your chicken 

        
        """
    
        choice_in = input("Choice: ")
        choice = str(choice_in)
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your goat
        elif choice == "1":
            goat.talk()
        
        # feed your goat
        elif choice == "2":
            goat.eat()
         
        # play with your goat
        elif choice == "3":
            goat.play()
        
        # listen to your pig
        elif choice == "4":
            pig.talk()
        
        # feed your pig
        elif choice == "5":
            pig.eat()
         
        # play with your pig
        elif choice == "6":
            pig.play()

        # listen to your chicken
        elif choice == "7":
            chicken.talk()
        
        # feed your chicken
        elif choice == "8":
            chicken.eat()
         
        # play with your chicken
        elif choice == "9":
            chicken.play()

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.") 
