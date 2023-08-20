from temppoke import *

class gym:
    global badge
    badge=0

    def __init__(self):
        self.experience=random.randint(500,1001)
        self.badge=badge
        self.level=level
        self.potion=5
        self.poke1=pokename
        self.poke1hp=400
        self.oppo1hp=600
        self.ohp=random.randint(25,101)
        self.p=random.randint(4,9)
        self.rhp=random.randint(50,450)

    def fight(self):
        if choice==1:
            if self.poke1==pokename:
                for i in range(1,self.p):
                    print(self.poke1+"'s attacks:\n1.Tackle\t2.Vine whip\t3.Solar beam\t4.Seed bomb\n")
                    while(True):
                        try:
                            attack=int(input("Choose your selection in integer form.\n"))
                        except:
                            print("Not an integer.")
                        else:
                            break
                    if attack==1:
                        print(self.poke1+" used Tackle!")
                        video(1,1)
                        print(self.oppo+" lost "+self.rhp+" HP!\n"+self.oppo+" has "+self.oppo1hp+" HP.\n")
                        self.oppo1hp-=self.rhp
                        self.poke1hp-=self.ohp
                        print(self.oppo+" attacked!\n"+self.poke1+" lost "+self.ohp+" HP.\n"+self.poke1+" has "+self.poke1hp+" HP.\n")
                        if self.poke1hp<=0:
                            print(self.poke1+" has fainted!")
                            print("You have lost this gym battle!")
                            return
                        if self.oppo1hp<=0:
                            print(self.oppo+" has fainted!")
                            self.oppo1hp==600
                            exp+=self.experience
                            self.badge+=1
                            print("YOU ACHIEVED A BADGE!\nTotal badges="+self.badge)
                            if exp>=1000:
                                self.level+=1
                                print(self.poke1+" leveled up! Level: ",self.level)
                                exp=1
                            else:
                                print(self.poke1+" gained ",self.experience," experience.")
                        else:
                            pass
                    elif attack==2:
                        print(self.poke1+" used Vine whip!")
                        video(1,2)
                        print(self.oppo+" lost "+self.rhp+" HP!\n"+self.oppo+" has "+self.oppo1hp+" HP.\n")
                        self.oppo1hp-=self.rhp
                        self.poke1hp-=self.ohp
                        print(self.oppo+" attacked!\n"+self.poke1+" lost "+self.ohp+" HP.\n"+self.poke1+" has "+self.poke1hp+" HP.\n")
                        if self.poke1hp<=0:
                            print(self.poke1+" has fainted!")
                            print("You have lost this gym battle!")
                            return
                        if self.oppo1hp<=0:
                            print(self.oppo+" has fainted!")
                            self.oppo1hp==600
                            exp+=self.experience
                            self.badge+=1
                            print("YOU ACHIEVED A BADGE!\nTotal badges="+self.badge)
                            if exp>=1000:
                                self.level+=1
                                print(self.poke1+" leveled up! Level: ",self.level)
                                exp=1
                            else:
                                print(self.poke1+" gained ",self.experience," experience.")
                        else:
                            pass
                    elif attack==3:
                        print(self.poke1+" used Solar beam!")
                        video(1,3)
                        print(self.oppo+" lost "+self.rhp+" HP!\n"+self.oppo+" has "+self.oppo1hp+" HP.\n")
                        self.oppo1hp-=self.rhp
                        self.poke1hp-=self.ohp
                        print(self.oppo+" attacked!\n"+self.poke1+" lost "+self.ohp+" HP.\n"+self.poke1+" has "+self.poke1hp+" HP.\n")
                        if self.poke1hp<=0:
                            print(self.poke1+" has fainted!")
                            print("You have lost this gym battle!")
                            return
                        if self.oppo1hp<=0:
                            print(self.oppo+" has fainted!")
                            self.oppo1hp==600
                            exp+=self.experience
                            self.badge+=1
                            print("YOU ACHIEVED A BADGE!\nTotal badges="+self.badge)
                            if exp>=1000:
                                self.level+=1
                                print(self.poke1+" leveled up! Level: ",self.level)
                                exp=1
                            else:
                                print(self.poke1+" gained ",self.experience," experience.")
                        else:
                            pass
                    elif attack==4:
                        print(self.poke1+" used Seed bomb!")
                        video(1,4)
                        print(self.oppo+" lost "+self.rhp+" HP!\n"+self.oppo+" has "+self.oppo1hp+" HP.\n")
                        self.oppo1hp-=self.rhp
                        self.poke1hp-=self.ohp
                        print(self.oppo+" attacked!\n"+self.poke1+" lost "+self.ohp+" HP.\n"+self.poke1+" has "+self.poke1hp+" HP.\n")
                        if self.poke1hp<=0:
                            print(self.poke1+" has fainted!")
                            print("You have lost this gym battle!")
                            return
                        if self.oppo1hp<=0:
                            print(self.oppo+" has fainted!")
                            self.oppo1hp==600
                            exp+=self.experience
                            self.badge+=1
                            print("YOU ACHIEVED A BADGE!\nTotal badges="+self.badge)
                            if exp>=1000:
                                self.level+=1
                                print(self.poke1+" leveled up! Level: ",self.level)
                                exp=1
                            else:
                                print(self.poke1+" gained ",self.experience," experience.")
                        else:
                            pass
                print(self.oppo+" has fainted!")
                self.oppo1hp==600
                exp+=self.experience
                self.badge+=1
                print("YOU ACHIEVED A BADGE!\nTotal badges="+self.badge)
                if exp>=1000:
                    self.level+=1
                    print(self.poke1+" leveled up! Level: ",self.level)
                    exp=1
                else:
                    print(self.poke1+" gained ",self.experience," experience.")

        elif choice==2:
            if self.poke1==pokename:
                for i in range(1,self.p):
                    print(self.poke1+"'s attacks:\n1.Scratch\t2.Flamethrower\t3.Flameburst\t4.Flamecharge\n")
                    while(True):
                        try:
                            attack=int(input("Choose your selection in integer form.\n"))
                        except:
                            print("Not an integer.")
                        else:
                            break
                    if attack==1:
                        print(self.poke1+" used Scratch!")
                        video(2,1)
                        print(self.oppo+" lost "+self.rhp+" HP!\n"+self.oppo+" has "+self.oppo1hp+" HP.\n")
                        self.oppo1hp-=self.rhp
                        self.poke1hp-=self.ohp
                        print(self.oppo+" attacked!\n"+self.poke1+" lost "+self.ohp+" HP.\n"+self.poke1+" has "+self.poke1hp+" HP.\n")
                        if self.poke1hp<=0:
                            print(self.poke1+" has fainted!")
                            print("You have lost this gym battle!")
                            return
                        if self.oppo1hp<=0:
                            print(self.oppo+" has fainted!")
                            self.oppo1hp==600
                            exp+=self.experience
                            self.badge+=1
                            print("YOU ACHIEVED A BADGE!\nTotal badges="+self.badge)
                            if exp>=1000:
                                self.level+=1
                                print(self.poke1+" leveled up! Level: ",self.level)
                                exp=1
                            else:
                                print(self.poke1+" gained ",self.experience," experience.")
                        else:
                            pass
                    elif attack==2:
                        print(self.poke1+" used Flamethrower!")
                        video(2,2)
                        print(self.oppo+" lost "+self.rhp+" HP!\n"+self.oppo+" has "+self.oppo1hp+" HP.\n")
                        self.oppo1hp-=self.rhp
                        self.poke1hp-=self.ohp
                        print(self.oppo+" attacked!\n"+self.poke1+" lost "+self.ohp+" HP.\n"+self.poke1+" has "+self.poke1hp+" HP.\n")
                        if self.poke1hp<=0:
                            print(self.poke1+" has fainted!")
                            print("You have lost this gym battle!")
                            return
                        if self.oppo1hp<=0:
                            print(self.oppo+" has fainted!")
                            self.oppo1hp==600
                            exp+=self.experience
                            self.badge+=1
                            print("YOU ACHIEVED A BADGE!\nTotal badges="+self.badge)
                            if exp>=1000:
                                self.level+=1
                                print(self.poke1+" leveled up! Level: ",self.level)
                                exp=1
                            else:
                                print(self.poke1+" gained ",self.experience," experience.")
                        else:
                            pass
                    elif attack==3:
                        print(self.poke1+" used Flamburst!")
                        video(2,3)
                        print(self.oppo+" lost "+self.rhp+" HP!\n"+self.oppo+" has "+self.oppo1hp+" HP.\n")
                        self.oppo1hp-=self.rhp
                        self.poke1hp-=self.ohp
                        print(self.oppo+" attacked!\n"+self.poke1+" lost "+self.ohp+" HP.\n"+self.poke1+" has "+self.poke1hp+" HP.\n")
                        if self.poke1hp<=0:
                            print(self.poke1+" has fainted!")
                            print("You have lost this gym battle!")
                            return
                        if self.oppo1hp<=0:
                            print(self.oppo+" has fainted!")
                            self.oppo1hp==600
                            exp+=self.experience
                            self.badge+=1
                            print("YOU ACHIEVED A BADGE!\nTotal badges="+self.badge)
                            if exp>=1000:
                                self.level+=1
                                print(self.poke1+" leveled up! Level: ",self.level)
                                exp=1
                            else:
                                print(self.poke1+" gained ",self.experience," experience.")
                        else:
                            pass
                    elif attack==4:
                        print(self.poke1+" used Flamecharge!")
                        video(2,4)
                        print(self.oppo+" lost "+self.rhp+" HP!\n"+self.oppo+" has "+self.oppo1hp+" HP.\n")
                        self.oppo1hp-=self.rhp
                        self.poke1hp-=self.ohp
                        print(self.oppo+" attacked!\n"+self.poke1+" lost "+self.ohp+" HP.\n"+self.poke1+" has "+self.poke1hp+" HP.\n")
                        if self.poke1hp<=0:
                            print(self.poke1+" has fainted!")
                            print("You have lost this gym battle!")
                            return
                        if self.oppo1hp<=0:
                            print(self.oppo+" has fainted!")
                            self.oppo1hp==600
                            exp+=self.experience
                            self.badge+=1
                            print("YOU ACHIEVED A BADGE!\nTotal badges="+self.badge)
                            if exp>=1000:
                                self.level+=1
                                print(self.poke1+" leveled up! Level: ",self.level)
                                exp=1
                            else:
                                print(self.poke1+" gained ",self.experience," experience.")
                        else:
                            pass
                print(self.oppo+" has fainted!")
                self.oppo1hp==600
                exp+=self.experience
                self.badge+=1
                print("YOU ACHIEVED A BADGE!\nTotal badges="+self.badge)
                if exp>=1000:
                    self.level+=1
                    print(self.poke1+" leveled up! Level: ",self.level)
                    exp=1
                else:
                    print(self.poke1+" gained ",self.experience," experience.")        

        elif choice==3:
            if self.poke1==pokename:
                for i in range(1,self.p):
                    print(self.poke1+"'s attacks:\n1.Tackle\t2.Aqua tail\t3.Water pulse\t4.Aqua jet\n")
                    while(True):
                        try:
                            attack=int(input("Choose your selection in integer form.\n"))
                        except:
                            print("Not an integer.")
                        else:
                            break
                    if attack==1:
                        print(self.poke1+" used Tackle!")
                        video(3,1)
                        print(self.oppo+" lost "+self.rhp+" HP!\n"+self.oppo+" has "+self.oppo1hp+" HP.\n")
                        self.oppo1hp-=self.rhp
                        self.poke1hp-=self.ohp
                        print(self.oppo+" attacked!\n"+self.poke1+" lost "+self.ohp+" HP.\n"+self.poke1+" has "+self.poke1hp+" HP.\n")
                        if self.poke1hp<=0:
                            print(self.poke1+" has fainted!")
                            print("You have lost this gym battle!")
                            return
                        if self.oppo1hp<=0:
                            print(self.oppo+" has fainted!")
                            self.oppo1hp==600
                            exp+=self.experience
                            self.badge+=1
                            print("YOU ACHIEVED A BADGE!\nTotal badges="+self.badge)
                            if exp>=1000:
                                self.level+=1
                                print(self.poke1+" leveled up! Level: ",self.level)
                                exp=1
                            else:
                                print(self.poke1+" gained ",self.experience," experience.")
                        else:
                            pass
                    elif attack==2:
                        print(self.poke1+" used Aqua tail!")
                        video(3,2)
                        print(self.oppo+" lost "+self.rhp+" HP!\n"+self.oppo+" has "+self.oppo1hp+" HP.\n")
                        self.oppo1hp-=self.rhp
                        self.poke1hp-=self.ohp
                        print(self.oppo+" attacked!\n"+self.poke1+" lost "+self.ohp+" HP.\n"+self.poke1+" has "+self.poke1hp+" HP.\n")
                        if self.poke1hp<=0:
                            print(self.poke1+" has fainted!")
                            print("You have lost this gym battle!")
                            return
                        if self.oppo1hp<=0:
                            print(self.oppo+" has fainted!")
                            self.oppo1hp==600
                            exp+=self.experience
                            self.badge+=1
                            print("YOU ACHIEVED A BADGE!\nTotal badges="+self.badge)
                            if exp>=1000:
                                self.level+=1
                                print(self.poke1+" leveled up! Level: ",self.level)
                                exp=1
                            else:
                                print(self.poke1+" gained ",self.experience," experience.")
                        else:
                            pass
                    elif attack==3:
                        print(self.poke1+" used Water pulse!")
                        video(3,3)
                        print(self.oppo+" lost "+self.rhp+" HP!\n"+self.oppo+" has "+self.oppo1hp+" HP.\n")
                        self.oppo1hp-=self.rhp
                        self.poke1hp-=self.ohp
                        print(self.oppo+" attacked!\n"+self.poke1+" lost "+self.ohp+" HP.\n"+self.poke1+" has "+self.poke1hp+" HP.\n")
                        if self.poke1hp<=0:
                            print(self.poke1+" has fainted!")
                            print("You have lost this gym battle!")
                            return
                        if self.oppo1hp<=0:
                            print(self.oppo+" has fainted!")
                            self.oppo1hp==600
                            exp+=self.experience
                            self.badge+=1
                            print("YOU ACHIEVED A BADGE!\nTotal badges="+self.badge)
                            if exp>=1000:
                                self.level+=1
                                print(self.poke1+" leveled up! Level: ",self.level)
                                exp=1
                            else:
                                print(self.poke1+" gained ",self.experience," experience.")
                        else:
                            pass
                    elif attack==4:
                        print(self.poke1+" used Aqua jet!")
                        video(3,4)
                        print(self.oppo+" lost "+self.rhp+" HP!\n"+self.oppo+" has "+self.oppo1hp+" HP.\n")
                        self.oppo1hp-=self.rhp
                        self.poke1hp-=self.ohp
                        print(self.oppo+" attacked!\n"+self.poke1+" lost "+self.ohp+" HP.\n"+self.poke1+" has "+self.poke1hp+" HP.\n")
                        if self.poke1hp<=0:
                            print(self.poke1+" has fainted!")
                            print("You have lost this gym battle!")
                            return
                        if self.oppo1hp<=0:
                            print(self.oppo+" has fainted!")
                            self.oppo1hp==600
                            exp+=self.experience
                            self.badge+=1
                            print("YOU ACHIEVED A BADGE!\nTotal badges="+self.badge)
                            if exp>=1000:
                                self.level+=1
                                print(self.poke1+" leveled up! Level: ",self.level)
                                exp=1
                            else:
                                print(self.poke1+" gained ",self.experience," experience.")
                        else:
                            pass                        
                print(self.oppo+" has fainted!")
                self.oppo1hp==600
                exp+=self.experience
                self.badge+=1
                print("YOU ACHIEVED A BADGE!\nTotal badges="+self.badge)
                if exp>=1000:
                    self.level+=1
                    print(self.poke1+" leveled up! Level: ",self.level)
                    exp=1
                else:
                    print(self.poke1+" gained ",self.experience," experience.")                

    def bag(self):
        time.sleep(3)
        print("Your bag contains "+self.potion+" super potions.\nDo you want to use one?\n")
        self.c=input()
        if self.c=="Yes" | self.c=="yes" | self.c=='y' | self.c=='Y':
            print("You used a super potion on "+self.poke1)
            self.potion-=1
            if self.potion<=0:
                print("You do not have any super potions left.")
                self.potion=0
                return
            else:
                self.poke1hp+=200
                print("HP increased by 200.\n")
                print("Current HP is "+self.poke1hp)
                if self.poke1hp>=400:
                    self.poke1hp=400
                elif self.poke1hp<=0:
                    print("Cannot revive a fainted pokemon!")
                    self.poke1hp=0
                    return
                else:
                    pass
        else:
            pass

    def gymbattle(self):
            if choice==1:
                print(name,"chose "+pokename+"!\n")
                print("Your choices:\n1.Fight\t2.Bag\n")
                while(True):
                    try:
                        self.choice2=int(input("Enter your choice in integer form.\n"))
                    except:
                        print("Selection was not an integer.\n")
                    else:
                        break
                    if self.choice2==1:
                        print("You chose to fight!\n")
                        gym.fight()
                    elif self.choice2==2:
                        print("Opening your bag...")
                        gym.bag()

            elif choice==2:
                print(name,"chose "+pokename+"!\n")
                print("Your choices:\n1.Fight\t2.Bag\n")
                while(True):
                    try:
                        self.choice2=int(input("Enter your choice in integer form.\n"))
                    except:
                        print("Selection was not an integer.\n")
                    else:
                        break
                    if self.choice2==1:
                        print("You chose to fight!\n")
                        gym.fight()
                    elif self.choice2==2:
                        print("Opening your bag...")
                        gym.bag()

            elif choice==3:
                print(name,"chose "+pokename+"!\n")
                print("Your choices:\n1.Fight\t2.Bag\n")
                while(True):
                    try:
                        self.choice2=int(input("Enter your choice in integer form.\n"))
                    except:
                        print("Selection was not an integer.\n")
                    else:
                        break
                    if self.choice2==1:
                        print("You chose to fight!\n")
                        gym.fight()
                    elif self.choice2==2:
                        print("Opening your bag...")
                        gym.bag()
    
    def gym(self):
        print("You need total 5 badges to fight the elite 4!\nFight and win gym battles to collect the badges!\n")
        if level==5:
            print("You can now fight gym battles.\n")
            self.ans=input("Do you want to fight a gym battle?\n")
            if self.ans=='yes' | self.ans=='Yes' | self.ans=='Y' | self.ans=='y':
                time.sleep(2.5)
                self.oppo="Staryu"
                print("Your opponent is Misty!\nMisty chose Staryu!\n")
                gym.gymbattle()
                time.sleep(2.5)
            else:
                print("You cannot battle this gym again!\nYou cannot get this badge again!.\n")
                time.sleep(2.5)
                pass
        else:
            pass
        print("You have ",self.badge," number of badges.\n")    
        if level==15:
            print("New gym battle awaits!.\n")
            self.ans=input("Do you want to fight a gym battle?\n")
            if self.ans=='yes' | self.ans=='Yes' | self.ans=='Y' | self.ans=='y':
                time.sleep(2.5)
                self.oppo="Machamp"
                print("Your opponent is Lesner!\nLesner chose Machamp!\n")
                gym.gymbattle()
                time.sleep(2.5)
            else:
                print("You cannot battle this gym again!\nYou cannot get this badge again!.\n")
                time.sleep(2.5)
                pass
        else:
            pass
        print("You have ",self.badge," number of badges.\n")   
        if level==20:
            print("New gym battle awaits!.\n")
            self.ans=input("Do you want to fight a gym battle?\n")
            if self.ans=='yes' | self.ans=='Yes' | self.ans=='Y' | self.ans=='y':
                time.sleep(2.5)
                self.oppo="Raichu"
                print("Your opponent is Dr. Elex!\nDr. Elex chose Raichu!\n")
                gym.gymbattle()
                time.sleep(2.5)
            else:
                print("You cannot battle this gym again!\nYou cannot get this badge again!.\n")
                time.sleep(2.5)
                pass
        else:
            pass
        print("You have ",self.badge," number of badges.\n")   
        if level==25:
            print("New gym battle awaits!.\n")
            self.ans=input("Do you want to fight a gym battle?\n")
            if self.ans=='yes' | self.ans=='Yes' | self.ans=='Y' | self.ans=='y':
                time.sleep(2.5)
                self.oppo="Raichu"
                print("Your opponent is Dr. Elex!\nDr. Elex chose Raichu!\n")
                gym.gymbattle()
                time.sleep(2.5)
            else:
                print("You cannot battle this gym again!\nYou cannot get this badge again!.\n")
                time.sleep(2.5)
                pass
        else:
            pass
        print("You have ",self.badge," number of badges.\n")       
        if level==35:
            print("New gym battle awaits!.\n")
            self.ans=input("Do you want to fight a gym battle?\n")
            if self.ans=='yes' | self.ans=='Yes' | self.ans=='Y' | self.ans=='y':
                time.sleep(2.5)
                self.oppo="Charizard X"
                print("Your opponent is Evil ash!\nEvil ash chose Charizard X!\n")
                gym.gymbattle()
                time.sleep(2.5)
            else:
                print("You cannot battle this gym again!\nYou cannot get this badge again!.\n")
                time.sleep(2.5)
                pass
        else:
            pass
        print("You have ",self.badge," number of badges.\n")   

