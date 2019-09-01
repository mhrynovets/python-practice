#!/usr/bin/python3
""" Show survey structure """
import json
import sm

with open('sm.conf') as json_file:
    CONF = json.load(json_file)

RESP_SURV = sm.get_surveys(CONF['token'])
print(json.dumps(RESP_SURV, indent=4, sort_keys=True))
print()
print("-"*30)
print()

RESP_PAGES = sm.get_survey_pages(CONF['token'], CONF['surv_id'])
print(json.dumps(RESP_PAGES, indent=4, sort_keys=True))
print()
print("-"*30)
print()

for PAGE in RESP_PAGES["data"]:
    resp_questions = sm.get_survey_page_question(CONF['token'],
                                                 CONF['surv_id'],
                                                 PAGE["id"])
    print(json.dumps(resp_questions, indent=4, sort_keys=True))
    print()
