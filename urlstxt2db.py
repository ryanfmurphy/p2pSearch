# go from urls.txt into urls.db

import sqlite3, re
db = sqlite3.connect('urls.db')

with open('urls.txt', 'r') as fh:
    lines = fh.readlines()

url_re = 'https?://\S+'

for line in lines:
    print "line: ", line,
    this_line = {}
    this_line['description'] = line
    url_match = re.search(url_re, line)
    if url_match:
        url = url_match.group()
        this_line['url'] = url
        print this_line
        db.execute(
            'INSERT INTO url (url, description, source_node_id) VALUES (?, ?, ?)',
            (this_line['url'], this_line['description'], 1)
        )
        db.commit()

