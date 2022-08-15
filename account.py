"""
-----------------------------------------------
Validates user input when signing in or logging
in. Checks through database to see if user exists
when logging and signing in.
-----------------------------------------------
Author: Rohan Patel
_updated_ = "2022-07-  25"
-----------------------------------------------
"""

# Imports
import mysql.connector
from options import Options
from tkinter import *
from tkinter import messagebox


class Account:

    def __init__(self):
        """
        --------------------------------------------
        Connects application to the database to use
        for input validation.
        --------------------------------------------
        Returns:
            none
        --------------------------------------------
        """
        self.database = mysql.connector.connect (host="127.0.0.1", user="root", passwd="Myappdb3031*",
             database="atmdatabase", auth_plugin='mysql_native_password')
        self.cursor = self.database.cursor(buffered=True)


    def login_user(self, input_fields, login_frame, window):
        """
        --------------------------------------------
        Checks if user has created account (exists
        within database). Allows user into the account
        if it does exist, otherwise sends error message
        --------------------------------------------
        Parameters:
            input_fields - All entry fields user has
            entered information inside of in the login
            form. (array of Entries)
            login_frame - Login page that is displayed
            to user (Frame)
            window - The app that is displayed to user
            (Tkinter)
        Returns:
            none
        --------------------------------------------
        """

        # Calculations
        # TODO: Check if account number and pin number are in database
        # Get both account and pin number
        account_number = input_fields[0].get()
        pin_number = input_fields[1].get()

        # Build and format the sql statement
        statement = 'SELECT accountNumber, pinNumber FROM accounts ' \
                    'WHERE BINARY accountNumber = %s ' \
                    'AND BINARY pinNumber = %s'

        # Search through the database if account exists
        self.cursor.execute(statement, (account_number, pin_number))

        # Fetch the results
        results = self.cursor.fetchall()

        # Check if user has not made account
        if not results:
            # Display an error to user
            messagebox.showerror('Error', 'Invalid information or account does not exist')
        else:
            login_frame.destroy()
            self.options = Options(window, account_number, pin_number)

        # Returns
        # TODO: Return none
        return

    def signup_user(self, input_fields):
        """
        ---------------------------------------------
        Checks if account does NOT exist (NOT within
        database). It also makes sures all information
        entered is valid. If these conditions are passed,
        users information is inserted inside database.
        ---------------------------------------------
        Parameter:
            input_fields - All entry fields user has
            entered information inside of in the login
            form. (Array of Entries)
        Returns:
            none
        ---------------------------------------------
        """

        # Calculations
        # TODO: Check if all information is valid, and doesn't exist in database
        # Get all information user entered
        first_name = input_fields[0].get()
        last_name = input_fields[1].get()
        account_number = input_fields[2].get()
        pin_number = input_fields[3].get()

        # Check if both account and pin numbers are valid
        valid_account = self.valid_account_number(account_number)
        valid_pin = self.valid_pin_number(pin_number)

        # If all information entered is valid
        if first_name != "" and last_name != "" and valid_account and valid_pin:
            # Build and format sql statement
            statement = 'SELECT accountNumber, pinNumber FROM accounts ' \
                        'WHERE BINARY accountNumber = %s ' \
                        'OR BINARY pinNumber = %s'

            # Search through database to check if it exists
            self.cursor.execute(statement, (account_number, pin_number))

            # Get the results
            results = self.cursor.fetchall()

            # If account doesn't exist
            if not results:
                # Add new account to database
                statement = "INSERT INTO accounts VALUES (%s, %s, %s, %s, 0)"

                # Query the database
                self.cursor.execute(statement, (first_name, last_name, account_number, pin_number))
                self.database.commit()
            else:
                # Let user know that account already exists
                messagebox.showerror('Error', 'Account already exists!')
        else:
            # Let user know that the information entered is invalid
            messagebox.showerror('Error', 'Invalid information entered!')


    def valid_account_number(self, account_number):
        """
        ---------------------------------------------------
        Used as helper method for signup_user. Checks
        if account number contains 16-digits, and no
        special characters, and letters.
        ---------------------------------------------------
        Parameter:
            account_number - The account number user inputs
            (int)
        Returns:
            isValid - True if account number is valid,
            false otherwise. (boolean)
        ---------------------------------------------------
        """

        # Variables
        # TODO: Initialize variables
        isValid = True

        # Calculations
        # TODO: Checks if account number is valid
        if len(account_number) < 16 or not account_number.isnumeric():
            isValid = False

        # Returns
        # TODO: Return true if valid, false otherwise
        return isValid

    def valid_pin_number(self, pin_number):
        """
        ----------------------------------------------------
        Used as helper method for signup_user. Checks if
        pin number contains 4 to 6 digits, no special
        characters, and letters.
        ----------------------------------------------------
        Parameter:
            pin_number - The PIN number user inputs (int)
        Returns:
            isValid - True if PIN number is valid, False otherwise. (boolean)
        ----------------------------------------------------
        """

        # Variables
        # TODO: Initialize variables
        isValid = True

        # Calculations
        # TODO: Checks if pin number is valid
        if len(pin_number) < 4 or len(pin_number) > 6 or not pin_number.isnumeric():
            isValid = False

        # Returns
        # TODO: Return true if valid, false otherwise
        return isValid
