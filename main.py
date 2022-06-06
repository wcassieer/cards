from flask import (Flask, render_template, request, abort, jsonify, redirect, url_for)
from model import db, save_db

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        message="Here is a Welcome message...",
        cards=db
    )

@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template('card.html', card=card, index=index, max_index=len(db)-1)
    except IndexError:
        abort(404)

@app.route("/api/card/")
def api_card_list():
    # return model.db    # returning a list no allowed.
    return(jsonify(db ))

@app.route("/api/card/<int:index>")
def api_card_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)


@app.route('/add_card', methods=["GET", "POST"])
def add_card():
    if request.method == "POST":
        # form has been submitted, process data
        card = {"no": request.form['no'],
                "name": request.form['name'],
                "age": request.form['age'],
                "tel": request.form['tel'],
                "email": request.form['email']
                }
        db.append(card)
        save_db()
        return redirect(url_for('card_view', index=len(db)-1))
    else:
        return render_template("add_card.html")


@app.route('/remove_card/<int:index>', methods=["GET", "POST"])
def remove_card(index):
    try:
        if request.method == "POST":
            del db[index]
            save_db()
            return redirect(url_for('welcome'))
        else:
            return render_template("remove_card.html", card=db[index])
    except IndexError:
        abort(404)






"""
https://www.tldevtech.com/json-example/

[
{
"no": 1,
"name": "Coby Farrell",
"age": 35,
"tel": "643-800-0416 x7935",
"email": "reinger.eve@heaney.biz"
},
{
"no": 2,
"name": "Blake Batz",
"age": 57,
"tel": "(987) 966-8633",
"email": "rogahn.jonathon@eichmann.biz"
},
{
"no": 3,
"name": "Murray Marquardt",
"age": 60,
"tel": "357.849.7489 x087",
"email": "flatley.jace@yahoo.com"
},
{
"no": 4,
"name": "Omari D'Amore",
"age": 53,
"tel": "(760) 451-5600",
"email": "eroberts@hotmail.com"
},
{
"no": 5,
"name": "Lurline Goodwin",
"age": 34,
"tel": "589.735.9002",
"email": "providenci07@reinger.com"
},
{
"no": 6,
"name": "Kiel Rath",
"age": 38,
"tel": "+1-550-864-1657",
"email": "sophie.kris@hotmail.com"
},
{
"no": 7,
"name": "Dasia Huels",
"age": 23,
"tel": "701.396.0503 x446",
"email": "conroy.kacie@gmail.com"
},
{
"no": 8,
"name": "Blaze Stokes",
"age": 32,
"tel": "430-291-9027 x0795",
"email": "maribel05@gmail.com"
},
{
"no": 9,
"name": "Kenna Jenkins",
"age": 54,
"tel": "569-265-1709",
"email": "armando22@deckow.com"
},
{
"no": 10,
"name": "Corrine Cremin",
"age": 20,
"tel": "(249) 390-3316",
"email": "tweber@gmail.com"
},
{
"no": 11,
"name": "Rachel Tillman",
"age": 45,
"tel": "(638) 580-0531",
"email": "carlie57@zieme.com"
},
{
"no": 12,
"name": "Connie Bode",
"age": 44,
"tel": "619-874-5215 x5040",
"email": "amani26@sauer.com"
},
{
"no": 13,
"name": "Gwen McGlynn",
"age": 47,
"tel": "456.693.2402 x61057",
"email": "jadyn.huel@klocko.com"
},
{
"no": 14,
"name": "Edna Langworth",
"age": 30,
"tel": "603.800.6757 x3831",
"email": "christiana66@hotmail.com"
},
{
"no": 15,
"name": "Brielle Wisoky",
"age": 47,
"tel": "+1-740-366-2381",
"email": "gaylord.jayda@gaylord.net"
}
]


-- or --

{
  "red": "#f44336",
  "pink": "#e91e63",
  "purple": "#9c27b0",
  "deeppurple": "#673ab7",
  "indigo": "#3f51b5",
  "blue": "#2196f3",
  "lightblue": "#03a9f4",
  "cyan": "#00bcd4",
  "teal": "#009688",
  "green": "#4caf50",
  "lightgreen": "#8bc34a",
  "lime": "#cddc39",
  "yellow": "#ffeb3b",
  "amber": "#ffc107",
  "orange": "#ff9800",
  "deeporange": "#ff5722",
  "brown": "#795548",
  "grey": "#9e9e9e",
  "black": "#000000",
  "white": "#ffffff",
}




"""