import datetime
from flask import Flask,render_template,request
from pymongo import MongoClient

from dotenv import load_dotenv
import os

# .envを読み込む
load_dotenv()

# 環境変数からMongoDB URIを取得
mongo_uri = os.getenv("MONGODB_URI")

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html",title="Habit Tracker - Home")

@app.route("/add",methods=["GET","POST"])
def add_habit():
    return render_template("add_habit.html",title="Habit Tracker - Add Habit")



