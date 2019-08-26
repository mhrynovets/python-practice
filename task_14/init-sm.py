#!/usr/bin/python3
import json
import sys
import requests

def getUser(auth_token):
    s = requests.Session()
    s.headers.update({
        "Authorization": "Bearer %s" % auth_token,
        "Content-Type": "application/json"
    })
    url = "https://api.surveymonkey.com/v3/users/me"

    r = s.get(url)
    with open("logs/resp"+str(hash(r.text))+".txt", "w") as f:
        f.write(r.text)
    return r

def getSurveys(auth_token):
    s = requests.Session()
    s.headers.update({
        "Authorization": "Bearer %s" % auth_token,
        "Content-Type": "application/json"
    })
    url = "https://api.surveymonkey.com/v3/surveys"
    r = s.get(url)
    with open("logs/resp"+str(hash(r.text))+".txt", "w") as f:
        f.write(r.text)
    return r


if (len(sys.argv) == 2):
    token = str(sys.argv[1])
else:
    print("Input SurveyMonkey token to use:")
    token = str(input('> '))

token = token.strip().strip("'\"")

if (token == ""):
    print("Empty token forbidden. Exit.")
    sys.exit(1)

resp = getUser(token)

if ((resp.status_code //10 ) != 20):
    print("Wrong token. Exit.")
    sys.exit(1)

print("Hello", resp.json()["username"], ", lets go!")
resp = getSurveys(token)
j = resp.json()

conf = {}
conf["token"] = token
conf['surveys'] = []
for i in j["data"]:
    surv = {}
    surv["id"] = i["id"]
    surv["title"] = i["title"]
    conf['surveys'].append(surv)

with open('sm.conf', 'w') as outfile:
    json.dump(conf, outfile, indent=2)
