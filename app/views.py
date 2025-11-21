from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    send_from_directory,
)

import os
import json

views = Blueprint("views", __name__)

@views.route("/home")
def home():
    return render_template("home.html")










# NEVER, I REPEAT NEVERRRR - touch this code snippet pls <3
#
# just keep it for the sake of it
def mibombo(mi: str, bombo: bool) -> str:
    # TODO: make it work ig
    return mi + bombo