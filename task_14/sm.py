#!/usr/bin/python3
""" core functions for SurveyMonkey """

import datetime
import requests


def call_api(token, method, uri, payload='{}'):
    """ Basic function to comunicate with SM """
    if method not in ['get', 'post', 'delete']:
        return None

    url_header = "https://api.surveymonkey.com/v3/"

    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    })

    mcall = getattr(session, method)
    if method == 'post':
        result = mcall(url_header+uri, json=payload)
    else:
        result = mcall(url_header+uri)

    date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = "logs/cs-resp-{}-{}-{}.txt".format(date,
                                               method,
                                               result.status_code)
    with open(fname, 'w') as log_file:
        log_file.write(result.text)

    if (result.status_code // 10) == 20:
        return result.json()

    return None


def get_surveys(token):
    """ Get surveys by token """
    url = "surveys"
    resp = call_api(token, 'get', url)
    return resp


def create_survey(token, title="My Survey"):
    """ Create survey """
    payload = {"title": title}
    url = "surveys"
    resp = call_api(token, 'post', url, payload)
    return resp


def get_survey_pages(token, survey_id):
    """ Get pages in defined survey """
    url = "surveys/{}/pages".format(survey_id)
    resp = call_api(token, 'get', url)
    return resp


def delete_survey_page(token, survey_id, page_id):
    """ Delete page in defined survey """
    url = "surveys/{}/pages/{}".format(survey_id, page_id)
    resp = call_api(token, 'delete', url)
    return resp


def create_survey_page(token, survey_id, page_name="My Page"):
    """ Create page in defined survey """
    payload = {"title": page_name}
    url = "surveys/{}/pages".format(survey_id)
    resp = call_api(token, 'post', url, payload)
    return resp


def create_survey_page_question(token, survey_id, page_id, params):
    """ Create question in defined survey and page """
    payload = {}
    payload["headings"] = []
    payload["headings"].append({"heading": params['Description']})
    payload["family"] = "single_choice"
    payload["subtype"] = "vertical"
    payload["answers"] = {}
    payload["answers"]["choices"] = []
    for answer in params['Answers']:
        payload["answers"]["choices"].append({"text": answer})

    url = "surveys/{}/pages/{}/questions".format(survey_id, page_id)
    resp = call_api(token, 'post', url, payload)
    return resp


def get_survey_page_question(token, survey_id, page_id):
    """ Get questions in defined survey and page """
    url = "surveys/{}/pages/{}/questions".format(survey_id, page_id)
    resp = call_api(token, 'get', url)
    return resp


def create_collector(token, survey_id):
    """ Create collector """
    payload = {"type": "email"}
    url = "surveys/{}/collectors".format(survey_id)
    resp = call_api(token, 'post', url, payload)
    return resp


def create_message(token, collector_id):
    """ Create message """
    payload = {"type": "invite"}
    url = "collectors/{}/messages".format(collector_id)
    resp = call_api(token, 'post', url, payload)
    return resp


def create_recipients(token, collector_id, message_id, emails):
    """ Create list of recipients """
    payload = {}
    payload['contacts'] = [{"email": x} for x in emails]
    url = "collectors/{}/messages/{}/recipients/bulk".format(
        collector_id, message_id)
    resp = call_api(token, 'post', url, payload)
    return resp


def send_invites(token, collector_id, message_id):
    """ Send created message to defined recipients """
    timestamp = datetime.datetime.now() - datetime.timedelta(days=1)
    payload = {"scheduled_date": timestamp.strftime("%Y-%m-%dT%H:%M:%S")}
    url = "collectors/{}/messages/{}/send".format(collector_id, message_id)
    resp = call_api(token, 'post', url, payload)
    return resp


def message_info(token, collector_id, message_id):
    """ Get info about message """
    url = "collectors/{}/messages/{}".format(collector_id, message_id)
    resp = call_api(token, 'get', url)
    return resp


def message_stats(token, collector_id, message_id):
    """ Get info about message """
    url = "collectors/{}/messages/{}/stats".format(collector_id, message_id)
    resp = call_api(token, 'get', url)
    return resp


def get_user(token):
    """ Get info about user """
    url = "users/me"
    resp = call_api(token, 'get', url)
    return resp
