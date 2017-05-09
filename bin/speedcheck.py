#!/bin/python
import ConfigParser
import speedtest
import tweepy
from ConfigParser import SafeConfigParser


#load configuration file
parser = SafeConfigParser()
parser.read('../etc/guac.conf')


#print parser.get('twitter','consumer_key')




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
  c_key = parser.get('twitter', 'consumer_key')
  c_secret = parser.get('twitter', 'consumer_secret')
  a_token = parser.get('twitter', 'access_token')
  a_t_secret = parser.get('twitter','access_token_secret')

  cfg = {
    "consumer_key"        : c_key,
    "consumer_secret"     : c_secret,
    "access_token"        : a_token,
    "access_token_secret" : a_t_secret
    }

  api = get_api(cfg)
  tweet = "fuzzy-guacamole guac migration test 1"
  status = api.update_status(status=tweet)
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()

