#Robert Monsen
#RPG game
#CIT144

#Things to work on:
#Make each room appear on map one at a time until all rooms discovered
#Add more structures to maps, such as doorways, portrait, ants, safe, sun and moon.
#Tweak aesthetics of window/map design... could look better


from tkinter import *


class mainFrame():                                                                                                              #create tkinter GUI class for RPG
    def __init__(self):
        self.window = Tk()
        self.window.title("Complex")                                                                                            #Title of window
        self.window.resizable(width=FALSE, height=FALSE)                                                                        #Keep window size the same
        self.room = ['none']                                                                                                    #initialize lists for keeping track of rooms/items
        self.inv = ['none']
       
#####################Initialize a local list to store in-game events and keywords####################
        self.history_message = ["|| HISTORY ||"]
        
        self.key_help = ['help', 'menu']
        self.key_southwest = ['start', 'room one', 'room 1', 'first room', '1st room', 'southwest']
        self.key_northwest = ['northwest','north']
        self.key_southeast = ['southeast','east']
        self.key_northeast = ['northeast']
        self.key_matches = ['use matches', 'matches', 'strike matches', 'burn matches']
        
###############Display area for text for in-game events###########################
        self.text = StringVar()                                                                                                 #set text to a string variable type
        self.mainText = Label(self.window, textvariable = self.text, font=("Comic Sans MS", 12),bg="white", wraplength=500,     #create a label which displays game text
                              justify=CENTER, width=80, height=14, relief=SUNKEN, borderwidth=3)
        self.mainText.grid(row=1, column=1)                                                                                     #use grid manager to place main text label 
        self.user_text = StringVar()
        self.userText = Label(self.window, text=">>> ",textvariable = self.user_text,
                              bg="white", width=80, relief=SUNKEN, borderwidth=3)
        self.userText.grid(row=2,column=1,sticky=N)
        label1 = Label(self.window, text="Complex").grid(row=3, column=1)
        label2 = Label(self.window, text="***For Help type 'help' or 'start' to start the game!***").grid(row=4, column=1)

        #canvas
        self.can = Canvas(self.window, width=200,height=200,relief=SUNKEN, borderwidth=3)                                       #Create a canvas to draw the map
        self.can.grid(row=1,column=2)

        self.inventory = Canvas(self.window, width=200, height=80, relief=SUNKEN, borderwidth=3, bg="white")                     #Create Inventory window                             
        self.inventory.grid(row=2,column=2)

        label3 = Label(self.window, text="MAP",font=("Times New Roman", 16))
        label3.grid(row=1,column=2,sticky=N)
        label4 = Label(self.window, text="Inventory", font=("Times New Roman",16))
        label4.grid(row=1,column=2,sticky=S)

        

        #entrybox
        self.entry = StringVar()                                                                                                #Set entry box variables as strings
        self.entryBox = Entry(self.window, textvariable = self.entry, width=45)                                                 #Set size and write box to window
        self.entryBox.grid(row=2,column=1,sticky=S)                                                                             #Use grid manager to add to window under text display
        self.entryBox.bind("<Return>", self.OnPressEnter)                                                                       #Bind the 'Return' button to the entry box

        #Entry Button drawn to screen
        button = Button(self.window, text = "Enter", command = self.enter, width=15)                                            #draw buttons to screen for history and Entries
        button.grid(row=3, column=1,sticky=E)
        #History Button drawn to screen
        his_button = Button(self.window, text = "History", command = self.history, width=15)
        his_button.grid(row=3,column=1,sticky=W)

        self.welcome()

##############Main loop for updating widgets/looking for commands##########################   
        self.window.mainloop()

###################Functions prompted by commands######################################
    def OnPressEnter(self,event):                                                                                               #Both 'Return' button and Enter button perform same action (calls the
        self.onButtonPress()                                                                                                    #defined onButtonPress() method.
             
    def enter(self):
        self.onButtonPress()
        
