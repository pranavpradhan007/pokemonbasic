import random
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk,ImageSequence
import time
import pandas as pd

def display():
    for i in rows:
            print(i)

def caught(pokeball):
    if pokeball==1 or pokeball==2 or pokeball==3:
        global wildpokemon
        global rows
        
        if choice==1:
            if level<16:
                if "Bulbasaur" not in rows:
                    rows.append("Bulbasaur")
            elif level>=16:
                if "Ivysaur" not in rows:
                    rows.append("Ivysaur")
                    rows.remove("Bulbasaur")
            elif level>=36:
                if "Venusaur" not in rows:
                    rows.append("Venusaur")
                    rows.remove("Ivysaur")
        elif choice==2:
            if level<16:
                if "Charmander" not in rows:
                    rows.append("Charmander")
            elif level>=16:
                if "Charmeleon" not in rows:
                    rows.append("Charmeleon")
                    rows.remove("Charmander")
            elif level>=36:
                if "Charizard" not in rows:
                    rows.append("Charizard")
                    rows.remove("Charmeleon")
        elif choice==3:
            if level<16:
                if "Squirtle" not in rows:
                    rows.append("Squirtle")
            elif level>=16:
                if "Wartortle" not in rows:
                    rows.append("Wartortle")
                    rows.remove("Squirtle")
            elif level>=36:
                if "Blastoise" not in rows:
                    rows.append("Blastoise")
                    rows.remove("Wartortle")
        rows.append(wildpokemon)

def evolution(choice):
    rt=tk.Tk()
    rt.geometry("500x500")
    rt.resizable(False,False)
    rt.title('Evolution')

    if choice==1:
        if level==16:
            print("Bulbasaur is evolving!\n")
            def play_gif():
                global img
                img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\ivysaur.gif")
                lbl=Label(rt)
                lbl.place(x=0,y=0)
                for img in ImageSequence.Iterator(img):
                    img=ImageTk.PhotoImage(img)
                    lbl.config(image=img)
                    rt.update()
                    time.sleep(0.05)   
            play_gif()
            time.sleep(3)
            print("Your Bulbasaur evolved into Ivysaur!")
        elif level==36:
            print("Ivysaur is evolving!\n")
            def play_gif():
                global img
                img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\venusaur.gif")
                lbl=Label(rt)
                lbl.place(x=0,y=0)
                for img in ImageSequence.Iterator(img):
                    img=ImageTk.PhotoImage(img)
                    lbl.config(image=img)
                    rt.update()
                    time.sleep(0.05)   
            play_gif()
            time.sleep(3)
            print("Your Ivysaur evolved into Venusaur!")
    elif choice==2:
        if level==16:
            print("Charmander is evolving!\n")
            def play_gif():
                global img
                img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\charmeleon.gif")
                lbl=Label(rt)
                lbl.place(x=0,y=0)
                for img in ImageSequence.Iterator(img):
                    img=ImageTk.PhotoImage(img)
                    lbl.config(image=img)
                    rt.update()
                    time.sleep(0.05)   
            play_gif()
            time.sleep(3)
            print("Your Charmander evolved into Charmeleon!")
        elif level==36:
            print("Charmeleon is evolving!\n")
            def play_gif():
                global img
                img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\charizard.gif")
                lbl=Label(rt)
                lbl.place(x=0,y=0)
                for img in ImageSequence.Iterator(img):
                    img=ImageTk.PhotoImage(img)
                    lbl.config(image=img)
                    rt.update()
                    time.sleep(0.05)   
            play_gif()
            time.sleep(3)
            print("Your Charmeleon evolved into Charizard!")
    elif choice==3:
        if level==16:
            print("Squirtle is evolving!\n")
            def play_gif():
                global img
                img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\wartortle.gif")
                lbl=Label(rt)
                lbl.place(x=0,y=0)
                for img in ImageSequence.Iterator(img):
                    img=ImageTk.PhotoImage(img)
                    lbl.config(image=img)
                    rt.update()
                    time.sleep(0.05)   
            play_gif()
            time.sleep(3)
            print("Your Squirtle evolved into Wartortle!")
        elif level==36:
            print("Wartortle is evolving!\n")
            def play_gif():
                global img
                img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\blastoise.gif")
                lbl=Label(rt)
                lbl.place(x=0,y=0)
                for img in ImageSequence.Iterator(img):
                    img=ImageTk.PhotoImage(img)
                    lbl.config(image=img)
                    rt.update()
                    time.sleep(0.05)   
            play_gif()
            time.sleep(3)
            print("Your Wartortle evolved into Blastoise!")

    rt.destroy()
    rt.mainloop()
    
