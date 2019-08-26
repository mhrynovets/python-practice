#!/usr/bin/python3
import json
import sys
import requests
import datetime

######
# Define functions
######


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
    with open("logs/cs-resp-%s-%s-%s.txt" % (date, method, result.status_code), 'w') as f:
        f.write(result.text)

    if (result.status_code // 10) == 20:
        return result.json()
    else:
        return None

    return result


def getSurveys(token):
    url = "https://api.surveymonkey.com/v3/surveys"
    resp = callAPI(token, 'get', url)
    return resp


def createSurvey(token, title="My Survey"):
    payload = {"title": title}
    url = "https://api.surveymonkey.com/v3/surveys"
    resp = callAPI(token, 'post', url, payload)
    return resp


def getSurveyPages(token, surveyID):
    url = "https://api.surveymonkey.com/v3/surveys/%s/pages" % (surveyID)
    resp = callAPI(token, 'get', url)
    return resp


def deleteSurveyPage(token, surveyID, pageID):
    url = "https://api.surveymonkey.com/v3/surveys/%s/pages/%s" % (
        surveyID, pageID)
    resp = callAPI(token, 'delete', url)
    return resp


def createSurveyPage(token, surveyID, pageName="My Page"):
    payload = {"title": pageName}
    url = "https://api.surveymonkey.com/v3/surveys/%s/pages" % (surveyID)
    resp = callAPI(token, 'post', url, payload)
    return resp


def createSurveyPageQuestion(token, surveyID, pageID, params):
    payload = {}
    payload["headings"] = []
    payload["headings"].append({"heading": params['Description']})
    payload["family"] = "single_choice"
    payload["subtype"] = "vertical"
    payload["answers"] = {}
    payload["answers"]["choices"] = []
    for answer in params['Answers']:
        payload["answers"]["choices"].append({"text": answer})

    url = "https://api.surveymonkey.com/v3/surveys/%s/pages/%s/questions" % (
        surveyID, pageID)
    resp = callAPI(token, 'post', url, payload)
    return resp


def createCollector(token, surveyID):
    payload = {"type": "email"}
    url = "https://api.surveymonkey.com/v3/surveys/%s/collectors" % (surveyID)
    resp = callAPI(token, 'post', url, payload)
    return resp


def createMessage(token, collectorID):
    payload = {
        "type": "invite",
    }
    url = "https://api.surveymonkey.com/v3/collectors/%s/messages" % (
        collectorID)
    resp = callAPI(token, 'post', url, payload)
    return resp


def createRecipients(token, collectorID, messageID, emails):
    payload = {}
    payload['contacts'] = [ { "email":x.strip() } for x in emails if x.strip != "" ]
    url = "https://api.surveymonkey.com/v3/collectors/%s/messages/%s/recipients/bulk" % (
        collectorID, messageID)
    resp = callAPI(token, 'post', url, payload)
    return resp


def sendInvites(token, collectorID, messageID):
    payload = { "scheduled_date": (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%S") }
    url = "https://api.surveymonkey.com/v3/collectors/%s/messages/%s/send" % (
        collectorID, messageID)
    resp = callAPI(token, 'post', url, payload)
    return resp


##########
# Start
##########


try:
    with open('new-survey.json') as f:
        sm_struct = json.load(f)
except:
    print("Can't read json with new survey ('new-survey.json'). Exiting...")
    sys.exit(1)

try:
    with open('email_list.txt') as f:
        sm_mails = f.readlines()
except:
    print("Can't read list with emails ('email_list.txt'). Exiting...")
    sys.exit(1)

try:
    with open('sm.conf') as json_file:
        conf = json.load(json_file)
except:
    print("Can't read config file ('sm.conf'). Possible, 'init.py' routine was not executed. Exiting...")
    sys.exit(1)

if not 'token' in conf:
    print("No token found, run 'init.py' routine before start app. Exiting...")
    sys.exit(1)

survID = 0
collectorID = 0
messageID = 0
err_status = []

for surv, pages in sm_struct.items():
    print()
    print("createSurvey(token, "+surv+")")
    respSurv = createSurvey(conf["token"], surv)
    if (respSurv == None):
        print("Error on creating survey", surv)
        err_status.append(1)
    else:
        survID = respSurv['id']
        for page, questions in pages.items():
            print()
            print("createSurveyPage(token, %s, %s)" % (respSurv['id'], page))
            respPage = createSurveyPage(conf["token"], respSurv['id'], page)
            if (respPage == None):
                print("Error on creating page", page)
                err_status.append(2)
            else:
                for question, details in questions.items():
                    print()
                    print("createSurveyPageQuestion(token, %s, %s, details)" %
                          (respSurv['id'], respPage['id']))
                    print(details)
                    respQuestion = createSurveyPageQuestion(
                        conf["token"], respSurv['id'], respPage['id'], details)
                    if (respQuestion == None):
                        print("Error on creating question", question)
                        err_status.append(3)
        # Clean up a default generated empty page
        print()
        print("getSurveyPages(token, %s)" % (respSurv['id']))
        pages = getSurveyPages(conf["token"], respSurv['id'])
        if (pages == None):
            print("Error on fetching pages in surv ", surv)
            err_status.append(4)
        else:
            print("deleteSurveyPage(token, %s, %s)" %
                  (respSurv['id'], pages['data'][0]['id']))
            deleteSurveyPage(conf["token"], respSurv['id'],
                             pages['data'][0]['id'])
        print("createCollector(token, %s)" % (respSurv['id']))
        respCollector = createCollector(conf["token"], respSurv['id'])
        if (respCollector == None):
            print("Error on creating collector in surv ", surv)
            err_status.append(5)
        else:
            collectorID = respCollector['id']
            print("createMessage(token, %s)" % (respCollector['id']))
            respMessage = createMessage(conf["token"], respCollector['id'])
            if (respMessage == None):
                print("Error on creating message in surv ", surv)
                err_status.append(6)
            else:
                messageID = respMessage['id']
                print("createRecipients(token, %s, %s, sm_mails)" % (respCollector['id'], respMessage['id']))
                respRecipients = createRecipients(conf["token"], respCollector['id'], respMessage['id'], sm_mails)
                if (respRecipients == None):
                    print("Error on creating recipients list in surv ", surv)
                    err_status.append(7)
                else:
                    print("sendInvites(token, %s, %s)" % (respCollector['id'], respMessage['id']))
                    respSendInvites = sendInvites(conf["token"], respCollector['id'], respMessage['id'])
                    if (respSendInvites == None):
                        print("Error on sending invites in surv ", surv)
                        err_status.append(8)
if not err_status:
    print("Survey created, invites sent.") 
    print("Now you can check stats with script 'get_stats.py'")
    print("You can get structure of survey with script 'get_struct_sm.py'")
else:
    print("Some errors was detected during deployment. Error codes:"," ".join(err_status))

conf['survID'] = survID
conf['collectorID'] = collectorID
conf['messageID'] = messageID

with open('sm.conf', 'w') as outfile:
    json.dump(conf, outfile, indent=2)

