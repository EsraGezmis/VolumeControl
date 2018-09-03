#!/usr/bin/env python3                                              
 
# D-Bus Client 
 
import dbus                                                                    
import tkinter as tk
import alsaaudio
import sys
from tkinter import ttk
from tkinter import *


       
                                                                                 
bus = dbus.SessionBus()                                                       
session = bus.get_object("org.me.p_session", "/org/me/p_session")                                                                                               



#if sys.argv[1]=="up":
#    method_message7 = session.get_dbus_method('volumeup', 'org.me.p2') 
#    method_message7()
#    method_message8 = session.get_dbus_method('expand', 'org.me.p2') 
#    method_message8()

method_message7 = session.get_dbus_method('volumeup', 'org.me.p2') 
method_message7()
method_message8 = session.get_dbus_method('expand', 'org.me.p2') 
method_message8()


