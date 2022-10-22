from sqlalchemy import Column, Integer, String
from database import Base

class create_article_text(Base):
    __tablename__= "articles_info"
    id = Column(Integer, primary_key = True)
    url = Column(String)
    title = Column(String)
    date = Column(String)
    tags = Column(String)
    text = Column(String)
    links = Column(String)