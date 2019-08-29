#!/usr/bin/python3

# 5. Create script, which represents provided JSON as HTML file with tables.
# You can choose which fields can be present, but the number of them should be at least 5. (jinja2)

import json
import sys
from jinja2 import Template

if len(sys.argv) not in range(2,4):
    print("Usage: %s filename [optional: fields in CSV format]" % sys.argv[0])
    print("Exit.")
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        json_data = json.load(f)
except:
    print("Can't read given file. Exiting...")
    sys.exit(1)

fields = []
if (len(sys.argv) == 3):
    fieldsIn = [x.strip(" ").strip("'\"") for x in sys.argv[2].split(",")]
    for field in fieldsIn:
        if field in json_data[0]:
            fields.append(field)
else:
    fields = [x for x in json_data[0].keys()]

tmpl = Template('''
<html><body>
<table border=1>
    <tr>{% for field in fields %}<th>{{ field }}</th>{% endfor %}</tr>
    {% for item in json recursive %}
    <tr>{% for field in fields %}<td>{{ item[field] }}</td>{% endfor %}</tr>
    {% endfor %}
</table>
</body></html>
''')

html = tmpl.render(json=json_data, fields=fields)

print(html)
with open('index.html', 'w') as f:
    f.writelines(html)
