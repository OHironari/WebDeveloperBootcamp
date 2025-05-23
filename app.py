from flask import Flask,render_template

app = Flask(__name__)

class GalileanMoons:
    def __init__(self,first,second,third,fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth


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
