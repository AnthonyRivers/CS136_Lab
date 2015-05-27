# Antonio Rios
# March 25, 2015
# CS136 Lab
# Lab 7: Fancy Calculator
###############################################3


from tkinter import *
from functools import partial as command


class FancyCalculator(Frame):

    # constructor
    def __init__(self, root, **options):

        self.root = root

        if 'title' in options:
            self.root.title(options['title'])
        if 'geometry' in options:
            self.root.geometry(options['geometry'])
        # add the font and size
        self.root.option_add('Font', 'Arial 20')
        # make our string variable and set it blank
        self.display_text = StringVar()
        self.display_text.set("")

        ##################### widget configuration #######################################################
        config = {'width': 5, 'height':2, 'foreground':'black', 'borderwidth':1, 'relief':GROOVE}

        ######################## create super frames #####################################################
        calculator_frame = Frame(root)
        calculator_frame.pack(expand= YES, fill= BOTH)
        display = Label(calculator_frame, text="", textvariable = self.display_text, \
                                              anchor = 'e', padx = 10, font = "Arial 15",
                                              bg = "#202020", fg = 'white', height=2)
        keypad_frame = Frame(calculator_frame)

        ######################### keypad frames ##########################################################
        upper_frame = Frame(keypad_frame)

        for label_text in ['(', ')', '.']:
            label = Label(upper_frame, text = label_text, background='#DBDBDB', **config)

            # added the label bind
            label.bind('<Button-1>', self.add_character(label_text))

            label.pack(side=LEFT, expand=YES, fill=BOTH)

        middle_frame = Frame(keypad_frame)

        for numbers in ["123", "456", "789"]:
            row_frame = Frame(middle_frame)

            for number in numbers:
                label = Label(row_frame, text = number, background='#A7C0C0', **config)

                # added label bind, makes it so we can add the numbers in the display
                label.bind('<Button-1>', self.add_character(number))

                label.pack(side=LEFT, expand=YES, fill=BOTH)
            row_frame.pack(side=TOP, expand=YES, fill=BOTH)

        lower_frame = Frame(keypad_frame)

        for label_text in ['0', 'ca', 'ce']:
            label = Label(lower_frame, text=label_text, background='#DBDBDB', **config)

            if label_text == 'ca':

               #added label bind, makes the display blank
                label.bind('<Button-1>', self.clear_display())
            elif label_text == 'ce':

                # added label bind, makes it delete the last character added
                label.bind('<Button-1>', self.delete_last_entry())

            else:
                """
                Create a binding of the mouse-clicked event to this label.
                Use a functor to let the label "know" that the function add_character() needs
                to be called when the label is clicked, as well as about its reading, i.e. '0'.

                label.bind(...event id goes here...,... functor goes here...)

                """
                # added label bind, makes it add 0
                label.bind('<Button-1>', self.add_character(label_text))

                label.config(background='#A7C0C0')
            label.pack(side=LEFT, expand=YES, fill=BOTH)

        right_frame = Frame(keypad_frame)

        for operation in ['/', '*', '-', '+', '=']:
            label = Label(right_frame, text=operation, background='#FF0066', **config)
            label.pack(side=TOP, expand=YES, fill=BOTH)

            if operation == '=':

                # added label bind, makes it calculate the equation
                label.bind('<Button-1>', self.calculate())


            else:
                """
                Create a binding of the mouse-clicked event to each operation label.
                Use a functor to let each label "know" that function add_operation() needs
                to be called when the label is clicked, as well as about its operation.

                label.bind(...event id goes here...,...functor here)

                """
                # added label bind, makes it add the operator in the displays
                label.bind('<Button-1>', self.add_operation(operation))
######################################## resizing config ###############################################################
        for i in range(5):
            keypad_frame.rowconfigure(i, weight =1)
        for i in range(4):
            keypad_frame.columnconfigure(i, weight=1)

        calculator_frame.rowconfigure(0,weight=1)
        calculator_frame.rowconfigure(1, weight=1)
        calculator_frame.columnconfigure(0, weight=1)

################################ positioning/displaying ################################################################
        upper_frame.grid(row=0, column=0, columnspan=3, sticky='nsew')
        middle_frame.grid(row=1, column=0, columnspan=3,rowspan=3, sticky='nsew')
        lower_frame.grid(row=4, column=0, columnspan=3, sticky='nsew')
        right_frame.grid(row=0, column=3, rowspan=5, sticky='nsew')

        display.grid(row=0, column=0, columnspan=4, sticky='nsew')
        keypad_frame.grid(row=1, column=0, columnspan=4,rowspan=4, sticky='nsew')

############################### callbacks ############################################################

    # add a character, e.g. numbers, parantheses, etc. to the display label
    def add_character(self, text):

        def _add_character(event):

            self.display_text.set(self.display_text.get() + text)



        return _add_character


    # adds an operation, i.e. one of +-*/, to the display label
    def add_operation(self, operation):

        def _add_operation(event):

            self.display_text.set(self.display_text.get() + " " + operation + " ")

        return _add_operation

    # clears the display
    def clear_display(self):

        def _clear_display(event):
            self.display_text.set('')

        return _clear_display

    # deletes that last entry in the display
    def delete_last_entry(self):
        """
        This will delete the last character, except for operations
        which need to be deleted along with their sandwiching spaces!

        your code goes here
        """
        def _delete_last_entry(event):
            display = self.display_text.get()

            if display[-1]== ' ':
                self.display_text.set(display[:(len(display)-3)])
            else:
                self.display_text.set(display[:(len(display)-1)])

        return _delete_last_entry




################################## application logic - calculates result ###############################################

    # calculates the result
    def calculate(self):
        """
        IMPORTANT: make sure that if an exception occurs,
        you display the text ERROR on the display

        Otherwise, this code is surprisingly easy, you just need to apply the function
        eval() to the string:

        your code goes here
        """


        def _calculate(event):
            try:
                display = eval(self.display_text.get())
                self.display_text.set(display)
            except ZeroDivisionError as zerodivision:
                self.display_text.set("Undefined")
            except:
                self.display_text.set("ERROR")

        return _calculate

def main():
    root = Tk()
    FancyCalculator(root, title="Calculator")
    root.mainloop()

if __name__=='__main__':
    main()
