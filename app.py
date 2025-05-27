import datetime
from flask import Flask,render_template,request
from pymongo import MongoClient

from dotenv import load_dotenv
import os

# .envを読み込む
load_dotenv()

# 環境変数からMongoDB URIを取得
mongo_uri = os.getenv("MONGODB_URI")

@app.route("/",methods=["GET","POST"])
def todo():
    return render_template("home.html",todos=["Get milk", "Learn programming"])










