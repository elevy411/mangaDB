from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    manga = db.relationship('MangaOwned',backref='user',lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class MangaOwned(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140),index=True,unique=True)
    author = db.Column(db.String(140))
    volume_owned = db.Column(db.String(140))
    volume_available = db.Column(db.String(140))
    finished_series= db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<{} - {}>'.format(self.title,self.author)