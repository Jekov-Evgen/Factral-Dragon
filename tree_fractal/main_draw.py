from tkinter import ttk
from tkinter import *
from draw_dragon import dragon_curve

class MainWindow:
    def __init__(self) -> None:
        pass
    
    def start(self):
        root = Tk()
        root.title("Кривая дракона")
        frm = ttk.Frame(root, padding=10)
        frm.grid
        
        ttk.Label(text="Введите количесвто итераций", 
                  font="30").grid(row=0, column=0, padx=10, pady=10)
        
        self.itr = ttk.Entry()
        self.itr.grid(row=1, column=0, padx=10, pady=10)
        
        ttk.Button(text="Запустить итерации", 
                   command=self.button_processing).grid(row=2, column=0, padx=10, pady=10)
        
        root.mainloop()
        
    def button_processing(self):
        try:
            quantity = int(self.itr.get())
            dragon_curve(quantity, 20)
        except:
            info = Toplevel()
            
            Label(info, text="Вы ввели значение которое невозможно перевести в целочисленное", 
                  font="30").grid(row=0, column=0, padx=10, pady=10)
            
            Button(info, text="OK", command=info.destroy).grid(row=1, column=0, padx=10, pady=10)