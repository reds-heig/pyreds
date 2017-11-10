#!/usr/bin/env python
# encoding: utf-8

import readline

import command

class History(command.Module):
    _brief       = "History command support"
    _description = "History command support.\n" \
                   "Depending on its parameter type:\n" \
                   "  - No param: It shows the current history\n" \
                   "  - Param is 'int': Execute command at 'param' index in history\n" \
                   "  - Param is 'int': Search for history input which has 'param' string"

    _input = command.Params(command.Input('param', "param"))

    def __init__(self, globals):
        self.globals = globals
        super(History, self).__init__()

    def _function(self, param=None):

        if param is None:
            self.show()
        elif isinstance(param, str):
            self.search(param)
        elif isinstance(param, int):
            self.execute(param)
        else:
            print "Not support input '%s'" % param

    def show(self):

        historyLength        = readline.get_current_history_length()
        historyLengthDigitNr = len(str(historyLength))

        for idx in range(1, historyLength):
            idxLen = len(str(idx))
            print "%(space)s%(idx)s  '%(historyItem)s'" % {'space'       : ' '*(1+historyLengthDigitNr-idxLen),
                                                           'idx'         : idx,
                                                           'historyItem' : readline.get_history_item(idx)}

    def execute(self, index):

        command = readline.get_history_item(index)
        if command is not None:
            print "executing command: '%s'" % command

            exec(command, self.globals)

            # add the  executed command in the history by replacing maestro.history.execute()
            pos = readline.get_current_history_length() - 1
            readline.replace_history_item(pos, command)
        else:
            print "history: Index '%i' is out of range" % index

    def search(self, searchItem):

        historyLength        = readline.get_current_history_length()
        historyLengthDigitNr = len(str(historyLength))

        for idx in range(1, historyLength):
            historyItem = readline.get_history_item(idx)
            if historyItem.find(searchItem) != -1:
                idxLen = len(str(idx))
                print "%(space)s%(idx)s  '%(historyItem)s'" % {'space'       : ' '*(1+historyLengthDigitNr-idxLen),
                                                               'idx'         : idx,
                                                               'historyItem' : readline.get_history_item(idx)}

