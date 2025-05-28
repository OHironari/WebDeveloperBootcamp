import datetime
from flask import Flask,render_template,request
from pymongo import MongoClient

from dotenv import load_dotenv
import os

# .envを読み込む
load_dotenv()

# 環境変数からMongoDB URIを取得
mongo_uri = os.getenv("MONGODB_URI")
habits = ["Test habit","Test habit 2"]

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html",habits=habits,title="Habit Tracker - Home")

@app.route("/add",methods=["GET","POST"])
def add_habit():
    if request.method == "POST":
        habits.append(request.form.get("habit"))
    return render_template("add_habit.html",title="Habit Tracker - Add Habit")



