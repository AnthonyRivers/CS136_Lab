# Antonio Rios
# March 7, 2015
# CS 136 LAB
# LAB 5: Currency Converter
###################################################3


from tkinter import *
from tkinter.ttk import *

####################### Class Currency Converter ############################
class CurrencyConverter(Frame):

    # Constructor
    def __init__(self, root, **options):
        """
        Call the super constructor. Instead of explicitly mentioning
        the class, you can get the superclass object by 'super()'
        then you call '.__init__() on it without passing self!

        :param root: an instance of Tk() root widget
        :param options: Tkinter GUI configuration options
        :return: returns nothing
        """
        super().__init__(root)
        ################## Set general configurations #######################
        self.root = root

        if 'title' in options:
            self.root.title(options['title'])
        if 'geometry' in options:
            self.root.geometry(options['geometry'])

        self.root.resizable(0,0)
        self.option_add('*Font', 'Verdana 12')
        self.grid(column=0, row=0, sticky='nesw')

        ################# Init data attributes ##############################
        # Keeps track of the ammounts
        self.euros = StringVar()
        self.dollars = StringVar()
        self.pesos = StringVar()
        self.rupees = StringVar()
        self.yen = StringVar()

        # if 'rate' in options:
        #     self.rate = options['rate']
        # else:
        #     print('No exchange rate provided')
        if 'rates' in options:
            self.rates = options['rates']


        ##################### Instantiate widgets ###########################
        dollars_text_label     = Label(self, text='Dollars')
        dollars_amount_entry   = Entry(self, textvariable=self.dollars, justify = RIGHT)
        euros_text_label   = Label(self, text='Euros')
        euros_amount_label = Label(self, textvariable=self.euros, anchor='e')
        pesos_text_label   = Label(self, text='Pesos')
        pesos_amount_label = Label(self, textvariable=self.pesos, anchor='e')
        rupees_text_label   = Label(self, text='Rupees')
        rupees_amount_label = Label(self, textvariable=self.rupees, anchor='e')
        yen_text_label   = Label(self, text='Yen')
        yen_amount_label = Label(self, textvariable=self.yen, anchor='e')

        convert_button        = Button(self, text='Convert', command=self.convert)
        quit_button          = Button(self, text='Quit', command=self.quit_command)

        ################### Position & Display widgets #######################
        dollars_text_label.grid(row=0, column=0, sticky='w')
        dollars_amount_entry.grid(row=0, column=1)
        euros_text_label.grid(row=1, column=0, sticky='w')
        euros_amount_label.grid(row=1, column=1, sticky='e')
        pesos_text_label.grid(row=2, column=0, sticky='w')
        pesos_amount_label.grid(row=2, column=1, sticky='e')
        rupees_text_label.grid(row=3, column=0, sticky='w')
        rupees_amount_label.grid(row=3, column=1, sticky='e')
        yen_text_label.grid(row=4, column=0, sticky='w')
        yen_amount_label.grid(row=4, column=1, sticky='e')

        convert_button.grid(row=5, columnspan=2, sticky='news')
        quit_button.grid(row=6, columnspan=2, sticky='news')


    def convert(self):
        """
        The convert method reads the Euros value and coverts
        it to USA dollars. Displays the dollar amount on the
        dollar label. Using the currency exchange rate passed in
        the constructor the amount is calculated.
        :return: returns nothing
        """
        euros_amount = float(self.dollars.get()) * float(self.rates[0])
        self.euros.set(str(euros_amount))

        pesos_amount = float(self.dollars.get()) * float(self.rates[1])
        self.pesos.set(str(pesos_amount))

        rupees_amount = float(self.dollars.get()) * float(self.rates[2])
        self.rupees.set(str(rupees_amount))

        yen_amount = float(self.dollars.get()) * float(self.rates[3])
        self.yen.set(str(yen_amount))

    def quit_command(self):
        self.root.destroy()

########################### main() ###########################################
def main():
    root = Tk()
    CurrencyConverter(root, title = "Currency Converter", rates = [0.92, 15.5, 62.78, 120.83])
    root.mainloop()


if __name__ == '__main__':
    main()