Implement a class MoneyBox to work with a virtual piggy bank.

Each piggy bank has a limited capacity, which is expressed as an integer - the number of coins that can be put into the piggy bank. The class should maintain information about the number of coins in the piggy bank, provide the ability to put coins into the piggy bank and find out whether it is possible to add some more coins to the piggy bank, not exceeding its capacity.

The class should look like this:
class MoneyBox:
    def __init__(self, capacity):
        # constructor with an argument - capacity of a piggy bank

    def can_add(self, v):
        # True, if it is possible to add v coins, False instead

    def add(self, v):
        # put v coins in a piggy bank

When the piggy bank is created, the number of coins in it is 0.
Note:
The add(self, v) method is guaranteed to be called only if can_add(self, v) – True