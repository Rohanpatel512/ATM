"""
---------------------------------------------------
A page displayed once user logs into their account.
Given three options (deposit, withdraw, and check
balance).
---------------------------------------------------
Author: Rohan Patel
_updated_= "2022-07-26"
---------------------------------------------------
"""

# Imports
from tkinter import *
from tkinter import ttk
from user import User

class Options:

    def __init__(self, window, account_number, pin_number):
        """
        ---------------------------------------------
        Intializes the options page displayed on users
        screen.
        ---------------------------------------------
        Parameters:
            window - The app displayed on screen (Tkinter)
            account_number - Users account number (int)
            pin_number - Users PIN number (int)
        Returns:
            none
        ---------------------------------------------
        """
        self.user = User(account_number, pin_number)
        self.display_page(window)

    def display_page(self, window):
        """
        -----------------------------------------------
        Displays the options page to user.
        -----------------------------------------------
        Parameter:
            window - The app displayed to user (Tkinter)
        Returns:
            none
        -----------------------------------------------
        """

        # Calculations
        # TODO: Creates three buttons and adds to frame, adds frame to page/notebook.
        option_frame = ttk.Frame(window, width=400, height=300)

        # Fill up the window with option frame
        option_frame.pack(fill=BOTH, expand=True)

        # Create three buttons
        deposit_button = Button(option_frame, text="Deposit", width=20, height=2,
                                command=lambda: self.open_deposit(window, option_frame))
        withdraw_button = Button(option_frame, text="Withdraw", width=20, height=2,
                                 command=lambda: self.open_withdraw(window, option_frame))
        balance_button = Button(option_frame, text="Check Balance", width=20, height=2,
                                command=lambda: self.open_balance(window, option_frame))

        # Add all three buttons to frame
        deposit_button.grid(row=1, column=1, padx=5, pady=5)
        withdraw_button.grid(row=2, column=1, padx=5, pady=5)
        balance_button.grid(row=3, column=1, padx=5, pady=5)

        # Returns
        # TODO: Returns none
        return

    def open_deposit(self, window, option_frame):
        """
        ------------------------------------------------------------
        Displays the deposit tab where user enters amount to
        deposit
        ------------------------------------------------------------
        Parameter:
            window - The app displayed to user (Tkinter)
            option_frame - Page that is displayed to user once they've
            logged in (Frame)
        Returns:
            none
        ------------------------------------------------------------
        """
        # Calculations
        # TODO: Creates a entry field, and two buttons which are added to frame
        option_frame.destroy()
        deposit_frame = ttk.Frame(window, width=400, height=300)

        # Fill up the window with frame
        deposit_frame.pack(fill=BOTH, expand=True)

        # Create an entry field and two buttons
        deposit_amount_field = Entry(deposit_frame, width=40)
        deposit_button = Button(deposit_frame, text="Deposit", width=20, height=2,
                                command=lambda: self.user.deposit(deposit_amount_field.get()))
        back_button = Button(deposit_frame, text="\u2190", width=20, height=2,
                                command=lambda: self.go_back(window, deposit_frame))

        # Add the widgets to frame
        deposit_amount_field.place(relx=.43, rely=.3, anchor=CENTER)
        deposit_button.place(relx=.3, rely=.5, anchor=CENTER)
        back_button.place(relx=.7, rely=.5, anchor=CENTER)

        # Returns
        # TODO: Return none
        return

    def open_withdraw(self, window, option_frame):
        """
        -------------------------------------------------------------
        Displays the withdraw tab where user enters amount to
        withdraw
        -------------------------------------------------------------
        Parameter:
            window - The app displayed on screen to user (Tkinter)
            option_frame - Page that is displayed to user once they've
            logged in (Frame)
        Returns:
            none
        -------------------------------------------------------------
        """
        # Calculations
        # TODO: Creates a entry field, and two buttons which are added to frame
        option_frame.destroy()
        withdraw_frame = ttk.Frame(window, width=400, height=300)

        # Fill up the window with frame
        withdraw_frame.pack(fill=BOTH, expand=True)

        # Create an entry field and two buttons
        withdraw_amount_field = Entry(withdraw_frame, width=40)
        withdraw_button = Button(withdraw_frame, text="Withdraw", width=20, height=2,
                                 command=lambda: self.user.withdraw(withdraw_amount_field.get()))
        back_button = Button(withdraw_frame, text="\u2190", width=20, height=2,
                                 command=lambda: self.go_back(window, withdraw_frame))

        # Add the widgets to frame
        withdraw_amount_field.place(relx=.43, rely=.3, anchor=CENTER)
        withdraw_button.place(relx=.3, rely=.5, anchor=CENTER)
        back_button.place(relx=.7, rely=.5, anchor=CENTER)

        # Returns
        # TODO: Return none
        return

    def open_balance(self, window, option_frame):
        """
        -------------------------------------------------------------
        Displays the check balance tab where can check amount of
        money they have
        -------------------------------------------------------------
        Parameter:
            window - The app that is displayed to user on screen (Tkinter)
            option_frame - Page that is displayed to user once they've
            logged in (Frame)
        Returns:
            none
        -------------------------------------------------------------
        """

        # Calculations
        # TODO: Displays the balance to user, and a back button to go back
        option_frame.destroy()
        balance_frame = Frame(window, width=400, height=300)

        # Fill up the window with frame
        balance_frame.pack(fill=BOTH, expand=True)

        # Create the text to be displayed to user
        text = f"Your current balance is: ${self.user.get_balance():,.2f}"

        # Create a label and back button
        balance_label = Label(text=text, font=('Helvetica 15 bold'))
        back_button = Button(text="\u2190", width=20, command=lambda: self.go_back(window, balance_frame))

        # Add the widgets to balance frame
        balance_label.place(relx=.5, rely=.3, anchor=CENTER)
        back_button.place(relx=.5, rely=.5, anchor=CENTER)

        # Returns
        # TODO: Return nothing
        return

    def go_back(self, window, page):
        """
        ---------------------------------------------------------------
        When back button is clicked from a page, user goes back to the
        options page.
        ---------------------------------------------------------------
        Parameter:
            window - The app being displayed on screen (Tkinter)
            page - The page that is shown to user (Frame)
        Returns:
            none
        ---------------------------------------------------------------
        """
        # Calculations
        # TODO: Go back from page to options page
        page.destroy()
        self.display_page(window)

        # Returns
        # TODO: Return nothing
        return