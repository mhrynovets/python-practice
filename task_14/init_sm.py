#!/usr/bin/python3
""" Prepare SurveyMonkey script """
import json
import sys
import sm


def main():
    """ Main routine """
    if len(sys.argv) == 2:
        token = str(sys.argv[1])
    else:
        print("Input SurveyMonkey token to use:")
        token = str(input('> '))

    token = token.strip().strip("'\"")

    if token == "":
        print("Empty token forbidden. Exit.")
        sys.exit(1)

    resp = sm.get_user(token)

    if (resp.status_code // 10) != 20:
        print("Wrong token. Exit.")
        sys.exit(1)

    print("Hello", resp.json()["username"], ", lets go!")
    resp = sm.get_surveys(token)
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


if __name__ == "__main__":
    main()
