from ..extensions import db

class Uc(db.Model):
    __tablename__ = "ucs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150))
    type = db.Column(db.String(50))
    start = db.Column(db.Date)
    end = db.Column(db.Date)

    def __repr__(self):
        return f"<Uc(nome={self.name}, tipo={self.type}, inicio={self.start}, fim={self.end})>"
