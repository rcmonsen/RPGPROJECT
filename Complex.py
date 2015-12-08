#Robert Monsen
#RPG game
#CIT144

from tkinter import *

class mainFrame():  #create tkinter GUI class for RPG
    def __init__(self):
        self.window = Tk()
        self.window.title("Complex")
        self.window.resizable(width=FALSE, height=FALSE)
        self.room = []
        self.count = 0
#####################Initialize a local list to store in-game events####################
        self.history_message = ["|| HISTORY ||"]

###############Display area for updating text for in-game events###########################
        self.text = StringVar()
        self.mainText = Label(self.window, textvariable = self.text, font=("Comic Sans MS", 12),bg="white", wraplength=500,
                              justify=CENTER, width=80, height=14, relief=SUNKEN, borderwidth=3)
        self.mainText.grid(row=1, column=1)
        self.user_text = StringVar()
        self.userText = Label(self.window, text=">>> ",textvariable = self.user_text,
                              bg="white", width=80, relief=SUNKEN, borderwidth=3)
        self.userText.grid(row=2,column=1)
        label1 = Label(self.window, text="Complex").grid(row=3, column=1)
        label2 = Label(self.window, text="***For Help type 'help' or 'start' to start the game!***").grid(row=4, column=1)

        #entrybox
        self.entry = StringVar()
        self.entryBox = Entry(self.window, textvariable = self.entry, width=45)
        self.entryBox.grid(row=5,column=1)
        self.entryBox.bind("<Return>", self.OnPressEnter)

        #Entry Button drawn to screen
        button = Button(self.window, text = "Enter", command = self.enter, width=15)
        button.grid(row=5, column=1,sticky=E)
        #History Button drawn to screen
        his_button = Button(self.window, text = "History", command = self.history, width=15)
        his_button.grid(row=5,column=1,sticky=W)

##############Main loop for updating widgets/looking for commands##########################   
        self.window.mainloop()
###################Functions prompted by commands######################################
    def OnPressEnter(self,event):
        self.onButtonPress()
         
    def enter(self):
        self.onButtonPress()
        
##################These are all the calls to the game functions##########################
    def onButtonPress(self):
        self.user_text.set(">>> "+self.entryBox.get())
        if self.entryBox.get() == 'help':
            self.text.set("||HELP MENU||\n To win the game search the rooms for clues.\n\n At any time you can attempt to enter the keyword that wins the game.\n\n Look for words inside of quotes such as 'down' or 'search'.\n\n Type 'start' to start the game. \n\n Use the [History] button to see what you've previously done.")
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
        elif self.entryBox.get().lower() == 'start':
            self.start()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
        elif self.entryBox.get().lower() == 'north':
            self.north()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
        elif self.entryBox.get().lower() == 'east':
            self.east()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
        elif self.entryBox.get().lower() == 'blue':
            self.blue_door()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
        elif self.entryBox.get().lower() == 'yellow':
            self.yellow_door()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
        elif self.entryBox.get().lower() == 'portrait':
            self.portrait()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
        elif self.entryBox.get().lower() == 'crack':
            self.crack()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
        elif self.entryBox.get().lower() == 'black mass':
            self.black_mass()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
        elif self.entryBox.get().lower() == 'use matches':
            self.matches()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
        elif self.entryBox.get().lower() == 'note':
            self.note()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
        elif self.entryBox.get().lower() == 'northeast':
            self.northeast()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
        elif self.entryBox.get().lower() == 'safe':
            self.safe()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
        elif self.entryBox.get().lower() == 'day and night' or self.entryBox.get().lower() == 'night and day':
            self.win()
            self.history_message.append("\nENTRY >>>"+str(self.entryBox.get())+"\n")
            self.history_message.append("\nTEXT >>>"+str(self.text.get())+"\n")
        else:
            self.text.set("Invalid Entry")


#################game functions######################################################
    def start(self):
        self.text.set("You awake on the floor of a room.\n You see two doors, one\
 to the 'north' and one to the 'east'.")
    def north(self):
        self.text.set("You enter the room. You immediately notice a striking 'portrait' of yourself hanging above a fireplace directly ahead.\
 To your right there is a 'yellow' door with large 'crack' in it, large enough to slip your hand through...")
    def east(self):
        self.text.set("You enter the room to the east. The first thing you notice is a deep red carpet... WITH ANTS!!!\
 They appear to be in a large 'black mass'.... as if they are covering something.\n You also notice that there is a 'blue' door to the north...")
    def blue_door(self):
        self.text.set("You move around the 'black mass' towards the blue door and grab the handle.\
 It doesn't turn. There might be another way around...")
    def yellow_door(self):
        self.text.set("You move to the yellow door and attempt to open it. It is locked. Maybe check the 'crack' or the 'portrait'")
    def portrait(self):
        self.text.set("You struggle to move the large portrait of yourself and find behind it a small pack\
 of matches taped to the bottom corner. You put them in your pocket. Maybe you can 'use matches' somewhere...") 
    def crack(self):
        self.text.set("You wiggle your hand inside of the crack just far enough to unlock the door from the other side.\
 Do you enter the 'northeast' room?")
    def black_mass(self):
        self.text.set("You stand in front of the black mass of wriggling ants. They are not afraid.")
    def matches(self):
        self.text.set("You set the matches on fire and throw them towards the pile of ants. They scatter, revealing a\
 honey-covered 'note' on the floor.")
    def note(self):
        self.text.set("The note reads:\n There are two sisters: one gives birth to the other and she, in turn, gives birth to the first.\
 Who are the two sisters?")
    def northeast(self):
        self.text.set("You enter the room. You see the blue door to your right, and to your left you see the sun and the moon painted\
 on the north wall. in front of you there sits a large 'safe', with no lock or handle.")
    def safe(self):
        self.text.set("You stand in front of the safe. In small white letters, where one would expect to see a lock, you see\
 the words ''Speak the answer of Oedipus and recieve your reward.''")
    def win(self):
        self.text.set("You speak the words of Oedipus and the safe *clicks* open to reveal a tiny golden sphinx with a note inscribed\
 on its side saying ''Winner, winner, chicken dinner!''\n\n\n Thanks for Playing!")

########################history button funtion#########################################

    def history(self):
        self.top = Toplevel()
        self.top.title("History")
        self.msg = Message(self.top, text=self.history_message, width=1000)
        self.msg.pack()
            
############Main Loop of the class##################################################        
    
mainFrame()  
    
