import os, sys

sys.path.append(os.getcwd())

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import db
from models import *

tags = [Tag(name='python'),Tag(name='flask')]

if __name__ == '__main__':
    engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432') 
    conn = engine.connect()
    try:
       conn.execute("commit")
       conn.execute("drop database flask_db")
    except Exception as other:
       print("Can't delete 'flask_db' because of:", other)
    
    try:
       conn.execute("commit")
       conn.execute("create database flask_db")
    except Exception as other:
       print("Can't create 'flask_db' because of:", other)

    conn.close()

    db.create_all()
    db.session.add_all(tags) 
    db.session.commit()

    allTags = db.session.query(Tag).all()

    entries = [Entry(title='Python entry', body='This is a Python entry', tags=[allTags[0]]),
               Entry(title='Flask entry', body='This is a Flask entry'),
               Entry(title='More Flask', body='This is a More Flask entry'),
               Entry(title='Django entry', body='This is a Django entry')]

    db.session.add_all(entries)
    db.session.commit()
    db.session.close()
