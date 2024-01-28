from taipy.gui import Gui
from app.pages.home import home_md
from app.pages.choice import choice_md
from app.pages.profile import profile_md
from app.pages.wishlist import wishlist_md

from app.pages.choice import on_init as choice_on_init

import json
from os import environ as env
from urllib.parse import quote_plus, urlencode

from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for

import pyperclip
import json

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
   
app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")

oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
)

# GLOBAL STATE
user = None

pages = {
    # "/": "<|navbar|>",
    "home": home_md,
    "choice": choice_md,
    "profile": profile_md,
    "wishlist": wishlist_md,
}

def on_init(state):
    choice_on_init(state)

stylekit = {
    "color_secondary": "#BB86FC",
    "color_primary": "#68CAAA",
}

# for logout
@app.route("/")
def home():
    return redirect(f"/home")

@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
    redirect_uri=url_for("callback", _external=True)
    )

@app.route("/callback", methods=["GET", "POST"])
def callback():
    global user
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    pyperclip.copy(json.dumps(token))
    print("token copied")
    # TODO: control redirect by whether the profile is new
    return redirect(f"/profile")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://" + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
        {
        "client_id": env.get("AUTH0_CLIENT_ID"),
        },
        quote_via=quote_plus,
    )
    )
Gui(pages=pages,flask=app).run(use_reloader=True,port=5001,stylekit=stylekit)
