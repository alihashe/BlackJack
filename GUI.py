# import tkinter as tk
# from tkinter import Label, Button

# class GUI:

#     def __init__(self):
#         self.gui = tk.Tk(className="BlackJack")
#         self.gui['bg'] = 'green'
#         self.gui.bind("<Escape>", self.exit_fullscreen)
#         self.gui.attributes("-fullscreen", True)
#         self.gui.minsize(800,600)

#     def exit_fullscreen(self, event):
#         print(event)
#         self.gui.attributes("-fullscreen", False)
    
#     def display_main_window(self):
#         label = Label(self.gui, text="Welcome to BlackJack!", bg='green', font=50)
#         label.pack(pady=80)
#         self.gui.mainloop()
