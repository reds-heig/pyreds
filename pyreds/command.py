#!/usr/bin/env python
# encoding: utf-8


class Command(object):

    def __init__(self):

        # Default class variable used for the help command
        self._brief       = "== No brief available for ths command =="
        self._description = "== No description available for this command =="

        # Support command separators for the current cmd
        if not hasattr(self, 'cmdSeparator'):
            self.cmdSeparator = []

        if not hasattr(self, 'cmdList'):
            self.cmdList = []

        # Creation of the cmdList for each components
        for obj in dir(self):

            if isinstance(getattr(self, obj), Command):
                self.cmdList.append(obj)

                # Adding the '.' command separator
                if self.cmdSeparator.count('.') == 0:
                    self.cmdSeparator.append('.')

            # Adding the '(' command separator
            if (obj == '_function'):
                if self.cmdSeparator.count('(') == 0:
                    self.cmdSeparator.append('(')

    def __call__(self, *paramsTuple):

        extractedParams = self.extractParams(paramsTuple)
        # Execute the command
        rc = self._function(*extractedParams)

        return rc

    def extractParams(self, paramsTuple):
        extractedParams = []

        # loop through the input parameter list
        for idx in range(len(paramsTuple)):
            if self._input.params[idx].symbolicVals is not None:
                extractedParams.append(self._input.params[idx].symbolicVals[paramsTuple[idx]])
            else:
                extractedParams.append(paramsTuple[idx])

        return extractedParams


class Module(Command):

    def __init__(self):
        super(Module, self).__init__();


class Params(object):

    def __init__(self, *params):
        # Creation of list of parameters
        self.params = params

        # Creation of dictionary of parameters
        self.paramsByName = {}
        for param in params:
            self.paramsByName[param.name] = param

    def __getitem__(self, idx):
        return self.params[idx]


class Input(object):

    def __init__(self, name, description, symbolicVals=None):
        self.name         = name
        self.description  = description
        self.symbolicVals = symbolicVals


