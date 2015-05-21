#!/usr/bin/env python
import sys
from pcbnew import *
import wx
import numpy as np 
 
in_filename=sys.argv[1]
out_filename = sys.argv[2]
net_name = sys.argv[3]
via_spacing = sys.argv[4]
edge_clearance = sys.argv[5]
via_type_idx = sys.argv[6]
pcb = LoadBoard(in_filename)
 
net_code = pcb.FindNet(net_name).GetNet()
 
pcb_bounding_box = pcb.ComputeBoundingBox()
pcb_bounding_box.Inflate(-FromMils(int(edge_clearance)))

rounded_via_spacing_x = ToMils(pcb_bounding_box.GetWidth())/int(ToMils(pcb_bounding_box.GetWidth())/float(via_spacing))
rounded_via_spacing_y = ToMils(pcb_bounding_box.GetHeight())/int(ToMils(pcb_bounding_box.GetHeight())/float(via_spacing))

for x in np.arange(ToMils(pcb_bounding_box.GetX()), ToMils(pcb_bounding_box.GetX() + pcb_bounding_box.GetWidth()), rounded_via_spacing_x):
    for y in np.arange(ToMils(pcb_bounding_box.GetY()), ToMils(pcb_bounding_box.GetY() + pcb_bounding_box.GetHeight()), rounded_via_spacing_y):
        print "adding a via...%f %f"%(x,y)
        new_via = VIA(pcb)
        new_via.SetPosition(wxPoint(FromMils(float(x)),FromMils(float(y))))
        new_via.SetNetCode(net_code)
        pcb.Add(new_via)
         
pcb.Save(out_filename)
