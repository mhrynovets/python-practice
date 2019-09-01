#!/usr/bin/python3
""" create SurveyMonkey survey routine """

import json
import sys
import argparse
import sm


def init_vars():
    """ Main routine """
    parser = argparse.ArgumentParser()
    parser.add_argument('-j', '--jsondata', default='new-survey.json',
                        type=argparse.FileType('r'),
                        help='File, that contains JSON for new survey')
    parser.add_argument('-c', '--configdata', default='sm.conf',
                        type=argparse.FileType('r+'),
                        help='File, that contains config')
    parser.add_argument('-e', '--emaildata', default='email_list.txt',
                        type=argparse.FileType('r'),
                        help='File, that contains emails for new survey')
    args = parser.parse_args()

    try:
        conf = json.load(args.configdata)
    except ValueError:
        print("Can't parse config file. Possible, 'init.py' "
              "routine was not executed. Exit.")
        sys.exit(1)

    try:
        sm_struct = json.load(args.jsondata)
    except ValueError:
        print("Can't parse data file ('sm.conf'). Possible, 'init.py' "
              "routine was not executed. Exit.")
        sys.exit(1)

    sm_mails = []
    for line in args.emaildata:
        if line.strip() != "":
            sm_mails.append(line.strip())

    if 'token' not in conf:
        print("No token found, run 'init.py' routine before start app. Exit.")
        sys.exit(1)

    return conf, sm_struct, sm_mails


def new_survey(conf, data):
    """ Survey chain - create survey """
    for surv_name, pages in data.items():
        resp_surv = sm.create_survey(conf["token"], surv_name)
        if not resp_surv:
            print("Problem during creating survey. Check logs.")
            return None
        conf['last_surv'] = {'id': resp_surv['id']}
        conf['last_surv']['errors'] = ""

        return new_pages(conf, pages, resp_surv['id'])


def new_pages(conf, data, surv_id):
    """ Survey chain - create pages """
    for page, questions in data.items():
        resp_page = sm.create_survey_page(conf["token"], surv_id, page)
        if not resp_page:
            conf['last_surv']['errors'] += '2'
            print(f"Problem during creating page '{page}'. Check logs.")
            return None

        return new_question(conf, questions, surv_id, resp_page['id'])


def new_question(conf, data, surv_id, page_id):
    """ Survey chain - create questions """
    for details in data.values():
        resp_question = sm.create_survey_page_question(conf["token"],
                                                       surv_id,
                                                       page_id,
                                                       details)
        if not resp_question:
            conf['last_surv']['errors'] += '3'
            print("Problem during creating question. Check logs.")
            return None

    return True


def remove_empty_page(conf, surv_id):
    """ Survey chain - remove empty page """
    pages = sm.get_survey_pages(conf["token"], surv_id)
    if not pages:
        conf['last_surv']['errors'] += '4'
        print("Problem during removing empty page. Check logs.")
        return None
    return sm.delete_survey_page(conf["token"], surv_id,
                                 pages['data'][0]['id'])


def new_collector(conf, surv_id, emails):
    """ Survey chain - create collector """
    resp_collector = sm.create_collector(conf["token"], surv_id)
    if not resp_collector:
        conf['last_surv']['errors'] += '5'
        print("Problem during creation collector. Check logs.")
        return None
    conf['last_surv']['collector_id'] = resp_collector['id']
    return new_message(conf, resp_collector['id'], emails)


def new_message(conf, coll_id, emails):
    """ Survey chain - create message """
    resp_message = sm.create_message(conf["token"], coll_id)
    if not resp_message:
        conf['last_surv']['errors'] += '6'
        print("Problem during creation message. Check logs.")
        return None
    conf['last_surv']['message_id'] = resp_message['id']
    return new_recipients(conf, coll_id, resp_message['id'], emails)


def new_recipients(conf, coll_id, mess_id, emails):
    """ Survey chain - create recipients """
    resp_recipients = sm.create_recipients(conf["token"], coll_id, mess_id,
                                           emails)
    if not resp_recipients:
        conf['last_surv']['errors'] += '7'
        print("Problem during creation recipients. Check logs.")
        return None
    return send_messages(conf, coll_id, mess_id)


def send_messages(conf, coll_id, mess_id):
    """ Survey chain - mend messages """
    respsend_invites = sm.send_invites(conf["token"], coll_id, mess_id)
    if not respsend_invites:
        conf['last_surv']['errors'] += '8'
        print("Problem during sending messages. Check logs.")
        return None
    return True


def main(conf, sm_struct, sm_mails):
    """ Main routine """
    res = new_survey(conf, sm_struct)
    if res is not None:
        res = remove_empty_page(conf, conf['last_surv']['id'])
    if res is not None:
        res = new_collector(conf, conf['last_surv']['id'], sm_mails)

    if conf['last_surv']['errors'] == "":
        print("Survey created, invites sent.")
        print("Now you can check stats with script 'get_stats.py'")
        print("You can get structure of survey with script 'get_struct_sm.py'")
    else:
        print("Some errors was detected during deployment. "
              "Error codes:", " ".join(conf['last_surv']['errors']))

    with open('sm.conf', 'w') as outfile:
        json.dump(conf, outfile, indent=2)


if __name__ == "__main__":
    CONF, DATA, EMAILS = init_vars()
    main(CONF, DATA, EMAILS)
