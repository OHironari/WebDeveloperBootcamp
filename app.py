import datetime
from flask import Flask,render_template,request
from pymongo import MongoClient

from dotenv import load_dotenv
import os

# .envを読み込む
load_dotenv()

# 環境変数からMongoDB URIを取得
mongo_uri = os.getenv("MONGODB_URI")

def create_app():
    app = Flask(__name__)
    client = MongoClient(mongo_uri)
    app.db = client.microblog

    entries = []

    @app.route("/",methods=["GET","POST"])
    def home():
        if request.method == "POST":
            #contentはhtmlのname=の部分
            #<textarea name="content" id="entry" class="form__textarea"></textarea>
            entry_content = request.form.get("content")
            formatted_date=datetime.datetime.today().strftime("%Y-%m-%d")
            app.db.entries.insert_one({"content" : entry_content, "date" : formatted_date})
        entries_with_date = [
            (
                entry["content"],
                entry["date"],
                datetime.datetime.strptime(entry["date"],"%Y-%m-%d").strftime("%b %d")

            )
            for entry in app.db.entries.find({})
        ]
        return render_template("home.html",entries=entries_with_date)

    return app








