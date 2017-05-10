# fuzzy-guacamole
A tool for checking your internet speeds and annoying your ISP with notifications when you don't get what you pay for.

This app is meant to be run on a raspberry pi attached via ethernet cable to your modem/router, not via wifi, or locally
via cron on a hardware firewall.


# Requirements
This app requires a couple of python packages installable with pip. Run `pip install -r requirements.txt` to get them:
- tweepy
- speedtest-cli

This app also requires a twitter app / developer account.  Sign up and create your own at dev.twitter.com (its free)

Once that has been created you will need to update ./etc/speedtest.conf

Required details needed are as follows:

- Subscribed ISP service level in MBps down/up
- ISP twitter handle
- twitter app consumer_key        
- twitter app consumer_secret     
- twitter access_token        
- twitter access_token_secret 
- Splunk HTTP Event Collector Token