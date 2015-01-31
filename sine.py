#!/usr/bin/python

import json
import math
import requests
import sys
from time import sleep
import os

INFLUX_PROTO = os.getenv('INFLUXDB_PROTO', 'http')
INFLUX_HOST = os.getenv('INFLUXDB_HOST', 'localhost')
INFLUX_PORT = os.getenv('INFLUXDB_PORT', '8086')
INFLUX_DATABASE = os.getenv('INFLUXDB_NAME', 'test1')
INFLUX_USER = os.getenv('INFLUXDB_USER', 'root')
INFLUX_PASS = os.getenv('INFLUXDB_PASS', 'root')

STATUS_MOD = 10

POST_URL = '%s://%s:%s/db/%s/series' % (INFLUX_PROTO, INFLUX_HOST, INFLUX_PORT, INFLUX_DATABASE)

parameters = {'u': INFLUX_USER, 'p': INFLUX_PASS}

print("POST_URL = %s" % POST_URL)

n = 0
while True:
    for d in range(0, 360):
        v = [{'name': 'sin', 'columns': ['val'], 'points': [[math.sin(math.radians(d))]]}]
        #print("%s" % json.dumps(v))
        r = requests.post(POST_URL, params=parameters, data=json.dumps(v))
        if r.status_code != 200:
            print('Failed to add point to influxdb -- aborting.')
            sys.exit(1)
        n += 1
        sleep(1)
        if n % STATUS_MOD == 0:
            print('%d points inserted.' % n)
