from app import db

class Deceased(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    jewish_death_date = db.Column(db.String(64), index=True)
    secular_death_date = db.Column(db.DateTime, index=True)
    tablet_column = db.Column(db.Float, index=True)
    bio = db.Column(db.Text)
    order = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Deceased {}>'.format(self.full_name)
