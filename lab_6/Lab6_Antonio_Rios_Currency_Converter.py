# Antonio Rios
# March 23, 2015
# CS 136 LAB
# LAB 6: Modified Currency Converter to use
# the DollarLabel and CurrencyEntry created in lab 6
#######################################################


from tkinter import *
from tkinter.ttk import *
from DisplayLabel import DollarLabel
from EntryField import CurrencyEntry


####################### Class Currency Converter ############################
class CurrencyConverter(Frame):
    '''
        The CurrencyConverter class subclasses the Frame class,
        and contains two methods the convert() method which does
        the actual currency conversion operation and the destroy()
        method which is called by the Quit button to close the
        application.
    '''
    # Constructor
    def __init__(self, root, **options):
        """
        The constructor for the CurrencyConverter program
        set's the general configuration for title and window size
        if passed in to the constructor.

        Initializes the instance variables to store
        the amount value for euros and dollars.

        The constructor instantiates the widgets, positions and
        displays the widgets.


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
        #EurosEntry_textvar = StringVar()
        #DollarLabel_textvar = StringVar()

        # Keeps track of the amounts
        self.euros = StringVar()
        self.dollars = StringVar()


        # if 'rate' in options:
        #     self.rate = options['rate']
        # else:
        #     print('No exchange rate provided')
        if 'rate' in options:
            self.rate = options['rate']

        ##################### Instantiate widgets ###########################
        euros_text_label     = Label(self, text='Euros')
        euros_amount_entry   = CurrencyEntry(self, textvariable=self.euros, justify = RIGHT, text='0.00')
        dollars_text_label   = Label(self, text='Dollars')
        dollars_amount_label = DollarLabel(self, textvariable=self.dollars, anchor='e', text = '0.00')
        convert_button        = Button(self, text='Convert', command=self.convert)
        quit_button          = Button(self, text='Quit', command=self.quit_command)

        ################### Position & Display widgets #######################
        euros_text_label.grid(row=0, column=0, sticky='w')
        euros_amount_entry.grid(row=0, column=1)
        dollars_text_label.grid(row=1, column=0, sticky='w')
        dollars_amount_label.grid(row=1, column=1, sticky='e')
        convert_button.grid(row=2, columnspan=2, sticky='news')
        quit_button.grid(row=3, columnspan=2, sticky='news')


    def convert(self):
        """
        The convert method reads the Euros value and coverts
        it to USA dollars. Displays the dollar amount on the
        dollar label. Using the currency exchange rate passed in
        the constructor the amount is calculated.
        :return: returns nothing
        """
        # The amounts of euros and dollars are casted to a float type
        # because self.euros is a string type.
        converted_amount = float(self.euros.get()) * float(self.rate)
        self.dollars.set(str(converted_amount))


    def quit_command(self):
        """
        The quit_command method is called when
        the Quit button is clicked. The method
        calls the root's destroy method and closes
        the window.

        :return: returns nothing.
        """
        self.root.destroy()

########################### main() ###########################################
def main():
    root = Tk()
    CurrencyConverter(root, title="Currency Converter", rate=1.117)
    root.mainloop()


if __name__ == '__main__':
    main()