##################These are all the calls to the game functions##########################
    def onButtonPress(self):                                                                                                                #tkinter waits for an action which, in this case, is specifically an 'enter' or 'Return' key press
        self.user_text.set(">>> "+self.entryBox.get())                                                                                      #upon event, the 'if' loop is called and performs actions based on the stored variables and keywords.
        if self.entryBox.get().strip(' ').lower() in self.key_help:                                                                         
            self.text.set("||HELP MENU||\n To win the game search the rooms for clues.\n\n At any time you can attempt\
 to enter the keyword that wins the game.\n\n Look for words inside of quotes such as 'down' or 'search'.\n\n Type 'start' to\
 start the game. \n\n Use the [History] button to see what you've previously done. Type 'back' at any time to go to the previous room.")
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
            self.room.append('help')
        elif self.entryBox.get().strip(' ').lower() == 'back':
            if 'northeast' in self.room:
                self.room.remove(self.room[0])
                self.room.append('northwest')
                self.north()
                self.map_update()
            elif 'northwest' in self.room:
                self.room.remove(self.room[0])
                self.room.append('southwest')
                self.start()
                self.map_update()
            else:
                self.room.remove(self.room[0])
                self.room.append('southwest')
                self.start()
                self.map_update()
                
        elif self.entryBox.get().strip(' ').lower() in self.key_southwest:
            self.start()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
            self.room.remove(self.room[0])
            self.room.append('southwest')
            self.map_update()
        elif self.entryBox.get().strip(' ').lower() in self.key_northwest:
            self.north()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
            self.room.remove(self.room[0])
            self.room.append('northwest')
            self.map_update()
        elif self.entryBox.get().strip(' ').lower() in self.key_southeast:
            self.east()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
            self.room.remove(self.room[0])
            self.room.append('southeast')
            self.map_update()
        elif self.entryBox.get().strip(' ').lower() == 'blue':
            self.blue_door()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
        elif self.entryBox.get().strip(' ').lower() == 'yellow':
            self.yellow_door()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
        elif self.entryBox.get().strip(' ').lower() == 'portrait':
            self.portrait()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
            if 'note' in self.inv:
                pass
            else:
                self.inv.append('matches')
                self.inv_matches()
        elif self.entryBox.get().strip(' ').lower() == 'crack':
            self.crack()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
        elif self.entryBox.get().strip(' ').lower() == 'black mass':
            self.black_mass()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
        elif self.entryBox.get().strip(' ').lower() == 'note':
            self.note()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
            self.inv.append('note')
            self.inv_note()
        elif self.entryBox.get().strip(' ').lower() in self.key_northeast:
            self.northeast()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
            self.room.remove(self.room[0])
            self.room.append('northeast')
            self.map_update()
        elif self.entryBox.get().strip(' ').lower() == 'safe':
            self.safe()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
        elif self.entryBox.get().strip(' ').lower() == 'day and night' or self.entryBox.get().lower() == 'night and day':
            self.win()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
            self.inv_sphynx()
        elif self.entryBox.get().strip(' ').lower() in self.key_matches:
            if 'southeast' in self.room and 'matches' in self.inv:
                self.matches()
                self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
                self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
                self.inv.remove(self.inv[1])
                self.inv_matches()
            else:
                self.text.set("You can't do that right now. Maybe go to the 'southeast' room first...")

        else:
            self.text.set("Invalid Entry")


