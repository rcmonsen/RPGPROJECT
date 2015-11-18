#Robert Monsen
#RPG game
#CIT144

from tkinter import *

class mainFrame():  #create tkinter GUI class for RPG
    def __init__(self):
        self.window = Tk()
        self.window.title("RPG")
        self.window.geometry("500x340")

        
        
        #add bg image
        background_img = PhotoImage(file='img.gif')
        back = Label(self.window, image=background_img)
        back.place(x=0, y=0, relwidth=1, relheight=1)

        
        
      
        #Displays
        self.text = StringVar()
        self.mainText = Label(self.window, textvariable = self.text,bg="white", wraplength=500,
                              justify=CENTER, width=80, height=14, relief=SUNKEN, borderwidth=3)
        self.mainText.pack()
        self.user_text = StringVar()
        self.userText = Label(self.window, text=">>> ",textvariable = self.user_text,
                              bg="white", width=80, relief=SUNKEN, borderwidth=3)
        self.userText.pack()

        #entrybox
        self.entry = StringVar()
        self.entryBox = Entry(self.window, textvariable = self.entry, width=40)
        self.entryBox.pack()
        self.entryBox.bind("<Return>", self.OnPressEnter)
        #Button
        button = Button(self.window, text = "Enter", command = self.enter)
        button.pack()

           
        self.window.mainloop()

    def processEnter(self, event):
        self.user_text.set(">>> "+self.entryBox.get())
        if (self.entryBox.get()).lower() == 'help':
            self.text.set("This is the help. I hope it helps.")
        self.entry.set('')
            
    def OnPressEnter(self,event):
        self.processEnter(event)
    def enter(self):
        self.processEnter(None)
    
    
    
mainFrame()
    
    
