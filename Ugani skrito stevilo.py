#!/usr/bin/env python
# -*- coding: utf-8 -*-

secret = 7

guess = int(raw_input("Ugani skrito število: "))

if guess == secret:
    print "Bravo, uganil si skrito število. To število je " + str(secret) + "."

if guess != secret:
    print "Napačen odgovor, več sreče prihodnjič."
