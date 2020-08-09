import tkinter as tk
from tkinter import *
from Medium import Methods

LARGE_FONT= ("Verdana", 12,'bold')
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        # Window
        self.geometry('400x350')
        self.resizable(0,0)

        # Logo
        global logo
        logo = PhotoImage(file = "/home/jugjug/Desktop/Python Course/GUI/photos/icon.png")
        logo_label = Label(self,image = logo)
        logo_label.pack()

        # Title Bar
        self.title("Website Blocker")
        title_photo = PhotoImage(file = "/home/jugjug/Desktop/Python/GUI/photos/logo.png")
        self.iconphoto(False,title_photo)

        # MenuBar Code
        # self.menubar = Menu(self)
        # self.config(menu = self.menubar)
        # Options = Menu(self.menubar,tearoff = 0)
        # self.menubar.add_cascade(label = "Options", menu = Options)
        # Options.add_command(label = "About app")
        # Options.add_command(label = "About Developer")
        # Options.add_separator()
        # Options.add_command(label = "Exit",command = self.quit)
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (ShowPage, UnblockWebsite, BlockWebsite, AboutDeveloper, AboutApp):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(ShowPage)
    
        global fb,gh,ld
        # About me
        about_me = Label(self, text = "-------------------- Follow me on -------------------- ")
        about_me.configure(font=("Times New Roman", 15, "bold italic"))
        about_me.place(x =0, y=260)

        # Fb address
        fb = PhotoImage(file = "photos/fb.png")
        fb_label = Label(self,image = fb)
        fb_label.bind("<Button-1>",Methods.github_callback)
        fb_label.place(x=50,y=290)

        # Github Profile
        gh = PhotoImage(file = "photos/github.png")
        gh_label = Label(self,image = gh, bg = "black")
        gh_label.bind("<Button-1>",Methods.facebook_callback)
        gh_label.place(x=180,y=290)

        # Linkdin Profile
        ld = PhotoImage(file = "photos/linkedin.png")
        ld_label = Label(self,image = ld)
        ld_label.bind("<Button-1>",Methods.linkedin_callback)
        ld_label.place(x = 300,y=290)

        me = Label(self,text = "-@ami_jugjug")
        me.place(x= 300,y=330)
   
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
      
class ShowPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        def updateListbox():
            CONTENT = Methods.show_sites()
            if(len(CONTENT) == 0):
                self.list.insert(0,"Not any site has been blocked yet.")
            else:
                self.list.insert(0,"***********BLOCKED WEBSITES***********")
                self.list.insert(1, *CONTENT)


        self.list = tk.Listbox(self,width = 200,bg = 'silver', height = 5,font = LARGE_FONT,justify = CENTER)
        updateListbox()
        self.list.pack()

        ubw = tk.Button(self, text="Unblock Website",command=lambda: controller.show_frame(UnblockWebsite))
        ubw.place(x = 225,y = 120)

        bw = tk.Button(self, text="Block Website",command=lambda: controller.show_frame(BlockWebsite))
        bw.place(x = 30,y = 120)

class BlockWebsite(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Block unwanted websites", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        def clear_text(self):
            link_entry.delete(0, 'end') 
            link_entry.insert(0,"")

        def submit_text(event):
            m = Methods(link_value)
            m.add_site()

        #Blocker Code
        lab = Label(self,text = "Paste the link you want to block down below")
        lab.configure(font=("Times New Roman", 15, "bold italic"))
        lab.pack()
        
        
        link_value = StringVar()
        link_entry = Entry(self,textvariable = link_value, width = 32 )
        link_entry.insert(0,"www.examplewebsite.com")
        m = Methods(link_value)
        link_entry.bind('<Button-1>',clear_text)
        link_entry.bind('<Return>',submit_text)
        link_entry.place(x = 15,y = 75)
        
        
        submit = Button(self,text = "Block it !!!",underline = 50,command = m.add_site)
        submit.configure(font=("Arial", 10,"bold"))
        submit.place(x=285, y=70)

        button1 = tk.Button(self, text="Back to Home",command=lambda: controller.show_frame(ShowPage))
        button1.place(x = 30,y = 120)

        button2 = tk.Button(self, text="Unblock Website",command=lambda: controller.show_frame(UnblockWebsite))
        button2.place(x = 225,y = 120)

class UnblockWebsite(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def deleteSelected():
            cs = self.list.curselection()[0]
            m = Methods(self.list.get(cs))
            m.remove_sites()
            self.list.delete(ANCHOR)

        def updateListbox():
            CONTENT = Methods.show_sites()
            if(len(CONTENT) == 0):
                self.list.insert(0,"Not any site has been blocked yet.")
            else:
                self.list.insert(0,"***********BLOCKED WEBSITES***********")
                self.list.insert(1, *CONTENT)

        self.list = tk.Listbox(self,width = 200,bg = 'silver', height = 5,font = LARGE_FONT,justify = CENTER)
        updateListbox()
        self.list.bind("<<ListboxSelect>>", lambda x: deleteSelected())
        self.list.pack()

        button1 = tk.Button(self, text="Back to Home",command=lambda: controller.show_frame(ShowPage))
        button1.place(x = 30,y = 120)

        button2 = tk.Button(self, text="Block Website",command=lambda: controller.show_frame(BlockWebsite))
        button2.place(x = 225,y = 120)

class  AboutDeveloper(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="About Developer", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(ShowPage),height = 1,width = 9)
        button1.place(x =10,y=40)

        global fb,gh,ld
        # About me
        about_me = Label(self, text = "-------------------- Follow me on -------------------- ")
        about_me.configure(font=("Times New Roman", 15, "bold italic"))
        about_me.place(x =0, y=150)

        # Fb address
        fb = PhotoImage(file = "photos/fb.png")
        fb_label = Label(self,image = fb)
        fb_label.bind("<Button-1>",Methods.github_callback)
        fb_label.place(x=50,y=180)
        # fb_label.grid(row = 0,column = 1)

        # Github Profile
        gh = PhotoImage(file = "photos/github.png")
        gh_label = Label(self,image = gh, bg = "black")
        gh_label.bind("<Button-1>",Methods.facebook_callback)
        gh_label.place(x=180,y=180)
        # gh_label.grid(row = 3,column = 2)

        # Linkdin Profile
        ld = PhotoImage(file = "photos/linkedin.png")
        ld_label = Label(self,image = ld)
        ld_label.bind("<Button-1>",Methods.linkedin_callback)
        ld_label.place(x = 300,y=180)

        me = Label(self,text = "-@ami_jugjug")
        me.place(x= 300,y=221)

class AboutApp(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="About App", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(ShowPage))
        button1.pack(side = LEFT)

master = App()
master.mainloop()