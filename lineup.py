# -*- coding: utf-8 -*-
"""
Created on 2017-11-24

@author: 강유신
"""

from tkinter import *
#from PIL import Image, ImageTk
import cv2


class Application(Frame):
    """
    전체 내용을 Window Frame으로 보여주는 Application
    input : Frame
    output : 정리된 Window Frame
    """

    def __init__(self, master=None):

        # parameters that you want to send through the Frame class.
        super().__init__(master)

        # run init_window which doesn't yet exist
        self.create_widgets()

    # Creation of wiget_window
    def create_widgets(self):

        # change the title of our master create_widgets
        self.master.title("YESIR LINE UP SIMULATOR")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        # added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Show Img", command=self.show_Img)

        # added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)

        #self.hi_there = Button(self)
        #self.hi_there["text"] = "Hello World\n(click me)"
        #self.hi_there["command"] = self.say_hi
        #self.hi_there.pack(side="top")

        self.quit = Button(self, text="QUIT", fg="red", command=root.destroy)
        self.quit.pack(side="bottom")

    # print "hi" message
    def say_hi(self):
        print("hi there, everyone!")

    # close widget_window
    def client_exit(self):
        exit()

    # img attach on widget_window
    def show_Img(self):
        # load = Image.open("20170113_183109.jpg")
        # render = ImageTk.PhotoImage(load)

        # labels can be text or images
        # img = Label(self, image=render)
        # img.image = render
        # img.place(x=0, y=0)
        img = cv2.imread("20170113_183109.jpg", 1)
        resized_img = cv2.resize(img, (int(img.shape[1]/2),
                                        int(img.shape[0]/2)))

        img_label = Label(self, image=resized_img)
        img.place(x=0, y=0)


root = Tk()
root.geometry("400x300")
app = Application(root)
app.mainloop()
