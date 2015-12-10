#!/usr/bin/env python3

""" GUI for Name that Shape """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from name_that_shape import *
import Tkinter
import tkMessageBox

"""
   Create a GUI for the Name That Shape program
   See name_shape_gui.png for specification
   Use the name_that_shape.py to perform computations
   For inputs that raise an error, pop up a modal dialog box
   For inputs that produce a shape name, display the string in the window
"""

class NameThatShapeGUI:


    def __init__(self):
        self.main_window = Tkinter.Tk()
        self.main_window.title("tk #10")
        # resize the window
        self.main_window.geometry("500x100")
        #background colour
        self.main_window.configure(background="#FFFFFF")

        # side entry
        self.entry = Tkinter.Frame(self.main_window)
        self.prompt_label = Tkinter.Label(self.entry, text='Enter the number of sides in the shape:')
        self.side_entry = Tkinter.Entry(self.entry, width=10)

        # show shape name
        self.name = Tkinter.Frame(self.main_window)
        self.name_label = Tkinter.Label(self.name, text='Name of Shape: ')
        self.shape = Tkinter.StringVar()
        self.shape.set("")
        self.shape_name = Tkinter.Label(self.name, textvariable=self.shape)

        # create button
        self.button = Tkinter.Frame(self.main_window)
        self.get_name = Tkinter.Button(self.button, text='Name', command=self.convert, width=4)
        self.quit = Tkinter.Button(self.button, text='Quit', command=self.main_window.destroy, width=3)

        # pack the widgets
        self.prompt_label.pack(side='left')
        self.side_entry.pack(side='left')

        self.name_label.pack(side='left')
        self.shape_name.pack(side='left')

        self.get_name.pack(side='left')
        self.quit.pack(side='left')

        # Pack the frames in the order they will appear
        self.entry.pack()
        self.name.pack()
        self.button.pack()


        Tkinter.mainloop()

    def error_message(self):
        tkMessageBox.showinfo("Response", "\"" + self.side_entry.get() + "\" is invalide input, please try it again!")

    def convert(self):
        shapename = name_that_shape(self.side_entry.get())
        if shapename is None:
            self.error_message()
        else:
            self.shape.set(shapename)

# Instantiating the object
ntsg = NameThatShapeGUI()




import Tkinter
import tkMessageBox


class NameThatShapeGUI:
    def __init__(self):
        # Create the main window widget
        self.main_window = Tkinter.Tk()
        self.main_window.geometry('500x100')

        # Create two frames to group widgets
        self.top_frame = Tkinter.Frame(self.main_window)
        self.middle_frame = Tkinter.Frame(self.main_window)
        self.bottom_frame = Tkinter.Frame(self.main_window)

        # Create widgets for the top frame
        self.prompt_label = Tkinter.Label(self.top_frame,
                                          text="Enter the number of sides in the shape:")
        self.side_entry = Tkinter.Entry(self.top_frame, width=10)

        # Pack the top frame's widgets
        self.prompt_label.pack(side="left")
        self.side_entry.pack(side="left")

        # Create widgets for the middle frame
        self.descr_label = Tkinter.Label(self.middle_frame, text="Name of shape:")
        self.value = Tkinter.StringVar()
        self.value.set("")
        self.shape_name = Tkinter.Label(self.middle_frame, textvariable=self.value)

        # Pack the middle frame's widgets
        self.descr_label.pack(side="left")
        self.shape_name.pack(side="left")


        # Create widgets for bottom frame
        self.conv_button = Tkinter.Button(self.bottom_frame,
                                          text="Name",
                                          command=self.convert)

        self.quit_button = Tkinter.Button(self.bottom_frame,
                                          text="Quit",
                                          command=self.main_window.destroy)

        # Pack the bottom buttons
        self.conv_button.pack(side="left")
        self.quit_button.pack(side="left")

        # Pack the frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()


        # Enter the Tkinter main loop
        Tkinter.mainloop()

    def convert(self):
        # Display and info dialog box
        self.value.set(self.side_entry.get())
        tkMessageBox.showinfo("Response", self.side_entry.get())

# Create an instance of the MainWindow class
ntsg = NameThatShapeGUI()

