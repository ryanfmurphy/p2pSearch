from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    description  =db.Column(db.String())
    source_id = Column(Integer, ForeignKey('node.id'))
    source = relationship("Node")

    tags = relationship("Tag",
                    secondary=association_table)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


CREATE TABLE url (
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
