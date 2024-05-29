import tkinter as tk 
from tkinter import ttk 

class Window(tk.Tk): 
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("Header")
        self.geometry("300x200")

        button1:ttk.Button = ttk.Button(self,text="Top").pack(fill='x')
    
        button2:ttk.Button = ttk.Button(self,text="Middle").pack(fill='x')
    
        button3:ttk.Button = ttk.Button(self,text="Bottom").pack(fill='x')
        
if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()