def video(choice,attack):
    try:
        root=tk.Tk()
        root.geometry("500x390")
        root.resizable(False,False)
        if choice==1:
            if attack==1:
                root.title('Tackle')
                def play_gif():
                    global img
                    if level<16:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\tackle bulbasaur.gif")
                    elif level>=16:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\ivysaur tackle.gif")
                    elif level>=36:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\venusaur tackle.gif")
                    lbl=Label(root)
                    lbl.place(x=0,y=0)
                    for img in ImageSequence.Iterator(img):
                        img=ImageTk.PhotoImage(img)
                        lbl.config(image=img)
                        root.update()
                        time.sleep(0.05)
                
                play_gif()
                time.sleep(3)
            elif attack==2:
                root.title('Vine whip')
                def play_gif():
                    global img
                    if level<16:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\vine whip.gif")
                    elif level>=16:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\ivysaur vine whip.gif")
                    elif level>=36:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\venusaur vinewhip.gif")
                    lbl=Label(root)
                    lbl.place(x=0,y=0)
                    for img in ImageSequence.Iterator(img):
                        img=ImageTk.PhotoImage(img)
                        lbl.config(image=img)
                        root.update()
                        time.sleep(0.05)
                
                play_gif()
                time.sleep(3)
            elif attack==3:
                root.title('Solar beam')
                def play_gif():
                    global img
                    if level<16:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\solar beam.gif")
                    elif level>=16:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\ivysaur solar beam.gif")
                    elif level>=36:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\venusaur solar beam.gif")
                    lbl=Label(root)
                    lbl.place(x=0,y=0)
                    for img in ImageSequence.Iterator(img):
                        img=ImageTk.PhotoImage(img)
                        lbl.config(image=img)
                        root.update()
                        time.sleep(0.05)
                
                play_gif()
                time.sleep(3)
            elif attack==4:
                root.title('Seed bomb')
                def play_gif():
                    global img
                    if level<16:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\seed bomb.gif")
                    elif level>=16:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\ivysaur seed bomb.gif")
                    elif level>=36:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\venusaur seed bomb.gif")
                    lbl=Label(root)
                    lbl.place(x=0,y=0)
                    for img in ImageSequence.Iterator(img):
                        img=ImageTk.PhotoImage(img)
                        lbl.config(image=img)
                        root.update()
                        time.sleep(0.05)
                
                play_gif()
                time.sleep(3)  
        elif choice==2:
            if attack==1:
                root.title('Scratch')
                def play_gif():
                    global img
                    if level<16:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\scratch.gif")
                    elif level>=16:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\charmeleon scratch.gif")
                    elif level>=36:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\charizard scratch.gif")
                    lbl=Label(root)
                    lbl.place(x=0,y=0)
                    for img in ImageSequence.Iterator(img):
                        img=ImageTk.PhotoImage(img)
                        lbl.config(image=img)
                        root.update()
                        time.sleep(0.05)
                
                play_gif()
                time.sleep(3)
            elif attack==2:
                root.title('Flamethrower')
                def play_gif():
                    global img
                    if level<16:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\flamethrower.gif")
                    elif level>=16:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\charmeleon flamethrower.gif")
                    elif level>=36:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\charizard flamethrower.gif")
                    lbl=Label(root)
                    lbl.place(x=0,y=0)
                    for img in ImageSequence.Iterator(img):
                        img=ImageTk.PhotoImage(img)
                        lbl.config(image=img)
                        root.update()
                        time.sleep(0.05)
                
                play_gif()
                time.sleep(3)
            elif attack==3:
                root.title('Flameburst')
                def play_gif():
                    global img
                    if level<16:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\flameburst.gif")
                    elif level>=16:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\charmeleon flameburst.gif")
                    elif level>=36:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\charizard flameburst.gif")
                    lbl=Label(root)
                    lbl.place(x=0,y=0)
                    for img in ImageSequence.Iterator(img):
                        img=ImageTk.PhotoImage(img)
                        lbl.config(image=img)
                        root.update()
                        time.sleep(0.05)
                
                play_gif()
                time.sleep(3)
            elif attack==4:
                root.title('Flame charge')
                def play_gif():
                    global img
                    if level<16:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\flamecharge.gif")
                    elif level>=16:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\charmeleon flamecharge.gif")
                    elif level>=36:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\charizard flamecharge.gif")
                    lbl=Label(root)
                    lbl.place(x=0,y=0)
                    for img in ImageSequence.Iterator(img):
                        img=ImageTk.PhotoImage(img)
                        lbl.config(image=img)
                        root.update()
                        time.sleep(0.05)
                
                play_gif()
                time.sleep(3)

        elif choice==3:
            if attack==1:
                root.title('Tackle')
                def play_gif():
                    global img
                    if level<16:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\tackle squirtle.gif")
                    elif level>=16:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\wartortle tackle.gif")
                    elif level>=36:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\blastoise tackle.gif")
                    lbl=Label(root)
                    lbl.place(x=0,y=0)
                    for img in ImageSequence.Iterator(img):
                        img=ImageTk.PhotoImage(img)
                        lbl.config(image=img)
                        root.update()
                        time.sleep(0.05)
                
                play_gif()
                time.sleep(3)
            elif attack==2:
                root.title('Aqua tail')
                def play_gif():
                    global img
                    if level<16:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\aqua tail.gif")
                    elif level>=16:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\wartortle aquatail.gif")
                    elif level>=36:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\blastoise aquatail.gif")
                    lbl=Label(root)
                    lbl.place(x=0,y=0)
                    for img in ImageSequence.Iterator(img):
                        img=ImageTk.PhotoImage(img)
                        lbl.config(image=img)
                        root.update()
                        time.sleep(0.05)
                
                play_gif()
                time.sleep(3)
            elif attack==3:
                root.title('Water pulse')
                def play_gif():
                    global img
                    if level<16:
                        img=Image.open("D:\\Pranav\\ython progs\\pokemon gifs\\water pulse.gif")
                    elif level>=16:
                        img=Image.open("D:\\Pranav\\ython progs\\pokemon gifs\\wartortle waterpulse.gif")
                    elif level>=36:
                        img=Image.open("D:\\Pranav\\ython progs\\pokemon gifs\\blastoise waterpulse.gif")
                    lbl=Label(root)
                    lbl.place(x=0,y=0)
                    for img in ImageSequence.Iterator(img):
                        img=ImageTk.PhotoImage(img)
                        lbl.config(image=img)
                        root.update()
                        time.sleep(0.05)
                
                play_gif()
                time.sleep(3)
            elif attack==4:
                root.title('Aqua jet')
                def play_gif():
                    global img
                    if level<16:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\Aqua jet.gif")
                    elif level>=16:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\wartortle aquajet.gif")
                    elif level>=36:
                        img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\blastoise aquajet.gif")
                    lbl=Label(root)
                    lbl.place(x=0,y=0)
                    for img in ImageSequence.Iterator(img):
                        img=ImageTk.PhotoImage(img)
                        lbl.config(image=img)
                        root.update()
                        time.sleep(0.05)
                
                play_gif()
                time.sleep(3)
        root.destroy()
        root.mainloop()
    except:
        pass

