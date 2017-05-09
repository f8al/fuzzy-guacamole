#!/bin/python
import ConfigParser
import os
import speedtest
import json





#load configuration file
Config = ConfigParser.ConfigParser()
Config.read("../etc/speedcheck.conf")

print Config

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


#HOST = ConfigSectionMap("global")['lhost']
#PORT = ConfigSectionMap("global")['lport']


servers = []
# If you want to test against a specific server
# servers = [1234]

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download()
s.upload()


results_dict = s.results.dict()

print results_dict

output = json.loads({results_dict}, sort_keys=True, indent=4, seperators=(',', ': '))

print output