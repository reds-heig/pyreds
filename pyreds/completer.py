#!/usr/bin/env python
# encoding: utf-8

import re
import readline
    
import command

# == Debub file ================================================================
# import logging

# LOG_FILENAME = 'completer.log'
# logging.basicConfig(filename=LOG_FILENAME,
#                     filemode='w',
#                     level=logging.DEBUG,
#                     )

# == Build the cmd regExp ======================================================
cmdRe   = re.compile(r"^\s*"                     # Initial space characters if any
                     r"(.*\s+)?"                 # initial par of a python cmd (like a 'myVar = ')
                     r"(?P<decodedCmd>\S+)"      # full path of the current cmd
                     r"(?P<cmdExtension>[.\[(])" # latest cmd delimiter
                     r"(?P<endOfCmd>.*)$")       # end of the command

paramRe = re.compile(r"([\"\'])?(\w+)([\"\'])?,")


class  Completer(object):

    def __init__(self, globals):

        self.globals       = globals
        self.matchingWords = []

        # set tab as completer key
        readline.parse_and_bind("tab: complete")
        readline.set_completer_delims(' .,\(\)')
        readline.set_completer(self.complete)

    def complete(self, text, state):

        if state == 0:
            self.matchingWords = []

            origline = readline.get_line_buffer()
            begin    = readline.get_begidx()
            end      = readline.get_endidx()

            m = cmdRe.match(origline)
            if m:
                # Reg Exp matched, a command was found
                cmdName      = m.group("decodedCmd")
                endOfCmd     = m.group("endOfCmd")
                cmdExtension = m.group("cmdExtension")

                if cmdExtension == ".":
                    try:
                        cmdList = eval(cmdName + ".cmdList", self.globals)
                    except:
                        cmdList = []

                    if len(text) == 0:
                        self.matchingWords = cmdList
                    else:
                        self.matchingWords = [w for w in cmdList if w.startswith(text)]

                        if cmdList.count(text) > 0:
                            cmd = eval(cmdName + '.' + text, self.globals)
                            for separator in cmd.cmdSeparator:
                                self.matchingWords.append(text + separator)
                            #remove the current found cmd
                            self.matchingWords.remove(text)
                
                elif cmdExtension == "(":

                    # build the parameters list
                    params    = paramRe.findall(endOfCmd)
                    paramsNb  = len(params)

                    # Get the number of input parameters
                    if eval("hasattr("  + cmdName + ", '_input')", self.globals):                   
                        cmdParamNb = eval("len(" + cmdName + "._input.params)", self.globals)
                    else:
                        cmdParamNb = 0

                    if endOfCmd.find(')') == - 1:

                        if cmdParamNb == 0 :
                            self.matchingWords = [text + ')']
                        else:
                            # Get the list of valid parameters object
                            paramsDict = eval(cmdName + "._input.params[" + str(paramsNb) + "].symbolicVals", self.globals)
                            if paramsDict is None:
                                listOfParamTmp = { '' : ''}
                            else:
                                params = paramsDict.keys()
                                if isinstance(params[0], str):
                                    paramsTmp = ["'%s'" % w for w in params]
                                    params    = paramsTmp
                                else:
                                    paramsTmp = [str(w) for w in params]
                                    params    = paramsTmp

                            if len(text) == 0:
                                self.matchingWords = params
                            elif  params.count(text) >0:
                                if paramsNb == (cmdParamNb-1):
                                    self.matchingWords = [text + ')']
                                else:
                                    self.matchingWords = [text + ', ']
                            else:
                                self.matchingWords = [w for w in params if w.startswith(text)]
            else:
                # Regex did not match
                globalsObjects = self.globals.keys()
                if globalsObjects.count('__builtins__') > 0:
                    globalsObjects.remove('__builtins__')

                if len(text) == 0:
                    self.matchingWords = sorted(globalsObjects)
                else:
                    self.matchingWords = [w for w in globalsObjects if w.startswith(text)]

                    if globalsObjects.count(text) > 0:
                        if isinstance(self.globals[text], command.Command):
                            for separator in self.globals[text].cmdSeparator:
                                self.matchingWords.append(text + separator)
                            #remove the current found cmd
                            self.matchingWords.remove(text)

        try:
            reponse = self.matchingWords[state]
        except IndexError:
            reponse = None

        return reponse
# =============================================================================