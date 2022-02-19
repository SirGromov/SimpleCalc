from tkinter import *
from math import *
from calculation import *


class Main(Frame):
    
    def __init__(self, root):
        self.operated = 0
        self.lastoper = 1
        self.root = root
        self.last = 'simple'
        super(Main, self).__init__(root)
        # После super() сразу вспомнилась шутка:
        # -Как вы выучили английский всего за день?
        # -Очень просто, там половину слов взяли из С++
        self.winConstructor('simple')

    def swap(self):
        self.root.destroy()
        self.root = Tk()
        self.root['bg'] = "black"
        self.root.title("Шайтан-считалка")
        self.root.resizable(False, False)
        self.root.iconbitmap(r'assets/icon.ico')
        self.last = self.varmode.get()
        self.winConstructor(self.varmode.get())

    # Джава дает о себе знать даже в названиях классов...
    def winConstructor(self, mode):
        # Мне очень лень прописывать каждую кнопку,
        # создам массив и опишу каждую циклом
        if mode == 'engeneer':
            btns = [
                "C", "Back", "*", "=", "sin(", "asin(", "isPrime",
                "1", "2", "3", "/", "cos(", "acos(", "LCM(",
                "4", "5", "6", "+", "tan(", "atan(", "GCD(",
                "7", "8", "9", "-", "log(", "!", "reduce(",
                ",", "0", ".", "%", "e", "pi", "isPerfect",
                "√", "**", "(", ")", "radians(", "degrees(", ""
            ]
            limx = 800
            enty = 31
            self.root.geometry("834x634+0+0")
        elif mode == 'simple':
            btns = [
                "C", "Back", "*", "=", 
                "1", "2", "3", "/", 
                "4", "5", "6", "+", 
                "7", "8", "9", "-", 
                ",", "0", ".", "%", 
                "√", "**", "(", ")"
            ]
            limx = 400
            enty = 18
            self.root.geometry("480x634+0+0")
        elif mode == 'coder':
            btns = [
                "C", "Back", "=", "A", 
                "1", "2", "3", "B", 
                "4", "5", "6", "C", 
                "7", "8", "9", "D", 
                ",", "0", ".", "E", 
                "+", "-", "*", "F"
            ]
            limx = 400
            enty = 18
            self.root.geometry("480x634+0+0")
        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.primalCalc(x)
            Button(text=bt, command=com,
                   font=("Comic Sans MS", 16), bg="black",
                   fg="white", activebackground="black",
                   activeforeground="white").place(
                       x=x, y=y, width=115, height=79)
            x += 117
            if x > limx:
                x = 10
                y += 81
        # Плохая идея, я хочу вывод результата в лейбле
        # После недели экспулатации передумал, пусть будет энтри
        self.rese = StringVar()
        self.res = "0"
        self.ent = Entry(textvariable=self.rese,
                         font=("Comic Sans MS", 32, "bold"),
                         fg="white", bg="black", width=enty)
        # АД ПЕРФЕКЦИОНИСТА!
        self.ent.place(x=11, y=50)
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        self.varmode = StringVar()
        self.varmode.set(self.last)

        self.modemenu = Menu(self.menu, tearoff=0)
        self.modemenu.add_radiobutton(label='Обычный', value='simple', variable=self.varmode, command=self.swap)
        self.modemenu.add_radiobutton(label='Инженер', value='engeneer', variable=self.varmode, command=self.swap)
        
        self.menu.add_cascade(label='Режим', menu=self.modemenu)
        
        self.winUpdate()
        # В программе с интерфейсом важна эстетичность!
        # И да, я пробовал .grid()

    # Функция, нужная для обработки ошибок,
    # введенных пользователем
    # Я для себя открыл eval(), ух, щас наворочу...
    def ErrorParser(self, oper):
        try:
            inp = eval(self.ent.get())
            if oper == "=": n = str(inp)
            elif oper == "√": n = str(inp**0.5)
            elif oper == "!": n = str(calculation.fact(inp))
            elif oper == "isPrime": n = str(calculation.isPrime(inp))
            elif oper == "isPerfect": n = str(calculation.isPerfect(inp))
            
        except Exception as e: n = e.__class__.__name__
        return n
    
    def primalCalc(self, operation):
        if operation == "C": self.res = ""
        elif operation == "Back":
            if not self.operated: self.res = self.res[0:-self.lastoper]
            else: self.res = ""
            self.operated = 0
            self.lastoper = 1
        elif operation in ["√", "=", "!", "isPrime", "isPerfect"]:
            self.res = str(self.ErrorParser(operation))
            self.lastoper = len(operation)
            self.operated = 1
        else:
            if self.res == "0" and operation == ".": self.res = "0"
            elif self.res == "0": self.res = ""
            self.res += operation
            self.lastoper = len(operation)
        self.winUpdate()
        # СВЯТЫЕ УГОДНИКИ! На джаве все выглядело бы лучше...

    def winUpdate(self):
        if self.ent.get() == "": self.res = "0"
        if self.res == "": self.res = "0"
        self.rese.set(self.res)


if __name__ == "__main__":
    root = Tk()
    root['bg'] = "black"
    root.title("Шайтан-считалка")
    root.geometry("480x634+0+0")
    root.resizable(False, False)
    root.iconbitmap(r'assets/icon.ico')
    Main(root).pack()
    root.mainloop()
