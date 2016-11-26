# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

from app import app, db

# need to add all models for db.create_all to work
from counter.models import *

class CounterTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DATABASE_NAME'] = 'testcounter'
        self.db_uri = 'mysql+pymysql://%s:%s@%s/' % (app.config['DB_USERNAME'], app.config['DB_PASSWORD'], app.config['DB_HOST'])
        app.config['SQLALCHEMY_DATABASE_URI'] = self.db_uri + app.config['DATABASE_NAME']
        engine = sqlalchemy.create_engine(self.db_uri)
        conn = engine.connect()
        conn.execute("commit")
        conn.execute("create database "  + app.config['DATABASE_NAME'])
        db.create_all()
        conn.close()
        self.app = app.test_client()

    def tearDown(self):
        db.session.remove()
        engine = sqlalchemy.create_engine(self.db_uri)
        conn = engine.connect()
        conn.execute("commit")
        conn.execute("drop database "  + app.config['DATABASE_NAME'])
        conn.close()

    def test_counter(self):
        rv = self.app.get('/')
        assert '1' in str(rv.data)
        rv = self.app.get('/')
        assert '2' in str(rv.data)

if __name__ == '__main__':
    unittest.main()
