import random
from tkinter import *
from tkinter import ttk 
from ctypes import windll

TOP_BG = "#000000"
BOTTOM_BG = "#14213d"
LINE_BG = "#fca311"
SYMB_BG = "#e5e5e5"
HIGHLIGHT_CL = "#fb8500"
RESET_BG = "#98c1d9"

TOP_FONT = ("Comic Sans", 15)
BUTTON_FONT = ("Comic Sans", 25)

windll.shcore.SetProcessDpiAwareness(1)

class Game():
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("410x500+1000+250")
        self.window.resizable(0,0)
        
        self.button = [[0,0,0],
                       [0,0,0],
                       [0,0,0]]
        self.count = 0
        self.choices = ["X","O"]
        self.result = False
        
        self.create_frames()
        self.create_buttons()
        
    def create_top_frame(self):
        self.top_frame = Frame(self.window, height=100, bg=TOP_BG)
        self.top_frame.pack(anchor=N, fill=X)
        self.top_frame.propagate(FALSE)
        self.top_frame.columnconfigure(0, weight=1)
        self.top_frame.columnconfigure(1, weight=1)
        self.top_frame.columnconfigure(2, weight=1)
        self.top_frame.rowconfigure(0, weight=1)
        
    def create_bottom_frame(self):  
        self.bottom_frame = Frame(self.window, height=500, bg=LINE_BG)
        self.bottom_frame.pack(anchor=S, fill="both", expand=True)
        self.bottom_frame.propagate(FALSE)
        
    def create_frames(self):
        self.create_top_frame()
        self.res_label = self.top_switches()
        self.create_bottom_frame()
        
    def top_switches(self):
        res_label = Label(self.top_frame, text="Winner is:  ", font=TOP_FONT, bg=TOP_BG, foreground=SYMB_BG)
        res_label.grid(row=0, column=0, columnspan=2)
        
        button = Button(self.top_frame, text="Reset", font=TOP_FONT, foreground=TOP_BG, bg=RESET_BG, command=self.clear, pady=1)
        button.grid(row=0, column=2, sticky=E)
        
        return res_label
    
    def create_buttons(self):
        for i in range(0,3):
            self.bottom_frame.columnconfigure(i, weight=1)
            self.bottom_frame.rowconfigure(i, weight=1)
            for j in range(0,3):
                self.button[i][j] = Button( self.bottom_frame,
                                            font=BUTTON_FONT,
                                            activebackground=BOTTOM_BG,
                                            foreground=SYMB_BG,
                                            bg=BOTTOM_BG,
                                            height=2, width=2, padx=37, pady=9,
                                            relief=FLAT, anchor=CENTER,
                                            command= lambda i=i, j=j: self.click(i,j))
                self.button[i][j].grid(row=i,column=j)
    
    def click(self,i,j):
        if self.result == True:
            self.clear()
        else:
            self.res_label.config(text= "Winner is:  ")
            if self.count % 2 == 0:
                self.button[i][j]['text'] = self.choices[0]
                self.count += 1
                self.check_result()
            else:
                self.button[i][j]['text'] = self.choices[1]
                self.count += 1
                self.check_result()
    
    def check_result(self):
        for row in range(0,3):
            for column in range(0,3):
                if (self.button[row][0]['text'] == self.button[row][1]['text'] == self.button[row][2]['text']) and self.button[row][0]['text'] != "":
                    self.result = True
                    self.res_label.config(text= "Winner is:  "+ self.choices[(self.count % 2) - 1])
                    self.button[row][0]['foreground'] = self.button[row][1]['foreground'] = self.button[row][2]['foreground'] = HIGHLIGHT_CL
                    
                elif (self.button[0][column]['text'] == self.button[1][column]['text'] == self.button[2][column]['text']) and self.button[0][column]['text'] != "":
                    self.result = True
                    self.res_label.config(text= "Winner is:  "+ self.choices[(self.count % 2) - 1])
                    self.button[0][column]['foreground'] = self.button[1][column]['foreground'] = self.button[2][column]['foreground'] = HIGHLIGHT_CL
                    
                elif (self.button[0][0]['text'] == self.button[1][1]['text'] == self.button[2][2]['text'])  and self.button[1][1]['text'] != "":
                    self.result = True
                    self.res_label.config(text= "Winner is:  "+ self.choices[(self.count % 2) - 1])
                    self.button[0][0]['foreground'] = self.button[1][1]['foreground'] = self.button[2][2]['foreground'] = HIGHLIGHT_CL
                    
                elif (self.button[0][2]['text'] == self.button[1][1]['text'] == self.button[2][0]['text'])  and self.button[1][1]['text'] != "":
                    self.result = True
                    self.res_label.config(text= "Winner is:  "+ self.choices[(self.count % 2) - 1])
                    self.button[0][2]['foreground'] = self.button[1][1]['foreground'] = self.button[2][0]['foreground'] = HIGHLIGHT_CL
                    
    def clear(self):
        self.result = False
        self.res_label.config(text= "Winner is:  ")
        for i in range(0,3):
            for j in range(0,3):
                self.button[i][j]['text'] = ""
                self.button[i][j]['foreground'] = SYMB_BG
                self.count = 0
                
    def run(self):
        self.window.mainloop()    
    
if __name__ == "__main__":
    game = Game()
    game.run()