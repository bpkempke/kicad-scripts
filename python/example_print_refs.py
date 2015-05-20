#!/usr/bin/env python
import sys
from pcbnew import *
 
 
filename=sys.argv[1]
 
pcb = LoadBoard(filename)
for module in pcb.GetModules():   
    print "* Module: %s"%module.GetReference()