def fight():
    global exp
    global level
    p=random.randint(2,7)

    if choice==1:
        if level<16:
            pokename="Bulbasaur"
        elif level>=16:
            pokename="Ivysaur"
        elif level>=36:
            pokename="Venusaur"
        for i in range(1,p):
            print(pokename+"'s attacks:\n1.Tackle\t2.Vine whip\t3.Solar beam\t4.Seed bomb\n")
            while(True):
                try:
                    attack=int(input("Choose your selection in integer form.\n"))
                except:
                    print("Not an integer.")
                else:
                    break
            if attack==1:
                print(pokename+" used Tackle!")
                video(1,1)
            elif attack==2:
                print(pokename+" used Vine whip!")
                video(1,2)
            elif attack==3:
                print(pokename+" used Solar beam!")
                video(1,3)
            elif attack==4:
                print(pokename+" used Seed bomb!")
                video(1,4)
            else:
                print("Game error! Exiting game.")
                exit()
        print(wildpokemon," fainted!\n")
        experience=random.randint(100,999)
        exp+=experience
        print(exp)
        if exp>=1000:
            level+=1
            print(pokename+" leveled up! Level: ",level)
            exp=1
            evolution(1)
        else:
            print(pokename+" gained ",experience," experience.")

    elif choice==2:
        if level<16:
            pokename="Charmander"
        elif level>=16:
            pokename="Charmeleon"
        elif level>=36:
            pokename="Charizard"
        for i in range(1,p):
            print(pokename+"'s attacks:\n1.Scratch\t2.Flamethrower\t3.Flameburst\t4.Flamecharge\n")
            while(True):
                try:
                    attack=int(input("Choose your selection in integer form.\n"))
                except:
                    print("Not an integer.")
                else:
                    break
            if attack==1:
                print(pokename+" used scratch!")
                video(2,1)
            elif attack==2:
                print(pokename+" used Flamethrower!")
                video(2,2)
            elif attack==3:
                print(pokename+" used Flameburst!")
                video(2,3)
            elif attack==4:
                print(pokename+" used Flamecharge!")
                video(2,4)
            else:
                print("Game error! Exiting game.")
                exit()
        print(wildpokemon," fainted!\n")
        experience=random.randint(100,999)
        exp+=experience
        if exp>=1000:
            level+=1
            print(pokename+" leveled up! Level: ",level)
            exp=1
            evolution(2)
        else:
            print(pokename+" gained ",experience," experience.")

    elif choice==3:
        if level<16:
            pokename="Squirtle"
        elif level>=16:
            pokename="Wartortle"
        elif level>=36:
            pokename="Blastoise"
        for i in range(1,p):
            print(pokename+"'s attacks:\n1.Tackle\t2.Aqua tail\t3.Water pulse\t4.Aqua jet\n")
            while(True):
                try:
                    attack=int(input("Choose your selection in integer form.\n"))
                except:
                    print("Not an integer.")
                else:
                    break
            if attack==1:
                print(pokename+" used Tackle!")
                video(3,1)
            elif attack==2:
                print(pokename+" used Aqua tail!")
                video(3,2)
            elif attack==3:
                print(pokename+" used Water pulse!")
                video(3,3)
            elif attack==4:
                print(pokename+" used Aqua jet!")
                video(3,4)
            else:
                print("Game error! Exiting game.")
                exit()
            print(wildpokemon," fainted!\n")
        experience=random.randint(100,999)
        exp+=experience
        if exp>=1000:
            level+=1
            print(pokename+" leveled up! Level: ",level)
            exp=1
            evolution(3)
        else:
            print(pokename+" gained ",experience," experience.")

