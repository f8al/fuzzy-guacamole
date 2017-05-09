#!/bin/python
import ConfigParser
import speedtest
import tweepy

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





def s_test():
    #servers = []
    # If you want to test against a specific server
    # servers = [1234]
    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download()
    s.upload()
    results_dict = s.results.dict()
    print "Download speed is: " + str(results_dict["download"]) + "!"
    print "Upload speed is: " + str(results_dict["upload"]) + "!"
    print "Ping is: " + str(results_dict["ping"]) + "!"






def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = {
    "consumer_key"        : "VALUE",
    "consumer_secret"     : "VALUE",
    "access_token"        : "VALUE",
    "access_token_secret" : "VALUE"
    }

  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet)
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()

