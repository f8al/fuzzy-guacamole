#!/bin/python
import speedtest
import tweepy
import requests
from ConfigParser import SafeConfigParser


#load configuration file
parser = SafeConfigParser()
parser.read('../etc/guac.conf') #change this to speedtest.conf once configured

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)


def main():
    '''get configs'''
    c_key = parser.get('twitter', 'consumer_key')
    c_secret = parser.get('twitter', 'consumer_secret')
    a_token = parser.get('twitter', 'access_token')
    a_t_secret = parser.get('twitter','access_token_secret')
    handle = parser.get('twitter', 'isp_handle')
    down = parser.get('global','speed_down')
    up = parser.get('global', 'speed_up')
    HEC_token = parser.get('global', 'HEC_token')

    '''SPEED TEST'''
    servers = []
    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download()
    s.upload()
    results_dict = s.results.dict()

    dl = float(results_dict["download"])
    ul = float(results_dict["upload"])
    dl = ((dl / 1024) / 1024)
    ul = ((ul / 1024) / 1024)
    dlr = round(dl,4)
    ulr = round(ul,4)

    cfg = {
        "consumer_key"        : c_key,
        "consumer_secret"     : c_secret,
        "access_token"        : a_token,
        "access_token_secret" : a_t_secret
    }
    api = get_api(cfg)
    if float(dlr) <= float(down) * 0.66:
        tweet = "hey "+ handle +" fuzzy-guacamole says current download speed is " + str(dlr) + " Mbps! This is less than 66% of paid service level! #shame #fuzzyguac"
        print tweet
    elif float(ulr) <= float(up) * 0.66:
        tweet = "hey "+ handle +" fuzzy-guacamole says current upload speed is " + str(ulr) + " Mbps! This is less than 66% of paid service level! #shame #fuzzyguac"
        print tweet
    elif float(dlr) <= float(down) * 0.66 and float(ulr) <= float(up) * 0.66:
        tweet = "hey " + handle + " fuzzy-guacamole says current download speed is " + str(dlr) + "Mbps & upload is " + str(ulr) + "Mbps! This is < 66% of paid service level! #fuzzyguac"
        print tweet
    else:
        exit()
    status = api.update_status(status=tweet)
    headers = {'Authorization' : HEC_token}
    payload = results_dict
    r = requests.post('http://posttestserver.com/post.php', headers=headers, data=payload)
    print r
    print r.text
    print r.headers

if __name__ == "__main__":
  main()

