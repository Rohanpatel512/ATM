"""
-----------------------------------------------
Graphical User Interface for home page
-----------------------------------------------
Author: Rohan Patel
_updated_ = "2022-07-14"
-----------------------------------------------
"""

# Imports
from tkinter import *
from tkinter import ttk
from forms import Forms


class Home:

   def __init__(self, title, width, height):
       """
       -------------------------------------------
       Initializes the home page with a title,
       login, and sign up button for user.
       -------------------------------------------
       Parameter:
           title - Title displayed on home page (str)
           width - Width of the window displayed (int)
           height - Height of window displayed (int)
       Returns:
           None
       -------------------------------------------
       """
       self._title = title
       self._width = width
       self._height = height
       self._window = Tk()

       self._window.title(self._title)
       self._window.geometry("{}x{}".format(self._width, self._height))
       self._window.resizable(width=False, height=False)

       self.form = Forms()

       self.add_components()

   def add_components(self):
       """
       ----------------------------------------------------
       Adds 1 label, and 2 buttons to the home screen
       ----------------------------------------------------
       Returns:
           none
       ----------------------------------------------------
       """

       # Variables
       # TODO: Initailize variables
       home_title = Label(text=self._title)
       login_button = Button(text="Login", width=20, height=2, command=lambda: self.form.open_login_form(self._window))
       sign_up_button = Button(text="Create Account", width=20, height=2, command=lambda: self.form.open_signup_form(self._window))

       # Calculation
       # TODO: Adds a title, and 2 labels to the home page
       # Set the size of the font
       home_title.config(font=('Raleway Bold', 40))

       # Adds 2 buttons and a label to the center
       home_title.place(relx=0.5, rely=0.1, anchor=CENTER)
       login_button.place(relx=0.5, rely=0.3, anchor=CENTER)
       sign_up_button.place(relx=0.5, rely=0.5, anchor=CENTER)

       # Display the app to user
       self._display()

       # Returns
       # TODO: Returns none
       return


   def _display(self):
       """
       ----------------------------------------------------
       Displays the GUI to user
       ----------------------------------------------------
       Returns:
           none
       ----------------------------------------------------
       """
       # Calculations
       # TODO: Displays the window to user
       self._window.mainloop()

       # Returns
       # TODO: Return nothing
       return
