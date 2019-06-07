# This is the main file that runs my frequency analysis app
# It's a command line app that performs frequency analysis on 
# on an encrypted file. It will start with xor encryption, with
# other ciphers being added maybe.

from prin import prin
from read import read
from apply_key import apply_key
from set_enc import set_enc
from frequency import frequency
import sys

class InputError(Exception):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class Instance():
    def __init__(self):
        self.original_text = None
        self.current_text = None
    
    def set_original_txt(self, string):
        self.original_text = string
        self.current_text = string
    
    def set_current_txt(self, string):
        self.current_text = string


class ArgumentParser():

    def __init__(self):
        self.instance = Instance()
        self.args = None
    
    def get_args(self, inp):
        self.args = inp



    def run_cmd(self):
        possible_commands = ['read', 'frequency', 'set', 'apply_key', 'reset', 'quit', 'print']
        help_message = "This is where a help message will go"
        try:
            cmd = possible_commands.index(self.args[0])
            if cmd == 0:
                #instance.set_original_text(read(self.args[1:]))
                return read(self.args[1:])
            elif cmd == 1:
                return frequency(self.args[1:])
            elif cmd == 2:
                # instance.set_current_text(set_enc(args[1:]))
                return set_enc(self.args[1:])
            elif cmd == 3:
                # instance.set_current_text(apply_key(args[1:]))
                return apply_key(self.args[1:])
            elif cmd == 4:
                # instance.set_current_text(instance.original_text)
                return "running reset"
            elif cmd == 5:
                sys.exit(0)
            elif cmd == 6:
                return "running print"
        except ValueError:
            raise InputError("invalid input: ", self.args)



parser = ArgumentParser()

#while True:
#    inp = input()
#    parser.get_args(inp.split(" "))
#    parser.run_cmd()