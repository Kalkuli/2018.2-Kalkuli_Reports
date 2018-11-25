from project import db


class Report(db.Model):
    __tablename__ = 'report'
    id             = db.Column(db.Integer,  primary_key=True, autoincrement=True)
    company_id     = db.Column(db.Integer,  nullable=True)
    tag_id         = db.Column(db.Integer,  nullable=True)
    date_from      = db.Column(db.DateTime, nullable=True)
    date_to        = db.Column(db.DateTime, nullable=True)

    def __init__(self, company_id, tag_id, date_from, date_to):
        self.company_id     = company_id
        self.tag_id         = tag_id 
        self.date_from      = date_from 
        self.date_to        = date_to 
        
    def to_json(self):
        return {
            'id': self.id,
            'company_id': self.company_id,
            'tag_id': self.tag_id,
            'date_from': self.date_from,
            'date_to': self.date_to,
        }
