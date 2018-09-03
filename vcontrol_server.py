#! /usr/bin/env python3

# D-Bus Server 

from gi.repository import GLib
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop

from gi.repository import GObject
import threading

import tkinter as tk
import alsaaudio
import sys
from tkinter import ttk
from tkinter import *


class Session_DBus(dbus.service.Object):
    def __init__(self):
        bus_name = dbus.service.BusName('org.me.p_session', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/org/me/p_session')
     
    @dbus.service.method('org.me.p1')    
    class Vbar:
    
        def __init__(self,master):
            frame=Frame(master)
            frame.pack()
            self.valuex=IntVar() 
            p=ttk.Progressbar(frame, length=200, mode="determinate", variable=self.valuex)
            p.pack()
            master.withdraw()
            #self.mixer=alsaaudio.Mixer()
        def mix(self):
            self.mixer=alsaaudio.Mixer()
            self.volume=self.mixer.getvolume()[0] 
            valuex=self.valuex.set(self.volume)
            
    @dbus.service.method('org.me.p2')
    def expand(self):
        root.deiconify()
        root.after(3000,root.withdraw)
        
    
    
    
    @dbus.service.method('org.me.p2')    
    

    def volumeup(self):
        self.mixer=alsaaudio.Mixer()
        self.volume=self.mixer.getvolume()[0]
        up=self.volume+5
        self.mixer.setvolume(up)
    
    
DBusGMainLoop(set_as_default=True)
dbus_service = Session_DBus()


root=Tk()
pp=Session_DBus.Vbar(root)
    #pp.mix()
def pbar():
    pp.mix()
    root.after(100,pbar)  
root.after(99,pbar)







    
def dbus_timeout_periodic():
    root.update_idletasks()
   
    

    
GObject.timeout_add(100,dbus_timeout_periodic)
dbus_loop=GObject.MainLoop()


dbus_thread=threading.Thread(target=dbus_loop.run)
dbus_thread.start()
root.mainloop()