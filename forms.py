"""
-----------------------------------------------
Graphical User Interface for signup and login
pages
-----------------------------------------------
Author: Rohan Patel
_updated_ = "2022-07-26"
-----------------------------------------------
"""

# Imports
from tkinter import *
from tkinter import ttk
from account import Account

class Forms:

    def __init__(self):
        """
        ---------------------------------------------------
        Initializes an array that holds all entry field objects
        that user will enter information inside of. Initializes
        an account object.
        ---------------------------------------------------
        Returns:
            none
        ---------------------------------------------------
        """
        self.input_fields = []
        self.userAccount = Account()

    def open_login_form(self, window):
        """
        ----------------------------------------------------
        Opens and displays the login form to user
        ----------------------------------------------------
        Parameter:
            window - The app displayed to user (Tkinter)
        Returns:
            none
        ----------------------------------------------------
        """

        # Calculations
        # TODO: Display the login form
        # Create a notebook and a frame for login page
        login_frame = ttk.Frame(window, width=400, height=300)

        # Fill up the entire window with frame
        login_frame.pack(fill=BOTH, expand=True)

        # Make 2 labels, 2 fields, and 2 buttons
        account_label = Label(login_frame, text="Account #")
        pin_label = Label(login_frame, text="PIN #")
        account_number_field = Entry(login_frame, width=20)
        pin_number_field = Entry(login_frame, width=20)

        # Add all input fields to array
        self.input_fields = [account_number_field, pin_number_field]

        login = Button(login_frame, text="Login", width=20, height=2,
                       command=lambda: self.userAccount.login_user(self.input_fields, login_frame, window))
        back = Button(login_frame, text="\u2190", width=20, height=2,
                       command=lambda: login_frame.destroy())

        # Add all labels, fields, and buttons to frame
        account_label.grid(row=0, column=1, pady=5, sticky=W)
        account_number_field.grid(row=0, column=2, pady=5)
        pin_label.grid(row=1, column=1, pady=5, sticky=W)
        pin_number_field.grid(row=1, column=2, pady=5)
        login.grid(row=2, column=1, pady=5)
        back.grid(row=2, column=2, pady=5)

        # Returns
        # TODO: Return none
        return

    def open_signup_form(self, window):
        """
        -----------------------------------------------------
        Opens and displays the signup form to user
        -----------------------------------------------------
        Parameters:
            window - The app displayed to user (Tkinter)
        Returns:
            none
        -----------------------------------------------------
        """

        # Variables
        # TODO: Initialize variables
        row = 0
        column = 1
        label_titles = ["Firstname:", "Lastname:", "Account No:", "PIN #:"]

        # Calculations
        # TODO: Adds 4 labels, and 4 entry fields to the sign-up form
        signup_frame = ttk.Frame(window, width=400, height=300)

        # Fill up the entire window with frame
        signup_frame.pack(fill=BOTH, expand=True)

        # Creates four entry fields
        firstname_field = Entry(signup_frame, width=20)
        lastname_field = Entry(signup_frame, width=20)
        account_number_field = Entry(signup_frame, width=20)
        pin_number_field = Entry(signup_frame, width=20)

        # Create a list of fields
        self.input_fields = [firstname_field, lastname_field, account_number_field, pin_number_field]

        # Loop through the list
        for i in range(0, len(label_titles)):
            # Create a label
            label = Label(signup_frame, text=label_titles[i])

            # Put the label and its input field beside each other
            label.grid(row=row, column=column, padx=5, pady=5)
            self.input_fields[i].grid(row=row, column=column + 1, padx=5, pady=5, sticky=E)

            # Increase value of row
            row += 1

        # Add a sign up button at row 4
        signup_button = Button(signup_frame, text="Sign Up", width=15,
                               command=lambda: self.userAccount.signup_user(self.input_fields))
        signup_button.grid(row=4, column=1, pady=5, padx=10, sticky=W)

        # Add a back button at row 4
        back = Button(signup_frame, text="\u2190", width=15, command=lambda: signup_frame.destroy())
        back.grid(row=4, column=2, pady=5, sticky=W)

        # Returns
        # TODO: Return none
        return

    def get_input_fields(self):
        """
        -------------------------------------------------
        Allows outside classes to have access to the
        input fields where user inserts information
        -------------------------------------------------
        Returns:
            input_fields - Entry fields with user information
            (arr)
        -------------------------------------------------
        """
        # Returns
        # TODO: Return the array
        return self.input_fields