#################game function text######################################################
    def start(self):                                                                                                #Functions to update the main text screen with in-game text.
        if 'none' in self.room:
            self.text.set("You awake on the floor of a room.\n You see two doors, one\
 to the 'north' and one to the 'east'.")
        else:
            self.text.set("You are in the southwest room where you woke up. There is a door to the 'north' and a door to the 'east'.")
    def north(self):
        self.text.set("You enter the room. You immediately notice a striking 'portrait' of yourself hanging above a fireplace directly ahead.\
 To your right there is a 'yellow' door.")
    def east(self):
        self.text.set("You enter the room to the east. The first thing you notice is a deep red carpet... WITH ANTS!!!\
 They appear to be in a large 'black mass'.... as if they are covering something.\n You also notice that there is a 'blue' door to the north...")
    def blue_door(self):
        self.text.set("You move around the 'black mass' towards the blue door and grab the handle.\
 It doesn't turn. There might be another way around... \n\n(type 'back' to go to previous room)")
    def yellow_door(self):
        self.text.set("You move to the yellow door and attempt to open it. It is locked. You notice a large crack below the handle. Maybe check the 'crack' or the 'portrait'\n\n(type 'back' to go to previous room)")
    def portrait(self):
        if 'matches' in self.inv or 'note' in self.inv:
            self.text.set("You admire the portrait of yourself. It seems the picture was taken very long ago... The difference is like night and day.\n\n(type 'back' to go to previous room)")
        else:
            self.text.set("You struggle to move the large portrait of yourself and find behind it a small pack\
 of matches taped to the bottom corner. You put them in your pocket. Maybe you can 'use matches' somewhere...\n\n(type 'back' to go to previous room)")
    def crack(self):
        self.text.set("You break open the crack, widening just enought to unlock the door from the other side.\
 Do you enter the 'northeast' room?\n\n(type 'back' to go to previous room)")
    def black_mass(self):
        self.text.set("You stand in front of the black mass of wriggling ants. They are not afraid. Maybe you should check the 'blue' door? \n\n(type 'back' to go to previous room)")
    def matches(self):
        self.text.set("You set the matches on fire and throw them towards the pile of ants. They scatter, revealing a\
 honey-covered 'note' on the floor.\n\n(type 'back' to go to previous room)")
    def note(self):
        self.text.set("The note reads:\n There are two sisters: one gives birth to the other and she, in turn, gives birth to the first.\
 Who are the two sisters?\n\n(type 'back' to go to previous room)")
    def northeast(self):
        self.text.set("You enter the room. You see the blue door to your right, and to your left you see the sun and the moon painted\
 on the north wall. in front of you there sits a large 'safe', with no lock or handle.")
    def safe(self):
        self.text.set("You stand in front of the safe. In small white letters, where one would expect to see a lock, you see\
 the words ''Speak the answer of Oedipus and recieve your reward.''\n\n(type 'back' to go to previous room)")
    def win(self):
        self.text.set("You speak the words of Oedipus and the safe *clicks* open to reveal a tiny golden sphinx with a note inscribed\
 on its side saying ''Winner, winner, chicken dinner!''\n\n\n Thanks for Playing!")

##########Intro pop up window######################################################################
    def welcome(self):
        self.welcome_message = ("Welcome to Complex! This is a text based RPG game made by Robert Monsen.\n\n To play simply type into the bottom\
 entry box and hit enter or <Return> on the keyboard. Try using keywords that appear with quotes around them such as 'start' or 'help'.")
        self.pop = Toplevel()
        self.pop.title("Welcome!")
        self.welcome_msg = Message(self.pop, text=self.welcome_message)
        self.welcome_msg.pack()

########################history button funtion#########################################

    def history(self):                                                  #when called will open a 'top level' window displaying the user's history of text input and in-game events
        self.top = Toplevel()
        self.top.title("History")
        self.msg = Message(self.top, text=self.history_message, width=1000)
        self.msg.pack()

