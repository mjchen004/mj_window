# import tkinter as tk 
# from tkinter import ttk 

# class Window(tk.Tk): 
#     def __init__(self,**kwargs):
#         super().__init__(**kwargs)
#         self.title("Header")
#         self.geometry("300x200")

#         button1:ttk.Button = ttk.Button(self,text="Top").pack(fill='both',expand=1)
    
#         button2:ttk.Button = ttk.Button(self,text="Middle").pack(fill='both',expand=1)
    
#         button3:ttk.Button = ttk.Button(self,text="Bottom").pack(fill='both',expand=1)
        
# if __name__ == '__main__':
#     window:Window = Window()
#     window.mainloop()

import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("Header")
        self.geometry("300x200")

        self.style = ttk.Style()
        self.style.theme_use('clam')  # Explicitly set a theme, e.g., 'clam', 'alt', 'default', 'classic'

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        button1 = ttk.Button(self, text="Top")
        button1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        button2 = ttk.Button(self, text="Middle")
        button2.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        button3 = ttk.Button(self, text="Bottom")
        button3.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

if __name__ == '__main__':
    window = Window()
    window.mainloop()
