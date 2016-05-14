#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

import sys
import os
import readline



class autocomplete(object):
    def __init__(self, options):
        self.options = sorted(options)
        return

    def complete(self, text, state):
        response = None
        if state == 0:
            if text:
                self.matches = [s 
                    for s in self.options
                    if s and s.startswith(text)
                ]
            else:
                self.matches = self.options[:]

        try:
            response = self.matches[state]
        except IndexError:
            response = None
        return response



#Control 1 = Shellsploit
#Control 2 = control.py
def start( control=1):
    if control == 1:
        from .db import ret2
        readline.set_completer(autocomplete(ret2()).complete)
        readline.parse_and_bind('tab: complete')
    else:
        from .db import ret
        readline.set_completer(autocomplete(ret()).complete)
        readline.parse_and_bind('tab: complete')


