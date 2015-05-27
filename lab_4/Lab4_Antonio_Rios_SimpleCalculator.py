# Antonio rios
# February 26, 2015
# CS 136 Lab
# Lab 4
#================================


from tkinter import *
from compute import * # import your code that you created before


class SimpleCalculator(Frame): # any class name is fine here

    # Constructor
    def __init__(self, root, title, geometry = None):

        ############################ Call super constructor ############################
        Frame.__init__(self, root)

        ############################ Init data attributes ############################
        # remember root widget
        self.root = root
        # create four textvariables for all Entry fields and for the operation button
        self.first_operand    = StringVar()    # textvariable for first operand, attached to first_operand_entry
        self.second_operand   = StringVar()    # textvariable for second operand, attached to second_operand_entry
        self.result           = StringVar()    # textvariable for result field, attached to result_entry
        self.operation        = StringVar()    # textvariable for operation, i.e. attached to operation_button

        ############################ Set general configurations ############################
        self.root.title(title)                 # set title of root widget
        self.root.resizable(0,0)               # set to none resizable
        self.option_add('*Font', 'Verdana 15') # set default font
        self.pack()                            # display our calculator frame in root widget

        ############################ Instantiate widgets ############################
        # buttons
        quit_button          = self.create_quit_button(self)
        operation_button     = self.create_operation_button(self)
        result_button        = self.create_result_button(self)
        # entries
        first_operand_entry  = self.create_first_operand_entry(self)
        second_operand_entry = self.create_second_operand_entry(self)
        result_entry         = self.create_result_entry(self)

        ############################ Position&display widgets with grid layout ############################

        # FILL IN THE DETAILS OF EACH GRID CALL
        operation_button.grid(row=0, column=0, sticky='NEWS')
        result_button.grid(row=1, column=0, sticky='NEWS')
        first_operand_entry.grid(row=0, column=1,sticky='NEWS')
        second_operand_entry.grid(row=1, column=1, sticky='NEWS')
        result_entry.grid(row=2, column=1,sticky='NEWS')
        quit_button.grid(row=3, columnspan=3, sticky='NEWS')


    ############################ Define command callbacks ############################
    def display_result(self):
        try:
            """
            COMPUTE THE RESULT AND SET THE RESULT ENTRY TO THAT RESULT
            THIS INVOLVES MAKING USE OF FUNCTION compute() THAT YOU CREATED BEFORE
            """
            self.result.set(compute(float(self.first_operand.get()), float(self.second_operand.get()), self.operation.get()))
        except ValueError:
            self.result.set('Invalid Input!')

    def advance_operation(self):

        """
        READ THE CURRENT OPERATION FROM THE operation textvariable
        RESET THAT textvariable TO THE OPERATION THAT IS THE SUCCESSOR OPERATION
        RECOMCUTE THE RESULT, I.E. JUST CALL THE FUNCTION THAT DOES THAT FOR YOU
        """
#        self.operation.set('+')
        if (self.operation.get() == '+'):
            self.operation.set('-')
        elif(self.operation.get() == '-'):
            self.operation.set('*')
        elif(self.operation.get() == '*'):
            self.operation.set('/')
        elif(self.operation.get() == '/'):
            self.operation.set('+')

        self.display_result()

    ############################ Helper methods to create widgets ############################

    # FILL IN ALL THE ONE-LINERS THAT CREATE THE DIFFERENT WIDGETS, I.E. WHERE THE ELLIPSES ARE
    def create_quit_button(self, parent):

        quit_button = Button(parent, text='QUIT', command=self.quit_command)
        return quit_button

    def create_operation_button(self, parent):
        self.operation.set('+')
        operation_button = Button(parent, textvariable=self.operation, command=self.advance_operation)
        return operation_button

    def create_result_button(self, parent):
        result_button = Button(parent, text='=', command=self.display_result)
        return result_button

    def create_first_operand_entry(self, parent):
        first_operand_entry = Entry(parent, textvariable=self.first_operand)
        return first_operand_entry

    def create_second_operand_entry(self, parent):
        second_operand_entry = Entry(parent, textvariable=self.second_operand)
        return second_operand_entry

    def create_result_entry(self, parent):
        result_entry = Entry(parent, textvariable=self.result, state='readonly')
        return result_entry

    def quit_command(self):
        self.root.destroy()



############################ main() ############################
def main():
    root = Tk()
    SimpleCalculator(root, "Simple Calculator")
    root.mainloop()


if __name__ == '__main__':
    main()
