#!/usr/bin/env python
import sys
from pcbnew import *
import wx
 
 
in_filename=sys.argv[1]
out_filename = sys.argv[2]
net_name = sys.argv[3]
via_spacing = sys.argv[4]
edge_clearance = sys.argv[5]
via_type_idx = sys.argv[6]
pcb = LoadBoard(in_filename)
 
 
pcb_bounding_box = pcb.ComputeBoundingBox()
pcb_bounding_box.inflate(-FromMils(edge_clearance))

rounded_via_spacing_x = ToMils(pcb_bounding_box.GetWidth())/int(ToMils(pcb_bounding_box.GetWidth())/via_spacing
rounded_via_spacing_y = ToMils(pcb_bounding_boxGetHeight())/int(ToMils(pcb_bounding_box.GetHeight())/via_spacing

for x in range(ToMils(pcb_bounding_box.GetX()), ToMils(pcb_bounding_box.GetX() + pcb_bounding_box.GetWidth()), rounded_via_spacing_x):
    for y in range(ToMils(pcb_bounding_box.GetY()), ToMils(pcb_bounding_box.GetY() + pcb_bounding_box.GetHeight()), rounded_via_spacing_y):
        print "adding a via..."
        new_via = VIA(pcb)
        new_via.SetPosition(wx.Point(x,y))
        pcb.Add(new_via)
         
pcb.Save(out_filename)
