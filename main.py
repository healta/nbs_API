from fastapi import FastAPI, status
from database import Base, engine
from pydantic import BaseModel
from sqlalchemy.orm import Session
import models
from models import create_article_text
from fastapi import HTTPException
import sqlite3

#creates database, but not needed, DB already created
Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/articles/")
def get_all_articles():
    session = Session(bind=engine, expire_on_commit=False)

    all_articles = session.query(create_article_text).all()

    session.close()

    return all_articles

@app.get("/articles/label={label}")
def get_article_by_label(label:str):

    con = sqlite3.connect('NBS_scrapes.db')
    
    cur = con.cursor()

    query = """SELECT * FROM articles_info WHERE tags = ?;"""

    cur.execute(query,(label,))

    get_labels = cur.fetchall()
    
    cur.close()

    con.close()

    if not get_labels:
        raise HTTPException(status_code=404, detail=f"Article with label {tags} not found.")

    return get_labels

@app.get("/articles/date={dates}")
def get_article_by_date(dates: str):

    con = sqlite3.connect('NBS_scrapes.db')
    
    cur = con.cursor()

    query = """SELECT * FROM articles_info WHERE date = ?;"""

    cur.execute(query,(dates,))

    get_dates = cur.fetchall()
    
    cur.close()

    con.close()

    if not get_dates:
        raise HTTPException(status_code=404, detail=f"Article with date {date} not found.")

    return get_dates

@app.get("/article/{id}")
def read_article_by_id(id:int):
    
    session = Session(bind=engine,  expire_on_commit= False)

    article = session.query(create_article_text).get(id)

    session.close()
    
    #raises exception if article ID is not in the database
    if not article:
        raise HTTPException(status_code=404, detail=f"Article with id {id} not found.")

    return article

@app.delete("/article/{id}")
def delete_article(id: int):

    session = Session(bind=engine, expire_on_commit=False)

    article = session.query(create_article_text).get(id)

    if article:
        session.delete(article)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404, detail=f"Article item with id {id} not found")

    return None

@app.put("/article/id={id}&text={text}")
def update_article(id: int, text:str):

    session = Session(bind=engine, expire_on_commit=False)

    to_change = session.query(create_article_text).get(id)

    if to_change:
        to_change.text = text
        session.commit()

    session.close()

    if not to_change:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found.")
    
    return to_change
