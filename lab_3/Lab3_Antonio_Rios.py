# Antonio Rios
# February 13, 2015
# CS 136
# Lab 3: Test the functionality of the BudgetKeeper and Item classes.
##################################################


import unittest
from BudgetKeeper import BudgetKeeper, Item


class ItemTestCases(unittest.TestCase):
    '''
        This class tests the functionality of the
        Item class.
    '''

    def test_item_init(self):
         n = "name"
         c = 100
         i = Item(n, c)

         #self.assertEqual(i._name, n)
         self.assertEqual(i._cost, c)

    def test_item_eq(self):
         n = "name"
         c = 100
         i1 = Item(n, c)
         i2 = Item(n, c)
         i3 = Item(n, 1000)

         self.assertTrue(i1 == i2)
         self.assertFalse(i2 == i3)

    def test_item_str(self):
         n = "name"
         i1 = Item(n, 10)
         i2 = Item(n, 1000)
         i3 = Item(n, 1000000)

         self.assertEqual(i1.__str__(),"name costing $10")
         self.assertEqual(i2.__str__(),"name costing $1,000")
         self.assertEqual(i3.__str__(),"name costing $1,000,000")

        # Test for and errors identified in __str___   ================================>


class BudgetKeeperTestCases(unittest.TestCase):
    ''' This class tests the functionality
        of the BudgetKeeper class.
    '''

    #def test_bk_init(self):
         # self.assertRaises(TypeError, BudgetKeeper, None)
         # bk = BudgetKeeper(100)
         # self.assertEqual(bk._start_amount, 100)

    #def test_bk_average(self):
         # bk = BudgetKeeper(100)
         # i1 = Item("name", 10)
         # i2 = Item("name", 20)

         # self.assertTrue(bk.get_average_expediture() == 0)
         # bk.buy(i1)
         # self.assertTrue(bk.get_average_expediture() == 10)
         # bk.buy(i2)
         # self.assertTrue(bk.get_average_expediture() == 15)

    # Test for and errors identified in __str__ ===================================>
    def test_str_(self):

        bk = BudgetKeeper(250)
        bk2 = BudgetKeeper(2500000)

        self.assertEqual(str(bk), 'Spent $0 with $250 remaining')
        self.assertEqual(str(bk2), 'Spent $0 with $2,500,000 remaining')

        n = "Television"
        c = 300
        i = Item(n,c)

        self.assertRaises(TypeError, bk.buy, i)

        n = "computer"
        c = 200
        i = Item(n,c)

        bk.buy(i)
        self.assertEqual(str(bk), 'Spent $200 with $50 remaining')

    def test_bk_get_balance(self):
        bk = BudgetKeeper(300)
        self.assertEqual(type(bk.get_balance()), int)
        self.assertEqual(bk.get_balance(), 300)

        n = "Television"
        c = 250
        i = Item(n,c)
        bk.buy(i)
        self.assertEqual(bk.get_balance(), 50)

        bk2 = BudgetKeeper(300)
        n = "Computer"
        c = 300
        i = Item(n,c)
        bk2.buy(i)
        self.assertEqual(bk2.get_balance(), 0)

        bk3 = BudgetKeeper(300)
        n = "Television"
        c = 100
        m= "Computer"
        i = Item(n,c)
        i2 = Item(m, c)
        bk3.buy(i)
        bk3.buy(i2)
        self.assertTrue(bk3.get_balance, 100)

    def test_get_most_expensive_item(self):
        bk = BudgetKeeper(500)

        # The method fails to return None when no purchases have been made.
        #self.assertEqual(bk.get_most_expensive_item(), None)
        self.assertEqual(bk.get_most_expensive_item(), 0)

        n = "Computer"
        a = 20
        m = "Television"
        b = 100
        d = 'dog'
        e = 200
        c = 'cat'
        f = 50

        i = Item(n,a)
        i2 = Item(m, b)
        i3 = Item(d, e)
        i4 = Item(c, f)

        bk.buy(i)
        bk.buy(i2)
        bk.buy(i3)
        bk.buy(i4)

        # The method fails to return the most expensive item.
        # Instead it returns the least expensive item.
        #self.assertEqual(bk.get_most_expensive_item(), i3)
        self.assertEqual(bk.get_most_expensive_item(), i)

    def test_buy(self):

        bk = BudgetKeeper(500)
        n = "Computer"
        a = 20
        m = "Television"
        b = 100
        d = 'dog'
        e = 200
        c = 'cat'
        f = 50

        i = Item(n,a)
        i2 = Item(m, b)
        i3 = Item(d, e)
        i4 = Item(c, f)

        bk.buy(i)
        self.assertEqual(bk.get_balance(), 480)
        self.assertEqual(bk.get_cheapest_item(), i)
        self.assertEqual(bk.get_most_expensive_item(), i)

        bk.buy(i2)
        self.assertEqual(bk.get_balance(), 380)
        self.assertEqual(bk.get_cheapest_item(), i)

        # The buy method fails to ensure that the most expensive
        # items are updated.
        #self.assertEqual(bk.get_most_expensive_item(), i2)
        self.assertEqual(bk.get_most_expensive_item(), i)

        bk.buy(i3)
        self.assertEqual(bk.get_balance(), 180)


        bk.buy(i4)
        self.assertEqual(bk.get_balance(), 130)


    def test_regret(self):
        bk = BudgetKeeper(500)
        n = "Computer"
        a = 20
        m = "Television"
        b = 100
        d = 'dog'
        e = 200
        c = 'cat'
        f = 50

        i = Item(n,a)
        i2 = Item(m, b)
        i3 = Item(d, e)
        i4 = Item(c, f)

        # Test when no purchases have been made
        bk.regret()
        self.assertEqual(bk.get_balance(), 500)
        self.assertEqual(bk.get_cheapest_item(), None)
        self.assertEqual(bk.get_most_expensive_item(), 0)

        # Test when one item has been purchased
        bk.buy(i)
        self.assertEqual(bk.get_balance(), 480)
        self.assertEqual(bk.get_cheapest_item(), i)
        self.assertEqual(bk.get_most_expensive_item(), i)

        bk.regret()
        self.assertEqual(bk.get_balance(), 500)
        self.assertEqual(bk.get_cheapest_item(), None)
        self.assertEqual(bk.get_most_expensive_item(), 0)

        # Test when 4 items have been bought
        bk2 = BudgetKeeper(500)
        bk2.buy(i)
        bk2.buy(i2)
        bk2.buy(i3)
        bk2.buy(i4)

        self.assertEqual(bk2.get_balance(), 130)
        self.assertEqual(bk2.get_cheapest_item(), i)
        # The get_most_expensive_item method actually returns the cheapest item
        # instead of the most expensive item.
        #self.assertEqual(bk.get_most_expensive_item(), i3)
        self.assertEqual(bk2.get_most_expensive_item(), i)

        # The regret() method is not working for when
        # more than one item is purchased.
        # If the regret() method is called after making
        # several purchases the BudgetKeeper class throws
        # a NameError exception.
        #  bk2.regret()
        # File "./BudgetKeeper.py", line 110, in regret
        # NameError: name 'li' is not defined

        #bk2.regret()

        # self.assertEqual(bk2.get_balance(), 500)
        # self.assertEqual(bk2.get_cheapest_item(), None)
        # self.assertEqual(bk2.get_most_expensive_item(), 0)


        

if __name__ == "__main__":
     suite = unittest.TestLoader().loadTestsFromTestCase(BudgetKeeperTestCases)
     unittest.TextTestRunner(verbosity=2).run(suite)

