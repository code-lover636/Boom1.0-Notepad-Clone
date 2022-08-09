from utils import *

root = Tk()
root.geometry("800x470")
root.title("Boom Text Editor 1.0")
root.iconbitmap("assets/boom.ico")
root.config(bd=0)
WIDTH, HEIGHT = root.winfo_screenwidth(), root.winfo_screenheight()

screen = Text(root, width=WIDTH, height=HEIGHT, bg="white", bd=0, highlightbackground="blue", font="Arial")
screen.pack(side=LEFT,fill=BOTH, expand=True)

# CREATING MENU
MenuBar = MenuBar(root,screen)
menu_bar = Menu(root); root.config(menu=menu_bar)
# file
filemenu = Menu(menu_bar)
filemenu.add_command(label="New",command=MenuBar.erase)
filemenu.add_command(label="Open",command=MenuBar.open_file)
filemenu.add_command(label="Save",command=lambda: MenuBar.save_doc("rewrite"))
filemenu.add_command(label="Save As",command=lambda: MenuBar.save_doc("as"))
filemenu.add_separator()
filemenu.add_command(label="Exit    Alt+F4",command=root.destroy)
# edit
Editmenu = Menu(menu_bar)
Editmenu.add_command(label="Cut       Ctrl+X",command=lambda: MenuBar.edit("cut"))
Editmenu.add_command(label="Copy    Ctrl+C",command=lambda: MenuBar.edit("copy"))
Editmenu.add_command(label="Paste    Ctrl+V",command=lambda: MenuBar.edit("paste"))
Editmenu.add_command(label="Delete        Del",command=lambda: MenuBar.edit("delete"))
Editmenu.add_separator()
Editmenu.add_command(label="Search",command=MenuBar.search)
# format
Formatmenu = Menu(menu_bar)
# Formatmenu.add_command(label="Word Wrap",command=erase)
Formatmenu.add_command(label="Font",command=MenuBar.font)
# About
Aboutmenu = Menu(menu_bar)
Aboutmenu.add_command(label="About this project",command=MenuBar.show_about)

menu_bar.add_cascade(label="File", menu=filemenu)
menu_bar.add_cascade(label="Edit", menu=Editmenu)
menu_bar.add_cascade(label="Format", menu=Formatmenu)
menu_bar.add_cascade(label="About", menu=Aboutmenu)

root.mainloop()

