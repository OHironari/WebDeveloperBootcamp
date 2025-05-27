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












#以下検証用のコードのため不要だが一応残している


class GalileanMoons:
    def __init__(self,first,second,third,fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth





@app.route("/for-loop/conditionals")
def render_for_loops_conditionals():
    
    user_os = {
        "Bob Smith":"Windows",
        "Anne Pun":"MacOS",
        "Adam Lee":"Linux",
        "Jose Salvatierra":"Windows"
    }
    return render_template("loops_and_conditionals.html",user_os=user_os)



@app.route("/for-loop/")
def render_loops_for():
    planets = [
        "Mercury",   # 水星
        "Venus",     # 金星
        "Earth",     # 地球
        "Mars",      # 火星
        "Jupiter",   # 木星
        "Saturn",    # 土星
        "Uranus",    # 天王星
        "Neptune"    # 海王星
    ]

    return render_template("for_loop.html",planets=planets)

@app.route("/conditionals_basics/")
def conditionals_basics():
    company = ""

    return render_template("conditionals_basics.html",company=company)


@app.route("/data_structures/")
def render_data_structures():

    movies = [
        "Leon the Professional"
        "The Usual Suspects"
        "A Beautiful Mind"
    ]

    car = {
        "brand":"Tesla",
        "model":"Roadstar",
        "year":"2020"
    }

    moons = GalileanMoons("Io","Europa","Ganymede","Callisto")

    kwargs = {
        "movies":movies,
        "car":car,
        "moons":moons
    }
    return render_template("data_structures.html",**kwargs)


@app.route("/expressions/")
def render_expressions():
    color = "brown"
    animal_one = "fox"
    animal_two = "dog"

    orange_amount = 10
    apple_amount = 20
    donate_amount = 15

    first_name = "Captain"
    last_name = "Marvel"

    kargs = {
        "color" : color,
        "animal_one" : animal_one,
        "animal_two" : animal_two,
        "orange_amount" : orange_amount,
        "apple_amount" : apple_amount,
        "donate_amount" : donate_amount,
        "first_name" : first_name,
        "last_name" : last_name
    }

    return render_template("expressions.html",**kargs)