def catch():
    root=tk.Tk()
    root.geometry("500x500")
    root.resizable(False,False)
    global pokeball
    pokeball=random.randint(1,3)
    if pokeball==1:
        print(name,", you have caught ",wildpokemon," !")
        root.title('Caught')
        def play_gif():
            global img
            img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\caught.gif")
            lbl=Label(root)
            lbl.place(x=0,y=0)
            for img in ImageSequence.Iterator(img):
                img=ImageTk.PhotoImage(img)
                lbl.config(image=img)
                root.update()
                time.sleep(0.05)
        play_gif() 
        caught(1)             
            
    elif pokeball==2:
        for i in range(0,4):
            if i==3:
                print(name,", you have caught ",wildpokemon," !")
                root.title('Caught')
                def play_gif():
                    global img
                    img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\caught.gif")
                    lbl=Label(root)
                    lbl.place(x=0,y=0)
                    for img in ImageSequence.Iterator(img):
                        img=ImageTk.PhotoImage(img)
                        lbl.config(image=img)
                        root.update()
                        time.sleep(0.05)
                play_gif()
                caught(2)              
                
            else:
                print("Hard to catch trying again")
                root.title('Catching')
                def play_gif():
                    global img
                    img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\catching.gif")
                    lbl=Label(root)
                    lbl.place(x=0,y=0)
                    for img in ImageSequence.Iterator(img):
                        img=ImageTk.PhotoImage(img)
                        lbl.config(image=img)
                        root.update()
                        time.sleep(0.05)
                play_gif()              
                               
                time.sleep(3)
    else:
        for i in range(0,10):
            if i==9:
                print(name,", you have caught ",wildpokemon," !")
                root.title('Caught')
                def play_gif():
                    global img
                    img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\caught.gif")
                    lbl=Label(root)
                    lbl.place(x=0,y=0)
                    for img in ImageSequence.Iterator(img):
                        img=ImageTk.PhotoImage(img)
                        lbl.config(image=img)
                        root.update()
                        time.sleep(0.05)
                play_gif()
                caught(3)              
                
            else:
                print("Hard to catch trying again")
                root.title('Catching')
                def play_gif():
                    global img
                    img=Image.open("D:\\Pranav\\python progs\\pokemon gifs\\catching.gif")
                    lbl=Label(root)
                    lbl.place(x=0,y=0)
                    for img in ImageSequence.Iterator(img):
                        img=ImageTk.PhotoImage(img)
                        lbl.config(image=img)
                        root.update()
                        time.sleep(0.05)
                play_gif()              
                
                time.sleep(3)
    root.destroy()           
    root.mainloop()

