#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =========================================================================== #
# pyreds - REDS Institute, HEIG-VD, Yverdon-les-Bains (CH) - 2017             #
# =========================================================================== #
""" Client main

Long description
"""
# =========================================================================== #
__author__ = "Jean-Pierre Miceli <jean-pierre.miceli@heig-vd.ch"
# =========================================================================== #


# == pyreds libs
import pyreds


class HelloWorld(pyreds.Command):
    _brief       = "Hello World command"
    _description = "Hello World command"

    def _function(self):
        print "Hello World!"

class Add(pyreds.Command):
    _brief       = "Simple Addition"
    _description = "return the sum of ValA + ValB"

    _input = pyreds.Params(pyreds.Input('ValA', "Value A"),
                           pyreds.Input('ValB', "Value B"))

    def _function(self, valA, valB):
        return valA + valB

class Toto(pyreds.Command):
    _brief       = "Toto command"
    _description = "This command is used to test the completer"

    param1 = {'One' : 1,
              'Two' : 2,
              'Three' : 3}

    param2 = {True  : True,
              False : False}

    _input = pyreds.Params(pyreds.Input('param1', "param1", param1),
                           pyreds.Input('param2', "param2", param2))

    def _function(self, param1, param2):
        print param1
        print param2

class Test(pyreds.Module):
    helloWorld = HelloWorld()
    add = Add()
    toto = Toto()




cli = pyreds.console.InteractiveConsole()
cli.addModule(Test)
cli.start()
