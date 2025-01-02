# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: frontend.py
# Bytecode version: 3.13.0rc3 (3571)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import os
import sys
import threading
import tkinter as tk
from PIL import Image, ImageTk
from challenge import test_1, test_2, test_3, test_4, test_5, test_6, get_flag
tests = [test_1, test_2, test_3, test_4, test_5, test_6, get_flag]
button_texts = ['   Espresso     ', 'Coffe (C 14)', '  CapChock  ', '    Moka    ', '    Corretto    ', '    Ginseng Coffee     ']
display_when_selected = [' A QUICK COFFEE, AT THE RIGHT TIME                          ', ' ONLY FOR VIP CUSTOMERS!                          ', ' CLASSICAL BUT COMPACT COFFEE                          ', ' REAL HANDMADE COFFEE                          ', ' THE PROGRAMMER\'S CHOICE                          ', ' FOR THE WEALTHY ONES                          ', ' YOU HAVE TO BUY ALL THE OTHER COFFEE FIRST!                          ']

def get_file(relative_path):
    try:
        base_path = sys._MEIPASS
    return os.path.join(base_path, relative_path)
    except Exception:
        base_path = os.path.abspath('.')

class LockMechanismApp:
    def __init__(self, root):
        self.root = root
        self.passed_checks = ['a'] * 6
        root.resizable(False, False)
        self.root.title('Reverse the Coffee Machine')
        self.root.geometry('350x760')
        self.root.configure(background='#EADEDA')
        self.logo = ImageTk.PhotoImage(Image.open(get_file('static/logo.png')).resize((250, 160)))
        btn = tk.Label(root, image=self.logo, width=350, background='#EADEDA')
        btn.grid(row=0, column=0, pady=(10, 0), columnspan=2)
        self.information_frame = tk.Frame(root, bg='#3B3232')
        self.information_frame.grid(row=1, column=0, pady=20, padx=(20, 0))
        self.display = 'Select a beverage                             '
        self.status_label = tk.Label(self.information_frame, bg='#363131', width=30, height=2, text=self.display, font=('Arial', 12))
        self.status_label.pack(pady=10)
        self.index = 0
        self.start_sliding_text()
        self.canvas = tk.Canvas(self.information_frame, width=220, height=40, bg='#363131', highlightthickness=0, bd=0)
        self.canvas.pack(pady=(0, 10))
        self.money_canvas = tk.Canvas(self.root, width=16, height=100, bg='#2F323A')
        self.money_canvas.grid(row=1, column=1, pady=(5, 10), padx=20)
        self.money_canvas.create_rectangle(4, 2, 12, 98, fill='black')
        self.key_pins = []
        self.pin_height = 30
        self.pin_width = 200
        self.pin_gap = 5
        self.initial_x = 12
        self.initial_y = 5
        self.pin_drop_distance = 20
        self.slectedBeverage = (-1)
        for i in range(1):
            x1 = self.initial_x + i * (self.pin_width + self.pin_gap)
            y1 = self.initial_y
            x2 = x1 + self.pin_width
            y2 = y1 + self.pin_height
            pin = self.canvas.create_rectangle(x1, y1, x2, y2, fill='#343030', outline='#343030')
            self.key_pins.append(pin)
        self.broken_img = ImageTk.PhotoImage(Image.open(get_file('static/out_of_service.png')).resize((20, 20)))
        self.imgs = [ImageTk.PhotoImage(Image.open(get_file('static/tea.png')).resize((70, 70))), ImageTk.PhotoImage(Image.open(get_file('static/caffe.png')).resize((70, 70))), ImageTk.PhotoImage(Image.open(get_file('static/capc.png')).resize((70, 70))), ImageTk.PhotoImage(Image.open(get_file('static/moka.png')).resize((70, 70))), ImageTk.PhotoImage(Image.open(get_file('static/choc.png')).resize((70, 70)))]
        self.buttons = []
        button_frame = tk.Frame(root, background='#f3e7cc')
        button_frame.grid(row=2, column=0, pady=(40, 15), ipady=10, padx=(0, 0), columnspan=2)
        for i in range(3):
            for j in range(2):
                button_index = i * 2 + j
                btn = tk.Button(button_frame, background='#E6A555', image=self.imgs[button_index], text=button_texts[button_index], compound='top', width=110, command=lambda idx=button_index: self.lockBeverage(idx), highlightthickness=0, bd=0)
                btn.grid(row=i, column=j, padx=10, pady=5, ipadx=0)
                btn.config(state=tk.NORMAL)
                self.buttons.append(btn)
        flag_btn = tk.Button(button_frame, background='#E6A555', text='Coffe, ehm flag', command=lambda idx=button_index: self.lockBeverage(6), highlightthickness=0, bd=0)
        flag_btn.grid(row=3, column=0, padx=10, pady=10, ipadx=0)
        flag_btn.config(state=tk.NORMAL)
        self.buttons.append(flag_btn)
        self.select_btn = tk.Button(button_frame, background='#E6A555', text='SELECT', command=self.start_check, highlightthickness=0, bd=0)
        self.select_btn.grid(row=3, column=1, padx=10, pady=10, ipadx=0)
        self.select_btn.config(state=tk.NORMAL)

    def start_check(self):
        if self.slectedBeverage == (-1):
            pass  # postinserted
        return

    def lockBeverage(self, index):
        if self.slectedBeverage!= (-1):
            self.unlockBeverage()
        return

    def unlockBeverage(self):
        self.enable_buttons()
        self.slectedBeverage = (-1)
        self.display = 'Select a beverage                             '

    def run_check(self, index):
        self.select_btn.config(state=tk.DISABLED)
        if index!= 6:
            self = tests[index]()
            self.root.after(0, lambda: self.update_gui_check(index, result))

    def update_gui_check(self, index, result):
        if result[0]:
            self.canvas.itemconfig(self.key_pins[0], fill='green')
            self.passed_checks[index] = result[1]
        self.root.after(5000, self.reset_pin, index)
        self.root.after(5000, self.unlockBeverage)

    def update_gui_flag(self):
        passed = False
        if not any((check is None for check in self.passed_checks)):
            try:
                self.display = tests[(-1)](''.join(self.passed_checks)) + '                             '
                self.canvas.itemconfig(self.key_pins[0], fill='green')
                passed = True
        if not passed:
            self.canvas.itemconfig(self.key_pins[0], fill='red')
            self.display = 'CHECK FAILED, NO FLAG!                          '
        self.root.after(5000, self.reset_pin, 0)
        self.root.after(5000, self.unlockBeverage)
        except:
            pass  # postinserted
        pass

    def reset_pin(self, index):
        self.canvas.itemconfig(self.key_pins[0], fill='#343030')

    def enable_buttons(self):
        for btn in self.buttons:
            btn.config(state=tk.NORMAL)
        self.select_btn.config(state=tk.NORMAL)

    def disable_buttons(self):
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)
        self.select_btn.config(state=tk.DISABLED)

    def start_sliding_text(self):
        self.status_label.config(text=self.display[self.index:] + self.display[:self.index], fg='#68ad2f')
        self.index = (self.index + 1) % len(self.display)
        self.root.after(300, self.start_sliding_text)
if __name__ == '__main__':
    root = tk.Tk()
    app = LockMechanismApp(root)
    root.mainloop()