df=pd.read_csv(r"D:\\Pranav\\python progs\\pokemon\\p.csv")
name=input("What is your name trainer?\n")
print("Hello ",name+". I am Professor Oak. You now can choose one of the three starting pokemon from kanto region.")
print("Choose your pokemon. 1.Bulbasaur\t2.Charmander\t3.Squirtle\n")

try:
    choice=int(input("Enter the number associated with the pokemon which you want to select. \n"))
    
except:
    print("Go away you are wasting my time!")
    exit()
if choice==1:
    print("You chose Bulbasaur!\n")
elif choice==2:
    print("You chose Charmander!\n")
elif choice==3:
    print("You chose Squirtle!\n")
else:
    print("Go away you are wasting my time!")
    exit()

print("\nGood luck for your future endeavours!\nYou will now encounter wild pokemon.\n")

exp=0   
level=1
rows=[]

while True:
    time.sleep(4)
    wildpokemon=df.sample()
    print("You have encountered a wild pokemon.\n",wildpokemon)

    print("\n1.Fight!\t2.Catch!\t3.Run away\t4.Pokemon\t5.Exit game")
    
    while(True):
        try:
            choice1=int(input("Enter number associated with the selection.\n"))
        except:
            print("Selection was not an integer")
        else:
            break
    if choice1==1:
        fight()
    elif choice1==2:
        catch()
    elif choice1==3:
        print("Got away safely!")
    elif choice1==4:
        print("Opening your caught pokemon list...")
        time.sleep(3)
        display()
    elif choice1==5:
        while True:
            try:
                ex=input("Are you sure you want to exit the game?\nExiting the game won't save your progress.\nPress y/Y for quiting the game.\nPress n/N for resuming the game.")
            except:
                print("Not a charectar! Try again!")
            else:
                break
        if ex=='y' or ex=='Y':
            print("Exiting...")
            time.sleep(5)
            exit()
        elif ex=='n' or ex=='N':
            pass
        else:
            print("Game error! Files have been corrupted!")
            exit()
    else:
        print("Pokemon was wayy too powerful. It killed your pokemon and you.\nGame over!")
        exit()