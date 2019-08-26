#!/usr/bin/python3
import json
import sys
import requests
import datetime


def callAPI(token, method, uri, payload='{}'):
    if not method in ['get', 'post', 'delete']:
        return None

    s = requests.Session()
    s.headers.update({
        "Authorization": "Bearer %s" % token,
        "Content-Type": "application/json"
    })

    mcall = getattr(s, method)
    if method == 'post':
        result = mcall(uri, json=payload)
    else:
        result = mcall(uri)

    date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    with open("logs/resp-%s-%s-%s.txt" % (date, method, result.status_code), 'w') as f:
        f.write(result.text)

    if (result.status_code // 10) == 20:
        return result.json()
    else:
        return None

    return result

#######################################################################
###  Begin
with open('sm.conf') as json_file:
    conf = json.load(json_file)

collector_id = conf['collectorID']
message_id = conf['messageID']


url = "https://api.surveymonkey.com/v3/collectors/%s/messages/%s/stats" % (
    collector_id, message_id)
resp = callAPI(conf["token"], 'get', url)
print(json.dumps(resp, indent=4, sort_keys=True))
print()
print("---------------------------------------------------------------")
print()

url = "https://api.surveymonkey.com/v3/collectors/%s/messages/%s" % (
    collector_id, message_id)
resp = callAPI(conf["token"], 'get', url)
print(json.dumps(resp, indent=4, sort_keys=True))
print()
print("---------------------------------------------------------------")
print()
