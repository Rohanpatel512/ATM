"""
---------------------------------------------------
Represents the actions users can do such as
withdraw, deposit, and check balance. Also gets
all the users information from database once
initialized
---------------------------------------------------
Author: Rohan Patel
_updated_= "2022-07-26"
---------------------------------------------------
"""

# Imports
import mysql.connector
from math import floor
from tkinter import messagebox
from dotenv import load_dotenv
import os

class User:

    def __init__(self, account_number, pin_number):
        """
        ---------------------------------------------
        Initializes the user and gets balance,
        account number, pin number, first name,
        and last name
        ---------------------------------------------
        Returns:
            none
        ---------------------------------------------
        """
        load_dotenv()
        # Initializes variables
        self.account_number = account_number
        self.pin_number = pin_number
        self.balance = 0
        self.database = mysql.connector.connect(host=os.getenv("HOST"), user=os.getenv("USER"), passwd=os.getenv("PASSWORD"),
             database=os.getenv("DATABASE"), auth_plugin=os.getenv("AUTH_PLUGIN"))
        self.cursor = self.database.cursor(buffered=True)

        self.set_balance()

    def deposit(self, deposit_amount):
        """
        --------------------------------------------------
        Gets the amount to add to total balance from user
        then adds to the balance. Saves this onto database
        --------------------------------------------------
        Parameters:
            deposit_amount - The total amount to be deposited
            into users account
        Returns:
            none
        ---------------------------------------------------
        """

        # Calculations
        # TODO: Add amount to users balance, then update changes in database.
        # Add the value of deposit amount to balance
        self.balance += float(deposit_amount)

        # Build the sql statement
        statement = 'UPDATE accounts '\
                    'SET balance = %s '\
                    'WHERE BINARY accountNumber = %s AND BINARY pinNumber = %s'

        # Execute the query
        self.cursor.execute(statement, (str(self.balance), self.account_number, self.pin_number))
        self.database.commit()

        # Returns
        # TODO: Return none
        return

    def withdraw(self, withdraw_amount):
        """
        ---------------------------------------------------
        Removes the amount user inputs from balance. If the
        amount to remove is greater than total balance, an
        error will be displayed. Saves remaining amount to
        database
        ---------------------------------------------------
        Parameters:
            withdraw_amount - Amount user will remove from
            current balance (float)
        Returns:
            none
        ---------------------------------------------------
        """
        # Calculations
        # TODO: Remove amount from total balance, update the database
        # If the amount to withdraw is less than current balance
        if float(withdraw_amount) <= self.balance:
            # Remove the amount and round to 2 decimal places
            self.balance = round(self.balance - float(withdraw_amount), 2)

            # Build the sql statement
            statement = 'UPDATE accounts '\
                        'SET balance = %s '\
                        'WHERE BINARY accountNumber = %s AND BINARY pinNumber = %s'

            # Execute the query
            self.cursor.execute(statement, (str(self.balance), self.account_number, self.pin_number))
            self.database.commit()
        else:
            # Display an error message
            messagebox.showerror("Error", "Value entered shouldn't be greater than total balance.")

        # Returns
        # TODO: Return none
        return

    def set_balance(self):
        """
        ---------------------------------------------------
        USED ONLY AS HELPER METHOD WHEN OBJECT IS CREATED.
        Gets the users total balance from the database
        ---------------------------------------------------
        Returns:
            none
        ---------------------------------------------------
        """

        # Calculations
        # TODO: Gets the users total balance from database using the account number and pin number
        # Creates a sql statement
        statement = 'SELECT balance FROM accounts WHERE BINARY accountNumber = %s ' \
                    'AND BINARY pinNumber = %s'

        # Execute the query
        self.cursor.execute(statement, (self.account_number, self.pin_number))

        # Fetch the results
        result = self.cursor.fetchall()

        # Get the balance from results array
        self.balance = float(result[0][0])

        # Returns
        # TODO: Return none
        return

    def get_balance(self):
        """
        --------------------------------------------------------
        Returns users current balance. Allows outside classes
        access to balance
        --------------------------------------------------------
        Returns:
            balance - The users total balance (float)
        --------------------------------------------------------
        """
        # Returns
        # TODO: Return the balance
        return self.balance