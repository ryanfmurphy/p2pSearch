from flask import Flask
app = Flask(__name__)

import json, re, collections, sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

tag_re = r'#[a-zA-Z0-9_]+\b'
url_re = 'https?://\S+'

@app.route('/urls')
def urls():
    with sqlite3.connect('urls.db') as db:
        db.row_factory = dict_factory
        return json.dumps(db.execute('SELECT * FROM url').fetchall())

'''
@app.route('/urls/tags')
def tags(): #todo make tag associations and implement this
    with open('urls.txt', 'r') as fh:
        data = fh.read()
    raw_tags = re.findall(r'#[a-zA-Z0-9_]+\b', data)
    ctr = collections.Counter()
    for tag in raw_tags:
        ctr[tag] += 1
    return json.dumps(ctr)
'''

@app.route('/urls/search/<search>')
def search(search):
    with sqlite3.connect('urls.db') as db:
        db.row_factory = dict_factory
        return json.dumps(db.execute('SELECT * FROM url WHERE description LIKE ?', ('%'+search+'%',)).fetchall())

@app.route('/urls/tag/<tag>')
def tag(tag):
    with open('urls.txt', 'r') as fh:
        lines = fh.readlines()

    matched_lines = []
    for line in lines:
        m = re.findall('#'+tag+r'\b', line)
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

