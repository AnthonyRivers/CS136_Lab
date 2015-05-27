# Antonio Rios
# March 13, 2015
# CS 136 LAB
# LAB 6: Currency Convert with Intelligent Display Label.
#######################################################


from tkinter import *
from tkinter.ttk import *


from EntryField import FloatEntry, CurrencyEntry


######################################### class FilteringLabel #####################################
class FilteringLabel(Label):
    """
    FilteringLabel takes a text variable (like any Label can do), but shows the value of that variable
    on its labels in a desired format. This is achieved by overriding the trivial implementation of method
    filter_callback() in subclasses
    """
    def __init__(self, root, **options):
        # call super
        super().__init__(root, **options)

        #remember text variable and start tracing
        self.__text_variable = options['textvariable']
        self.__text_variable.trace('w', self.__callback)

        # in case option 'text' is set, we already need to filter it
        if'text' in options:
            self.__text_variable.set(options['text'])

    # this is fired whenever text variable gets altered
    def __callback(self, *args):
        original_text = self.__text_variable.get()

        try:
            filtered_text = self.filter_callback(original_text)
        except Exception as e:
            # here we have an exception because no valid input was passed in
            filtered_text = "INPUT ERROR: '{}'".format(original_text)
            callback_string = str(self.filter_callback)
            name = callback_string.split()

            print("An error occurred in function '{}()] on input '{}':{}".format(name[2], original_text,e), flush=True)

        self.__text_variable.set(filtered_text)

    def filter_callback(self, text):
        """
        To be overriden in subclasses.
        Would fire an exception on invalid input or return some filtered text otherwise
        """
        if isintance(float(text),float):
            return '$' + text
        else:
            raise ValueError

################################ Dollar Label #############################################################
class DollarLabel(FilteringLabel):

    def __init__(self, root, **options):
        super().__init__(root, **options)

    def filter_callback(self, text):

        if text == '':
            return '$' + '0.00'

        if isinstance(float(text), float):

            if '.' in text:
                number = text.split('.')

                if len(number[1]) == 2:
                    return '$' + text

                elif len(number[1]) > 2:
                    decimal = number[1][0:2]
                    return '$' + number[0] + '.' + number[1][0:2]

                elif len(number[1]) == 1:
                    return '$' + text + '0'

                elif len(number[1]) < 2:
                    return '$' + text + '00'
            else:
                return '$' + text + '.00'
        else:
                raise ValueError


############################## POC #######################################################################
def main():
    root = Tk()
    root.title('Subclassing and Polymorphism Demo')

    textLabel = StringVar()

    display = DollarLabel(root, textvariable = textLabel, text = '0.00')

    entryString = StringVar()
    entryString.set('')
    textField = Entry(root, textvariable = entryString)

    showButton = Button(root, text = 'Show', command = lambda tl = textLabel, es = entryString: tl.set(es.get()))

    display.pack()
    textField.pack()
    showButton.pack()

    root.mainloop()

if __name__ == '__main__':
    main()