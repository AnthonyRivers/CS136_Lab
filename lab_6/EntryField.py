# Antonio Rios
# March 13, 2015
# CS 136 LAB
# LAB 6: Currency Convert with Intelligent Entry Field.
#######################################################


from tkinter import *
from tkinter.ttk import *

################################### Class ValidationException ##############################################
class ValidationException(Exception):
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

################################ Class ValidatingEntry ########################################################
class ValidatingEntry(Entry):
    """
    ValidatingEntry is a generic class that provides validating services.
    """
    def __init__(self, root, **options):
        # init super
        super().__init__(root, **options)

        # __text contains always the last valid entry, before the text variable got changed
        # set it to '', in case the validation of the initial text fails
        self.__text = ''
        self.__text_variable = options['textvariable']
        self.__text_variable.trace("w", self.__callback)

        # text variable
        if 'text' in options:
            self.__text_variable.set(options['text'])

        self.config(textvariable=self.__text_variable)

    def __callback(self, *discard):
        """
        Helper method that is the standard callback for text variable tracing,
        which calls the validation function internally and only applies changes
        if validation does not fail.
        """
        # get the newly entered text from the textvariable
        new_text = self.__text_variable.get()

        # pass the new_text as an argument to
        # the validate_callback() method to make
        # sure that new_text is a valid value. If
        # it's a valid value then it will be store
        # in the instance variable self.__text
        if self.validate_callback(new_text):
            # only set __text to the new text, when validation is fine
            self.__text = new_text

        self.__text_variable.set(self.__text)

    def validate_callback(self, text):
        """
        Override this method in subclasses. Returns False if validation fails, True otherwise.
        """
        # just return True in this trivial implemenation
        return True

################################ Class IntegerEntry ########################################################
class IntegerEntry(ValidatingEntry):
    """
    Entry that only accepts integers
    """
    def __init__(self, root, **options):
        super().__init__(root, **options)

    def validate_callback(self, text):
        try:
            if text:
                int(text)
            return True
        except ValueError:
            return False


################################### Class FloatEntry ########################################################
class FloatEntry(ValidatingEntry):
    """
    Entry that only accepts floating point numbers
    """
    def __init__(self, root, **options):
        super().__init__(root, **options)

    def validate_callback(self, text):
        try:
            if text:
                float(text)
            return True
        except ValueError:
            return False


################################## Class CurrencyEntry #########################################################
class CurrencyEntry(FloatEntry):
    '''
        The CurrencyEntry class subclasses the FloatEntry class.
        It overrides teh validate_callback() method from the superclass


    '''
    def __init__(self, root, **options):
        super().__init__(root, **options)

    def validate_callback(self, text):
        ''' The validate_callback method is an override method from
        the super class FloatEntry. The method validates that
        the string entered represents a number and that it has only up
        to two decimal positions after the decimal point.
        '''

        if not super().validate_callback(text):
            return False

        if '.' in text:
            fractional_amount = text.split('.')

            if(len(fractional_amount[1]) > 2):
                return False

        return True


########################################## main() ####################################################
def main():
    root = Tk()
    root.title('Subclassing and Polymorphism Demo')
    root.geometry('300x300')

    currency_value = StringVar()
    entry = CurrencyEntry(root, text='123.00', textvariable=currency_value)
    entry.pack()

    root.mainloop()

if __name__ == '__main__':
    main()