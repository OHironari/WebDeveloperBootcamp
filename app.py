import datetime
from flask import Flask,render_template,request
from pymongo import MongoClient

from dotenv import load_dotenv
import os

# .envを読み込む
load_dotenv()

app = Flask(__name__)

todos = [
    ("Get milk",False),
    ("Learn programming",True)
]

@app.route("/",methods=["GET","POST"])
def todo():
    return render_template("home.html",todos=todos)

@app.route("/<string:todo>")
def todo_item(todo: str):
    for text,complete in todos:
        if text == todo:
            complete_text = "[x]" if complete else "[]"
            title = f"{complete_text} - Todos"
            return render_template("todo.html",text=text,complete=complete,title=title)
    else:
        return render_template("not-found.html",text=todo,title="Not found")








