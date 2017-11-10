#!/usr/bin/env python
# encoding: utf-8

redstools
	--> interpreter --> InteractiveConsole

# End-user import of a ReDS Python interpreter 
from redstools import interpreter

cli = interpreter.InteractiveConsole()

cli.addModule(module)	

cli.interact()

# =========================================


import code
import readline


# module.cmd0.cmd1.func(param0, param1)

_function

_inputs
_outputs

CliCommand

CliModule

def completer(text, state):
	if state == 0:


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Interpreter
CommandLineInterface (cli)
Shell
Console

class (RedsCommand)
class (RedsModule)

_function

_indexedCmd

_inputs
(_outputs) <-- not sure it is needed

_brief
_description


structure
    reds --> Console / Shell / ...

Supported type of commands:
    cmd0.cmdn.func(param1, param2, paramn)  <-- this one should be first

    cmd0.cmdn.indexed[index]
    cmd0.cmdn.indexed[index0][index1]

    cmd0.cmdn.indexed[index].func(param1, param2, paramn)
    cmd0.cmd1.indexed[index0][index1].cmdn.func(param1, param2, paramn)


Features
    - histrory
    - tab completion
    - easy new command implementation
    - to modes supported: integration in a project or in standalone
    - embedded documentation
    - script support


Built-in commands:

- misc
    \--> parameter for console 
        \--> histrory file location
        \--> prompt msg (default & included version)
        \--> globals ?? - in included version can be updaded by devloper ?
    \-> move not api modules in lib ??
    \--> move environment in its own file + adding envrioment param in it
    \--> python 2.x and 3.x support
- script
    \--> load()/execute() from shell
    \--> -c option
    \--> check standalone and included version
- standalone mode
    \--> load module
- documentation
    \--> general tool doc
    \--> embedded doc support
- deployement (see pycamera or other python lib as example)
- other
    --> GUI support 
    --> watch list ?
