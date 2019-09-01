#!/usr/bin/python3
""" Show survey shipment stats """
import json
import sm

with open('sm.conf') as json_file:
    CONF = json.load(json_file)

RESP = sm.message_info(CONF['token'], CONF['collector_id'],
                       CONF['message_id'])
print(json.dumps(RESP, indent=4, sort_keys=True))
print()
print("-"*30)
print()

RESP = sm.message_stats(CONF['token'], CONF['collector_id'],
                        CONF['message_id'])
print(json.dumps(RESP, indent=4, sort_keys=True))
