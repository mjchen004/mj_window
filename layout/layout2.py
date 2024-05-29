import tkinter as tk 
from tkinter import ttk 

class Window(tk.Tk): 
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("Header")
        self.geometry("500x200")

        button1:ttk.Button = ttk.Button(self,text="Left").pack(side='left')
    
        button2:ttk.Button = ttk.Button(self,text="This is the Center Button").pack(side='left')

        button3:ttk.Button = ttk.Button(self,text="Right").pack(side='left')
        
    
    

if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()