class elite(gym):

    def __init__(self):
        super().__init__()
        self.potion=5
        self.opponent1hp=1000
        self.opponent2hp=1000
        self.poke2hp=400
        self.poke2="Pikachu"

    def bag(self):
        time.sleep(3)
        print("Your bag contains "+self.potion+" super potions.\nDo you want to use one?\n")
        self.c=input()
        if self.c=="Yes" | self.c=="yes" | self.c=='y' | self.c=='Y':
            if self.poke1:
                print("You used a super potion on "+self.poke1)
                self.potion-=1
                if self.potion<=0:
                    print("You do not have any super potions left.")
                    self.potion=0
                    return
                else:
                    self.poke1hp+=200
                    print("HP increased by 200.\n")
                    print("Current HP is "+self.poke1hp)
                    if self.poke1hp>=400:
                        self.poke1hp=400
                    elif self.poke1hp<=0:
                        print("Cannot revive a fainted pokemon!")
                        self.poke1hp=0
                        return
                    else:
                        pass
            elif self.poke2:            
                print("You used a super potion on "+self.poke2)
                self.potion-=1
                if self.potion<=0:
                    print("You do not have any super potions left.")
                    self.potion=0
                    return
                else:
                    self.poke2hp+=200
                    print("HP increased by 200.\n")
                    print("Current HP is "+self.poke1hp)
                    if self.poke2hp>=400:
                        self.poke2hp=400
                    elif self.poke2hp<=0:
                        print("Cannot revive a fainted pokemon!")
                        self.poke2hp=0
                        return
                    else:
                        pass
        else:
            pass

    def pokemon(self):
        pass

    def fight(self):
        pass

    def battle(self):
        if choice==1:
                print(name,"chose "+pokename+"!\n")
                print("Your choices:\n1.Fight\t2.Bag\t3.Change Pokemon\n")
                while(True):
                    try:
                        self.choice3=int(input("Enter your choice in integer form.\n"))
                    except:
                        print("Selection was not an integer.\n")
                    else:
                        break
                    if self.choice3==1:
                        print("You chose to fight!\n")
                        elite.fight()
                    elif self.choice3==2:
                        print("Opening your bag...")
                        elite.bag()
                    elif self.choice3==3:
                        print("Changing Pokemon...")
                        time.sleep(2.5)
                        elite.pokemon()

        elif choice==2:
                print(name,"chose "+pokename+"!\n")
                print("Your choices:\n1.Fight\t2.Bag\t3.Change Pokemon\n")
                while(True):
                    try:
                        self.choice3=int(input("Enter your choice in integer form.\n"))
                    except:
                        print("Selection was not an integer.\n")
                    else:
                        break
                    if self.choice3==1:
                        print("You chose to fight!\n")
                        elite.fight()
                    elif self.choice3==2:
                        print("Opening your bag...")
                        elite.bag()
                    elif self.choice3==3:
                        print("Changing Pokemon...")
                        time.sleep(2.5)
                        elite.pokemon()

        elif choice==3:
                print(name,"chose "+pokename+"!\n")
                print("Your choices:\n1.Fight\t2.Bag\t3.Change Pokemon\n")
                while(True):
                    try:
                        self.choice3=int(input("Enter your choice in integer form.\n"))
                    except:
                        print("Selection was not an integer.\n")
                    else:
                        break
                    if self.choice3==1:
                        print("You chose to fight!\n")
                        elite.fight()
                    elif self.choice3==2:
                        print("Opening your bag...")
                        elite.bag()
                    elif self.choice3==3:
                        print("Changing Pokemon...")
                        time.sleep(2.5)
                        elite.pokemon()
    
    def elite(self):
        if self.badge==5:
            print("You are now eligible for elite 4 battles!\nYou can chose your starting pokemon and pikachu.\nEach elite member will have 2 pokemon.\nDefeat them to win this game.\n")
            time.sleep(2.5)
            self.opponent="Mr. Giovanni"
            print("Your first opponent is "+self.opponent+"!\n"+self.opponent+" has 2 pokemon.")
            self.opponentpokemon='Persian'
            print(self.opponent+" chose "+self.opponentpokemon)
            elite.battle()
            


        else:
            return


g=gym()
e=elite()

g.gym()
e.elite()