from datetime import datetime

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    Unicode,
    UnicodeText,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), unique=True, nullable=False)
    body = Column(UnicodeText, nullable=True, default = u'')
    created = Column(DateTime, default=datetime.utcnow)
    edited = Column(DateTime, default=datetime.utcnow)

    @classmethod
    def all(cls):
        return [(o.id, o.title, o.body, o.created, o.edited) for o in DBsession.query(cls).order_by(created)]
    
    @classmethod
    def by_id(cls,gid):
#        return [(o.id, o.title, o.body, o.created, o.edited) for o in DBsession.query(Entry).filter(id = gid)]
        return DBsession.query(cls).get(gid)

#pass session in to evaluate if it exisits
"""
class Entry2(Entry):
    pass

entries = Entry.all()

entry2s = Entry2.all()
"""

Index('my_index', Entry.title, unique=True, mysql_length=255)

