# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

# solution

class bank:
    bank_name = "The Bank of Habib"
    def __init__(self,name):
        self.name = name

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def __str__(self):
        return f"Bank Name: {self.bank_name}, & Account Holder : Mr/Ms {self.name}"
        

s1 = bank("Hasnain")
print(s1)  #before changing the bank name
s1.change_bank_name("Bank Al-Falah")
s2 = bank("Ahmed")
s2.change_bank_name("Bank Al-Habib")
print(s2)  #after changing the bank name 
s3 = bank("Sara")
print(s3)  #after changing the bank name
