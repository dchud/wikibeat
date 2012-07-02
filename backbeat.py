#!/usr/bin/env python

import time

from OSC import OSCClient, OSCMessage
import requests

BASE_URL = 'http://localhost:3000/stats'
WIKIPEDIAS = ["ar-wikipedia", "bg-wikipedia", "ca-wikipedia",
    "cs-wikipedia", "da-wikipedia", "de-wikipedia", "el-wikipedia",
    "en-wikipedia", "eo-wikipedia", "es-wikipedia", "eu-wikipedia",
    "fa-wikipedia", "fi-wikipedia", "fr-wikipedia", "he-wikipedia",
    "hu-wikipedia", "id-wikipedia", "it-wikipedia", "ja-wikipedia",
    "ko-wikipedia", "lt-wikipedia", "ms-wikipedia", "nl-wikipedia",
    "no-wikipedia", "pl-wikipedia", "pt-wikipedia", "ro-wikipedia",
    "ru-wikipedia", "sk-wikipedia", "sl-wikipedia", "sv-wikipedia",
    "tr-wikipedia", "uk-wikipedia", "vi-wikipedia", "vo-wikipedia",
    "zh-wikipedia"] 

if __name__ == '__main__':
    client = OSCClient()
    client.connect(('localhost', 9999))
    while 1:
        beats = []
        for wp in WIKIPEDIAS:
            url = '%s/%s/60000.json' % (BASE_URL, wp)
            r = requests.get(url)
            beats.append(int(r.content))
        sorted_beats = sorted(beats, reverse=True)[:20]
        print sorted_beats
        for i in range(len(sorted_beats)):
            m = OSCMessage('/wikibeat/%s' % str(i + 1))
            m.append(sorted_beats[i])
            client.send(m)
        time.sleep(1)
    
