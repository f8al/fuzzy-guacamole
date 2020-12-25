#!/bin/python
import speedtest
import tweepy
import configparser
import os
import logging


pwd = os.getcwd()

#load configuration file
parser = configparser.ConfigParser()
config = pwd + '/etc/speedtest.conf'
parser.read( config ) #change this to speedtest.conf once configured


def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])

    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logging.error("Error creating API", exc_info=True)
        raise e
    logging.info("API created")
    return api


def main():
    '''get configs'''
    c_key = parser['twitter']['consumer_key']
    c_secret = parser['twitter']['consumer_secret']
    a_token = parser['twitter']['access_token']
    a_t_secret = parser['twitter']['access_token_secret']
    handle = parser['twitter']['isp_handle']
    down = parser['global']['speed_down']
    up = parser['global']['speed_up']

    '''SPEED TEST'''
    servers = []
    threads = 10
    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads, pre_allocate=False)
    s.results.share()
    results = s.results.dict()

    dl = float(results["download"])
    ul = float(results["upload"])
    dl = ((dl / 1024) / 1024)
    ul = ((ul / 1024) / 1024)
    dl = round(dl,2)
    ul = round(ul,2)
    down = parser['global']['speed_down']
    up = parser['global']['speed_up']

    cfg = {
        "consumer_key"        : c_key,
        "consumer_secret"     : c_secret,
        "access_token"        : a_token,
        "access_token_secret" : a_t_secret
    }
    api = get_api(cfg)
    if float(dl) <= float(down) * 0.66 and float(ul) <= float(up) * 0.66:
        tweet = f"hey {handle} fuzzy-guacamole says current download speed is {dl} Mbps & upload is {ul} Mbps! This is < 66% of paid service level! #fuzzyguac"
    elif float(dl) <= float(down) * 0.66:
        tweet = f"hey {handle} fuzzy-guacamole says current download speed is {dl} Mbps! This is less than 66% of paid service level! #shame #fuzzyguac"
    elif float(ul) <= float(up) * 0.66:
        tweet = f"hey {handle} fuzzy-guacamole says current upload speed is {ul} Mbps! This is less than 66% of paid service level! #shame #fuzzyguac"
    else:
        exit()
    print(tweet)
    api.update_status(status=tweet)

if __name__ == "__main__":
  main()

