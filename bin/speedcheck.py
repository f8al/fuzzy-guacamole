#!/bin/python
import ConfigParser
import os





#load configuration file
Config = ConfigParser.ConfigParser()
Config.read("../etc/shell.conf")


#config function
def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


HOST = ConfigSectionMap("global")['lhost']
PORT = ConfigSectionMap("global")['lport']