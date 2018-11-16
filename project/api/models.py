from project import db


class Report(db.Model):
    __tablename__ = 'report'
    id             = db.Column(db.Integer,  primary_key=True, autoincrement=True)
    company_id     = db.Column(db.Integer,  nullable=True)
    date_from      = db.Column(db.DateTime, nullable=False)
    date_to        = db.Column(db.DateTime, nullable=False)
    total_cost     = db.Column(db.String,    nullable=True)
    total_tax_cost = db.Column(db.Float,    nullable=True)

    def __init__(self, company_id, date_from, date_to, total_cost, total_tax_cost):
        self.company_id     = company_id 
        self.date_from      = date_from 
        self.date_to        = date_to 
        self.total_cost     = total_cost 
        self.total_tax_cost = total_tax_cost 
    
    def to_json(self):
        return {
            'id': self.id,
            'company_id': self.company_id,
            'date_from': self.date_from,
            'date_to': self.date_to,
            'total_cost': self.total_cost,
            'total_tax_cost': self.total_tax_cost
        }
