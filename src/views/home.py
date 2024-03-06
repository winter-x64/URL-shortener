import uuid

from flask import Blueprint, redirect, render_template, request, url_for

from .. import db
from ..models.models import urlbase

home_view = Blueprint(name="home_view", import_name=__name__)


def generate_event_id() -> str:
    event_id: str = str(uuid.uuid4().hex)[:8].upper()
    event_id = f"{event_id}"
    return event_id


@home_view.route(rule="/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        url_real: str = request.form.get("url_real")
        url_code: str = generate_event_id()

        teacher = urlbase(url_real=url_real, url_code=url_code)

        db.session.add(instance=teacher)
        db.session.commit()
        return redirect(location=url_for(endpoint="home_view.index"))

    url_list = urlbase.query.all()

    return render_template(template_name_or_list="index.html", url_list=url_list)


@home_view.route(rule="/<string:url_tail>", methods=["POST", "GET"])
def url_finder(url_tail: str):
    url_entry = urlbase.query.filter_by(url_code=url_tail).first()
    if url_entry:
        return redirect(location=url_entry.url_real)
    else:
        return "<h1>nahi nahi</h1>"
