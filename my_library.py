import tkinter as tk
import numpy as np
import tkinter.font
import tkinter.ttk as ttk

window = tk.Tk()
window.geometry('640x411')
# window.resizable(0,0)
# bg_img = tk.PhotoImage(file = "C:/MyStorage/Git/Time To Practise/GUIGame/images/background.png")
# background_label = tk.Label(image=bg_img)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
window.title("Shortest Way In Graph")
window.focus_set()
window.grab_set()
myFont = tkinter.font.Font(family = 'Helvetica' , size = 12, weight = 'bold')


class App(object):
    def __init__(self, master):
        self.MyWindow = tk.Frame(master)

        self.welcoming_label = tk.Label(window,
                                        text="Welcome to my app!\n On next page you can choose shortest way method, size  \nof matrix, and enter it.",
                                        font=("Times New Romans", 18))
        self.welcoming_label.grid()

        self.matrix_size = tk.Spinbox(window, from_=1, to=15, width=5)
        self.matrix_size.grid()

        self.start_button = tk.Button(window,
                                      text="Press me to continue...",
                                      command=self.clicked_1st)
        self.start_button.grid(column=0, row=2)

        self.cont = tk.Button(window,
                              text="Press to continue")

        self.check_sort = tk.Checkbutton(window,
                                         text="Sorting algorithms")

    def clicked_1st(self):
        # self.welcoming_label.configure(text=f"Hello! Choose one of my programs:")
        self.start_button.destroy()
        self.welcoming_label.destroy()
        self.matrix_size.destroy()
        self.build_matrix(int(self.matrix_size.get()))

    def build_matrix(self, size):
        rows = []
        for i in range(size):
            cols = []
            for j in range(size):
                e = tk.Entry(window, width=5, font=myFont, bd=5)
                e.grid(row=i, column=j, sticky=tk.NSEW)
                cols.append(e)
            rows.append(cols)
        window.geometry('%dx%d+0+0' % (15*size*4, 4*15*4))
        self.cont



app = App(window)
window.mainloop()
