#!/usr/bin/python

import json
import sys,socket,os
from urlparse import urlparse
import urllib2

try:
    os.remove('host-data')
except OSError:
    pass #silenty fail to not delete file
json_data=urllib2.urlopen('http://tilde.club/~pfhawkins/othertildes.json')
data = json.load(json_data)
#manually add the tilde.club as it isn't in the JSON returned
data['tilde.club'] = 'http://tilde.club'
for attribute, value in data.iteritems():
    with open("host-data", "a") as hfile:
        ur = urlparse(value)
        hfile.write("#{0}\n{1} {2}\n".format(attribute, socket.gethostbyname(ur.netloc), ur.netloc))
json_data.close()
