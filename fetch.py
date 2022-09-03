import json
import os
from datetime import datetime, timedelta
import requests
import matplotlib
import numpy as np
import cfg
import sys
import argparse
import shutil
import pprint

parser = argparse.ArgumentParser()

if os.path.exists("data.json"):
    os.remove("data.json")

API_key = cfg.API_key
production = cfg.production
production_types = list(production.keys())
production_types.sort()
transfer = cfg.transfer
bidding_areas = list(transfer.keys())
bidding_areas.sort()

url = 'https://api.fingrid.fi/v1/variable/{}/events/json'
headers = {'x-api-key':API_key, 'Accept':'application/json'}





start = datetime.now() - timedelta(days=365)
end = datetime.now() - timedelta(days=364)

for i in range(360):

    payload = {'start_time':'{}:00+0000'.format(datetime.strftime(start, '%Y-%m-%dT%H:%M')), 'end_time':'{}:00+0000'.format(datetime.strftime(end, '%Y-%m-%dT%H:%M'))}

    r = requests.get(url.format(production["Wind"]), headers=headers, params=payload)


    pprint.pprint(r.json())

    with open("data.json","a") as output:

        for event in r.json():
            output.write(json.dumps(event)+"\n")

    start = start + timedelta(days=1)
    end = end + timedelta(days=1)
