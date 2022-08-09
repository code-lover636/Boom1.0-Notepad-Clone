from tkinter import*
from tkinter import messagebox, ttk, font
from tkinter.filedialog import askopenfile, asksaveasfile
import clipboard, webbrowser


class MenuBar:
    title = "Boom Text Editor 1.0"
    content = ""
    def __init__(self,root,screen):
        self.root = root
        self.screen = screen        
        
    def erase(self):
        self.screen.delete("1.0",END)
        self.title = "Boom Text Editor 1.0"
        self.root.title(self.title)
            
                
    def open_file(self): 
        self.file = askopenfile(mode='r')
        if self.file is None: return
        self.erase()
        self.title  = self.file.name.split("/")[-1]
        self.root.title(self.title)
        if self.file: 
            self.content = self.file.read()
            self.screen.insert("1.0",self.content)
        
    def save_doc(self,type): 
        if self.title == "Boom Text Editor 1.0": type = "as"
        if type=="rewrite":
            with open(self.file.name,"w") as f: f.write(self.screen.get("1.0",END))
        elif type=="as":  
            file = asksaveasfile(mode='w', defaultextension=".txt")
            if file is None: return
            file.write(str(self.screen.get("1.0",END)))
            file.close()
            self.title  = file.name.split("/")[-1]
            self.root.title(self.title)
        

    def edit(self,opt):
        try:
            self.screen.selection_get()
            if opt == "cut": 
                data=self.screen.selection_get()
                self.screen.delete('sel.first','sel.last') 
                clipboard.copy(data)
            elif opt == "copy":
                data=self.screen.selection_get() 
                clipboard.copy(data)
            elif opt == "paste": 
                self.screen.delete('sel.first','sel.last') 
                self.screen.insert(str(self.screen.index(INSERT)),clipboard.paste())
            elif opt == "delete": self.screen.delete('sel.first','sel.last') 
                
        except: 
            if opt == "paste": self.screen.insert(str(self.screen.index(INSERT)),clipboard.paste())
        
    def search(self): 
        try:
            query = self.screen.selection_get()
            url = "https://google.com/search?q=" + query
            webbrowser.get().open(url)
        except:
            pass
    
    def show_about(self):
        self.erase()   
        about_txt = """
        BOOM TEXT EDITOR 1.0
        ABOUT
        
        This is a simple text editor made with python and tkinter gui. 
        Boom can be used to write and edit text.
        Boom 1.0 is actually a clone of windows notepad.
        """
        self.screen.insert("1.0",about_txt) 
    
    def ok(self): 
        self.screen.config(font=(self.fml.get(),self.size.get(),self.stl.get()))
        self.fontwin.destroy()
        
    def apply(self):
        self.Sample.config(font=(self.fml.get(),self.size.get(),self.stl.get()))
    
    def font(self):
        self.fontwin = Toplevel()
        self.fontwin.title("Font")
        self.fontwin.geometry("400x300")
        self.Sample = Label(self.fontwin, text="AaBbCcDd;!?", font=("Arial",25), width=23,)
        self.Sample.pack()
        combo = Frame(self.fontwin,pady=30,padx=10)
        combo.pack()
        # Font Family
        self.fml = StringVar()
        family = ttk.Combobox(combo, width=20, textvariable=self.fml, values=list(font.families()))
        family.pack(side=LEFT)
        family.set("Arial")
        # Font Style
        self.stl = StringVar()
        Style = ttk.Combobox(combo, width=10, textvariable=self.stl, values=["normal","bold","italic","bold italic"])
        Style.pack(side=LEFT)
        Style.set("normal")
        # Font Size    
        self.size = StringVar()
        Size = ttk.Combobox(combo, width=5, textvariable=self.size, values=[x for x in range(100)])
        Size.pack(side=LEFT)
        Size.set("15")

        but = Frame(self.fontwin,pady=40)
        Button(but,command=self.apply,text="Apply",padx=7,pady=7).pack(side=LEFT)
        Button(but,command=self.ok,text="Ok",padx=7,pady=7).pack(side=LEFT)
        Button(but,command=self.fontwin.destroy,text="Cancel",padx=7,pady=7).pack(side=LEFT)
        but.pack()
        family.event_generate('<Down>'); Style.event_generate('<Down>'); Size.event_generate('<Down>')
        self.fontwin.mainloop()
        