from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64))
    phoneNumber = db.Column(db.String(64))
    email = db.Column(db.String(64))
    posts = db.relationship('Post', backref='user')

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    content = db.Column(db.Text)
    done = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    @property
    def serialize(self):
        return {
            'postID' : self.id,
            'title' : self.title,
            'content' : self.content,
            'done' : self.done,
            'userID' : self.user_id
        }
