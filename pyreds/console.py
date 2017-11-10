#!/usr/bin/env python
# encoding: utf-8

# == System libs ==============================================================
import code
import atexit
import sys
import readline
import os
import argparse

import command
import completer
import history


class Environment(object):
    globals = {}


class InteractiveConsole(code.InteractiveConsole):

    STARTUP_MESSAGE = 'nice Startup message'
    PROMPT          = '(reds)>> '
    HISTORY_FILE    = os.path.join(os.path.expanduser("~"), ".redsHistory")

    def __init__(self,
                 locals      = Environment.globals,
                 filename    = "<console>",
                 historyFile = HISTORY_FILE):

        code.InteractiveConsole.__init__(self, locals, filename)
        completer.Completer(locals)

        self.historyInitialisation(historyFile)

        self.addModule(history.History, locals)

    def historyInitialisation(self, historyFile):

        if hasattr(readline, "read_history_file"):
            try:
                readline.read_history_file(historyFile)
            except IOError:
                pass
            atexit.register(self.historySave, historyFile)

    def historySave(self, historyFile):
        readline.write_history_file(historyFile)

    def addModule(self, module, *params):

        if issubclass(module, command.Module):

            className  = module.__name__
            moduleName = className[0].lower() + className[1:]

            Environment.globals.update({moduleName: module(*params)})

    # def reloadModule(self, module):
    # def removeModule(self, module):
        # del module...

    def start(self):
        sys.ps1 = self.PROMPT
        self.interact(self.STARTUP_MESSAGE)
