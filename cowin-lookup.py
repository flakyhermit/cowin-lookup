#!/usr/bin/env python3
import json
import requests
import os
from datetime import datetime

dist_ids = [300, 302, 304]
date = datetime.now().strftime("%d-%m-%Y")
results = 0
for did in dist_ids:
    root = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?"
    districtstr = "district_id=" + str(did)
    datestr = "&date=" + date
    tail = "-H  accept: application/json -H  Accept-Language: en_US"
    URL = root + districtstr + datestr + tail
    r = requests.get(URL)
    results = r.json()
for center in results['centers']:
   for session in center['sessions']:
       if session['available_capacity'] >= 0:
           command = "notify-send 'Vaccine available!' '" + center['name'] + ", " +  str(center['pincode']) +  ", " + session['vaccine'] + "'"
           os.system(command)
           print(center['address'], center['pincode'], session['date'], session['available_capacity'], session['vaccine'])
