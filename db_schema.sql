CREATE TABLE url (
    url_id INTEGER PRIMARY KEY AUTOINCREMENT,
    url VARCHAR,
    description VARCHAR,
    source_node_id INTEGER
);

CREATE TABLE node (
    node_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    host VARCHAR
);

CREATE TABLE tag (
    tag_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tag VARCHAR
);

CREATE TABLE tag2url (
    tag2url_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tag_id INTEGER,
    url_id INTEGER
);

INSERT INTO node (name, host) VALUES ('me', '127.0.0.1');

