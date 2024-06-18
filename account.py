""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: account.py
# Description: Contains the base Account class and derived classes.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Acc():
    def __init__(self, name, acc_number, balance):
        self.set_name(name)
        self.set_acc_number(acc_number)
        self.set_balance(balance)
    
    
    def get_name(self):
        return self._name

         
    def set_name(self, name):
        if name == "":
            raise ValueError("name the name")
        self._name = name

    
    def get_acc_number(self):
        return self._acc_number
    
    def set_acc_number(self, acc_number):
        if isinstance(acc_number,(int,float)) and acc_number >= 0:
            self._acc_number = acc_number
        else:
            raise ValueError("account number can not be negative")
        
        
    def get_balance(self):
        return self._balance
        
    def set_balance(self, balance):
        if isinstance(balance,(int,float)):
            self._balance = balance
            
    def deposit(self, balance, dep_amm):
        if dep_amm <= 0:            
            raise ValueError("balance in the negative")
        self._dep_amm += self._balance
    
    def withdraw(self, balance, with_amm):
        if with_amm <= 0:
            raise ValueError("cannot with draw nothing or negative numbers")
        else:
            self._with_amm -= self._balance
            print (f"withdrew {with_amm} successfully")
        

             
