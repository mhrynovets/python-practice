#!/usr/bin/python3

# 5. Create script, which represents provided JSON as HTML file with tables.
# You can choose which fields can be present, but the number of them should be at least 5. (jinja2)

import json
import sys
from jinja2 import Template

# load json from file
jsonFile = "cx_report.json"
try:
    with open(jsonFile) as f:
        json_data = json.load(f)
except:
    print("Can't read given file. Exiting...")
    sys.exit(1)

tmpl = Template('''
<html><body>
<table border=1>
    <tr>{% for item in json[0] %}<th>{{ item }}</th>{% endfor %}</tr>
    {% for item in json recursive %}
    <tr>{% for key, value in item.items() %}<td>{{ value }}</td>{% endfor %}</tr>
    {% endfor %}
</table>
</body></html>
''')

html = tmpl.render(json=json_data)

print(html)
with open('index.html', 'w') as f:
    f.writelines(html)
