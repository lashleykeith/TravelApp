import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


# This class defines the coloums and relationships in the
# category table on the psql database
class Destinations(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(1000), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'video':self.id
        }


# This class defines the coloums and relationships in the
# user table on the psql database
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(256), index=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'username': self.username
        }


# This class defines the coloums and relationships in the
# item table on the psql database
class Item(Base):
    __tablename__ = 'item'

    title = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(500))
    video = Column(String(250))
    photo_image = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Destinations)
    createdUser_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    #maybe
    @property
    def imgsrc(self):
        return uploaded_images.url(self.photo)
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        
        return {
            'cat_id': self.category_id,
            'title': self.title,
            'description': self.description,
            'video': self.video,
            'photo_image': self.photo_image,
            'id': self.id,
            'created_User': self.user.username
        }


engine = create_engine('sqlite:///destinations.db')

Base.metadata.create_all(engine)
