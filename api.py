from flask import Flask
app = Flask(__name__)

import json
import re
import collections

tag_re = r'#[a-zA-Z0-9_]+\b'
url_re = 'https?://\S+'

@app.route('/urls')
def urls():
    with open('urls.txt', 'r') as fh:
        data = fh.read()
    raw_tags = re.findall(r'#[a-zA-Z0-9_]+\b', data)
    ctr = collections.Counter()
    for tag in raw_tags:
        ctr[tag] += 1
    return json.dumps(ctr)

@app.route('/urls/<tag>')
def tag(tag):
    with open('urls.txt', 'r') as fh:
        lines = fh.readlines()

    matched_lines = []
    for line in lines:
        m = re.findall('#'+tag, line)
        if m:
            url_match = re.search(url_re, line)
            if url_match:
                url = url_match.group()
                matched_lines.append({
                    'url':url,
                    'description':line,
                })

    return json.dumps(matched_lines)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

