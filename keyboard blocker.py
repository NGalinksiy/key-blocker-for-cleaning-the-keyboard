import tkinter as tk
from tkinter import ttk
import keyboard  # works only with the "keyboard" module. Еnter into the terminal: "pip install keyboard"
import sys


class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes('-topmost', True)  # window on top of other windows
        self.overrideredirect(True)  # hide the frame window
        self.resizable(False, False)  # disabling window resizing
        self.title('Keys blocker')  # window name
        self.show_text = True  # a boolean variable for changing the text on the button

        self.blocker_key = None  # variable for button
        self.combo_win = None  # variable for combobox

        self.set_ui()  # calling the interface with buttons

    def set_ui(self):

        self.frame = ttk.LabelFrame(self)
        self.frame.pack(side=tk.TOP)
        self.combo_win = ttk.Combobox(self.frame,  # create combobox
                                      values=["hide", "don't hide"],  # values combobox
                                      width=10,  # size combobox
                                      state="readonly")  # You can't enter your own value
        self.combo_win.current(1)  # the standard value is a combobox
        self.combo_win.pack(side=tk.LEFT)  # location of the combobox in the window
        self.blocker_key = ttk.Button(self, text="block all key", width=30,
                                      command=self.block_key)  # creating a button to lock keyboard
        self.blocker_key.pack(side=tk.TOP)  # location of the lock button in the window
        ttk.Button(self.frame, text="Exit", command=self.exit_but) \
            .pack(side=tk.LEFT)  # button for exit
        ttk.Button(self.frame, text="Move", command=self.move_application) \
            .pack(side=tk.RIGHT)  # button for creating window frames
        self.bind_class('Tk', '<Enter>', self.enter_mouse)  # when hovering over the window with the mouse
        self.bind_class('Tk', '<Leave>', self.leave_mouse)  # when taking the mouse out of the window

    def enter_mouse(self, event):
        if self.combo_win.current() == 0 or 1:  # always show the window on mouse hover
            self.geometry("")

    def leave_mouse(self, event):
        if self.combo_win.current() == 0:  # if the value of the combo box is hide (0 in the list)
            self.geometry(f'{self.winfo_width()}x1')  # , then hide when not hovering the mouse

    def block_key(self):

        if self.show_text is True:  # if the buttons are unlocked
            self.show_text = False
            self.blocker_key['text'] = "unblock all keys"  # text changes
            for i in range(150):  # the code that will block all buttons
                keyboard.block_key(i)
        else:
            self.show_text = True
            self.blocker_key['text'] = "block all keys"  # text changes
            for i in range(150):  # the code that will unblock all buttons
                keyboard.unblock_key(i)

    def move_application(self):

        if self.overrideredirect() is True:  # if the window has a frame
            self.overrideredirect(False)  # remove them
        else:
            self.overrideredirect(True)  # create them

    def exit_but(self):  # exit the program
        self.destroy()
        sys.exit()


root = Application()
root.mainloop()
