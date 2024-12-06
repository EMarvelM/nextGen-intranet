from . import db, BaseModel

class User(BaseModel):
    __tablename__ = "users"

    firstname = db.Column(db.String(36), nullable=False)
    lastname = db.Column(db.String(36), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=True)
    permission = db.Column(db.String(36))
