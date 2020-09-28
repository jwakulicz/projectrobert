#!/usr/bin/env python

import sys
import subprocess

def matching_line(lines, keyword):
    for line in lines:
        matching = match(line,keyword)
        if matching != None:
            return matching
    return None
    
def match(line,keyword):
    line = line.lstrip()
    length = len(keyword)
    if line[:length] == keyword:
        return line[length:]
    else:
        return None
    
def get_quality():
    quality = matching_line(cell, "Quality=").split()[0].split('/')
    return str(int(round(float(quality[0])/float(quality[1]) * 100))).rjust(3)
    
def get_name(cell):
    return matching_line(cell,"ESSID:")[1:-1]
    
def do_wlist_scan():
    out = subprocess.Popen(['iwlist','wlan0','scan'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    if stderr != None
        return stderr
    return stdout
    
if __name__ == "__main__":
    cells = [[]]
    parsed_cells=[]
    
    for line in do_wlist_scan():
        cell_line = match(line, "Cell ")
        if cell_line != None:
            cells.append([])
            line = cell_line[-27:]
        cells[-1].append(line.rstrip())
        
    cells=cells[1:]
    
    for cell in cells:
        parsed_cells.append({"Name:":get_name(cell), "Strength": get_quality(cell)})
    
    print(parced_cells)
