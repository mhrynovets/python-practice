#!/usr/bin/python3
""" Represent provided JSON as HTML file with tables """
# 5. Create script, which represents provided JSON as HTML file with tables.
# You can choose which fields can be present,
# but the number of them should be at least 5. (jinja2)

import json
import os
import sys
import argparse
from jinja2 import Template


def init_vars():
    """ Parse args and prepare variables """
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help='incomming JSON file')
    parser.add_argument('-i', '--include', nargs='?', action='append',
                        help='which field to include. If set - displayed '
                             'will be only included fields. Flag can be '
                             'used multiple times to backup many files.')
    parser.add_argument('-e', '--exclude', nargs='?', action='append',
                        help='which field to exclude. Flag can be '
                             'used multiple times to backup many files.')
    parser.add_argument('-f', '--htmlfile',
                        help='Path with name for output file.')
    parser.add_argument('-y', '--yes', action='store_true',
                        help='Overwrite existing output file.')
    parser.add_argument('-s', '--preventscreen', action='store_true',
                        help='Prevent writing output to stdout.')

    args = parser.parse_args()

    if not os.path.isfile(args.infile) and not os.access(args.infile, os.R_OK):
        print("Typed JSON file not found or no permissions to access. Exit.")
        sys.exit(1)

    try:
        with open(args.infile) as read_file:
            json_data = json.load(read_file)
    except ValueError:
        print("Typed JSON file has incorrect content. Exit.")
        sys.exit(1)

    all_fields = {x for x in json_data[0].keys()}
    fields = set({})
    if args.include:
        for field in args.include:
            if field in all_fields:
                fields.add(field)
    else:
        fields = all_fields

    if args.exclude:
        for field in args.exclude:
            if field in fields:
                fields.remove(field)

    flags = {}
    if args.htmlfile:
        flags['htmlfile'] = args.htmlfile
    if args.yes:
        flags['overwrite'] = True
    if args.preventscreen:
        flags['noscreen'] = True

    return json_data, fields, flags


def main(json_data, fields, flags):
    """ Main routine """
    tmpl = Template('''<html><body>
<table border=1>
    <tr>{% for field in fields %}<th>{{ field }}</th>{% endfor %}</tr>
    {% for item in json recursive %}
    <tr>{% for fld in fields %}<td>{{ item[fld] }}</td>{% endfor %}</tr>
    {% endfor %}
</table>
</body></html>
''')

    html = tmpl.render(json=json_data, fields=fields)

    if 'noscreen' not in flags:
        print(html)

    if 'htmlfile' in flags:
        if os.path.isfile(flags['htmlfile']) and \
          not flags.get('overwrite', False):
            print(f"Output file '{flags['htmlfile']}' exists, but "
                  "overwrite flag --yes is not set. Exit.")
            sys.exit(1)
        if not os.access(os.path.dirname(flags['htmlfile']), os.W_OK):
            print(f"Output file '{flags['htmlfile']}' can't be created "
                  "due to permissions. Exit.")
            sys.exit(1)

        try:
            with open(flags['htmlfile'], 'w') as out_file:
                out_file.writelines(html)
        except PermissionError:
            print("No permissions to create output HTML file. Exit.")
            sys.exit(1)
        except OSError as err:
            print(
                f"Error occurred with output file: {err.strerror}. Exit.")
            sys.exit(1)


if __name__ == "__main__":
    JSON, FIELDS, FLAGS = init_vars()
    main(JSON, FIELDS, FLAGS)
