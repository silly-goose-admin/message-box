from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

white='#FFFFFF'
lightgrey='#555555'
grey='#333333'
darkgrey='#111111'
black='#000000'
red='#FA5252'
gold='#FCC419'
green='#4DE651'
lightgreen='#8BDC8C'

class IMG:
    def get_image(image_path):
        img=Image.open(image_path)
        img=img.resize((20, 20), Image.LANCZOS)
        img=ImageTk.PhotoImage(img)
        return img

class AppMsg:
    def __init__(self, parent, width=310, height=90):
        self.root=tk.Toplevel(parent)
        self.root.geometry(f'{width}x{height}')
        self.root.config(bg=darkgrey)
        self.root.overrideredirect(True)

        self.info=IMG.get_image('icons/indication/info.png')
        self.warning=IMG.get_image('icons/indication/warning.png')
        self.error=IMG.get_image('icons/indication/error.png')
        
        self.close=IMG.get_image('icons/window/close.png')

        self.title_bar=tk.Frame(self.root, bg=grey, height=20)
        self.title_bar.pack(fill=X, side=TOP)
        self.title_bar.pack_propagate(False)

        self.message=tk.Frame(self.root, bg=darkgrey, height=70)
        self.message.pack(fill=X, side=BOTTOM)
        self.message.pack_propagate(False)

        self.create_widgets()
        self.center_window(width, height)

    def create_widgets(self):
        self.close_button=tk.Button(self.title_bar, bg=grey, image=self.close,
                                    command=self.root.destroy, relief='flat')
        self.close_button.pack(side=RIGHT)

        self.title=tk.Label(self.title_bar, text='App Message', bg=grey)
        self.title.pack(side=LEFT)

        self.msgicon=tk.Label(self.message, bg=darkgrey, bd=0, image=self.info)
        self.msgicon.pack(side=tk.LEFT, padx=5, pady=5)

        self.msgtxt=tk.Label(self.message,
                             wraplength=280, bg=darkgrey, fg=lightgrey)
        self.msgtxt.place(anchor=tk.CENTER, relx=0.5, rely=0.5)

        self.title_bar.bind('<Button-1>', self.start_move)
        self.title_bar.bind('<B1-Motion>', self.move_window)

    def center_window(self, width, height):
        self.root.update_idletasks()
        parent_width = self.root.winfo_screenwidth()
        parent_height = self.root.winfo_screenheight()

        x = (parent_width // 2) - (width // 2)
        y = (parent_height // 2) - (height // 2)

        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def start_move(self, event):
        self.root.x = event.x
        self.root.y = event.y

    def move_window(self, event):
        x = event.x_root - self.root.x
        y = event.y_root - self.root.y
        self.root.geometry(f'+{x}+{y}')
    
    def config_icon(self, msgtype):
        if msgtype == 'info':
            self.msgicon.config(image=self.info)
        elif msgtype == 'warning':
            self.msgicon.config(image=self.warning)
        elif msgtype == 'error':
            self.msgicon.config(image=self.error)
    
    def config_message(self, msg):
        self.msgtxt.config(text=msg)

    def show(self):
        self.root.after(3000, self.root.destroy)
    
    def info_msg(parent_frame, msg):
        app_msg=AppMsg(parent_frame)
        app_msg.config_icon('info')
        app_msg.config_message(msg)
        app_msg.show()

    def warning_msg(parent_frame, msg):
        app_msg=AppMsg(parent_frame)
        app_msg.config_icon('warning')
        app_msg.config_message(msg)
        app_msg.show()
        
    def error_msg(parent_frame, msg):
        app_msg=AppMsg(parent_frame)
        app_msg.config_icon('error')
        app_msg.config_message(msg)
        app_msg.show()
