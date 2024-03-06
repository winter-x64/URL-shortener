from .. import db


class urlbase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_code = db.Column(db.String(), nullable=False)
    url_real = db.Column(db.String(200), nullable=False)