################Map Update funtion################################################################
    def map_update(self):
        if 'southwest' in self.room:                                    #Draw the map and update with position of character depending on variable stored in self.room
            self.can.delete("all")
            self.can.create_line(30,30,185,30,width=3)
            self.can.create_line(30,185,185,185,width=3)
            self.can.create_line(30,30,30,185,width=3)
            self.can.create_line(185,30,185,185,width=3)
            self.can.create_line(108,185,108,30,width=3)
            self.can.create_line(30,108,185,108,width=3)
            self.can.create_line(61,109,77,109,width=4,fill="brown")    #north door
            self.can.create_line(108,140,108,154,width=4,fill="brown")  #east door
            self.can.create_line(140,109,154,109,width=4,fill="blue")   #blue door
            self.can.create_line(108,61,108,77,width=4,fill="yellow")   #yellow door
            self.can.create_oval(130,135,140,145,width=3,fill="black")  #create ants
            
            
            #position of oval
            self.can.create_oval(60,155,70,145,width=2)
        elif 'northwest' in self.room:
            self.can.delete("all")
            self.can.create_line(30,30,185,30,width=3)
            self.can.create_line(30,185,185,185,width=3)
            self.can.create_line(30,30,30,185,width=3)
            self.can.create_line(185,30,185,185,width=3)
            self.can.create_line(108,185,108,30,width=3)
            self.can.create_line(30,108,185,108,width=3)
            self.can.create_line(61,109,77,109,width=4,fill="brown")    #north door
            self.can.create_line(108,140,108,154,width=4,fill="brown")  #east door
            self.can.create_line(140,109,154,109,width=4,fill="blue")   #blue door
            self.can.create_line(108,61,108,77,width=4,fill="yellow")   #yellow door
            self.can.create_oval(130,135,140,145,width=3,fill="black")  #create ants
            #position of oval
            self.can.create_oval(60,78,70,88,width=2)
        elif 'southeast' in self.room:
            self.can.delete("all")
            self.can.create_line(30,30,185,30,width=3)
            self.can.create_line(30,185,185,185,width=3)
            self.can.create_line(30,30,30,185,width=3)
            self.can.create_line(185,30,185,185,width=3)
            self.can.create_line(108,185,108,30,width=3)
            self.can.create_line(30,108,185,108,width=3)
            self.can.create_line(61,109,77,109,width=4,fill="brown")    #north door
            self.can.create_line(108,140,108,154,width=4,fill="brown")  #east door
            self.can.create_line(140,109,154,109,width=4,fill="blue")   #blue door
            self.can.create_line(108,61,108,77,width=4,fill="yellow")   #yellow door
            self.can.create_oval(130,135,140,145,width=3,fill="black")  #create ants
            #position of oval
            self.can.create_oval(138,138,148,148,width=2)
        elif 'northeast' in self.room:
            self.can.delete("all")
            self.can.create_line(30,30,185,30,width=3)
            self.can.create_line(30,185,185,185,width=3)
            self.can.create_line(30,30,30,185,width=3)
            self.can.create_line(185,30,185,185,width=3)
            self.can.create_line(108,185,108,30,width=3)
            self.can.create_line(30,108,185,108,width=3)
            self.can.create_line(61,109,77,109,width=4,fill="brown")    #north door
            self.can.create_line(108,140,108,154,width=4,fill="brown")  #east door
            self.can.create_line(140,109,154,109,width=4,fill="blue")   #blue door
            self.can.create_line(108,61,108,77,width=4,fill="yellow")   #yellow door
            self.can.create_oval(130,135,140,145,width=3,fill="black")  #create ants
            #position of oval
            self.can.create_oval(138,60,148,70,width=2)

    def inv_matches(self):
        if 'matches' in self.inv:
            self.inventory.create_line(100,60,140,55,width=2)
            self.inventory.create_line(100,50,140,45,width=2)
            self.inventory.create_line(140,55,140,45,width=2)
            self.inventory.create_line(100,60,100,50,width=2)
            self.inventory.create_line(75,45,75,55,width=2)
            self.inventory.create_line(75,55,100,60,width=2)
            self.inventory.create_line(75,45,100,50,width=2)
            self.inventory.create_line(115,40,140,45,width=2)
            self.inventory.create_line(115,40,75,45,width=2)
            self.inventory.create_text(105,20,text="Matches")
        else:
            self.inventory.delete("all")

    def inv_note(self):
        if 'note' in self.inv:
            self.inventory.create_line(50,40,150,40)
            self.inventory.create_line(50,40,50,75)
            self.inventory.create_line(50,75,150,75)
            self.inventory.create_line(150,75,150,40)
            self.inventory.create_line(50,40,100,60)
            self.inventory.create_line(100,60,150,40)
            self.inventory.create_text(100,20,text="Note")
        else:
            self.inventory.delete("all")
    def inv_sphynx(self):
        self.inventory.delete("all")
        self.inventory.create_text(122,10,text='''.---.''',font=("Times New Roman",8,"bold"))
        self.inventory.create_text(120,20,text='''/   /  (''',font=("Times New Roman",8,"bold"))
        self.inventory.create_text(100,30,text='''.----.__.-\__)_/''',font=("Times New Roman",8,"bold"))
        self.inventory.create_text(90,40,text='''/                      (''',font=("Times New Roman",8,"bold"))
        self.inventory.create_text(100,50,text='''|         _/ _       \\_ _''',font=("Times New Roman",8,"bold"))
        self.inventory.create_text(100,60,text='''\\_____\ --\_____\\''',font=("Times New Roman",8,"bold"))

            

            

        
############Main Loop of the class##################################################        
    
mainFrame()                                                                         #calls the class mainFrame() which then loops over everything above.
    
