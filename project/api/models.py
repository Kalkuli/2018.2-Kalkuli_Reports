from project import db


class Report(db.Model):
    __tablename__ = 'report'
    id             = db.Column(db.Integer,  primary_key=True, autoincrement=True)
    company_id     = db.Column(db.Integer,  nullable=False)
    date_from      = db.Column(db.DateTime, nullable=False)
    date_to        = db.Column(db.DateTime, nullable=False)
    total_cost     = db.Column(db.Float,    nullable=False)
    total_tax_cost = db.Column(db.Float,    nullable=False)
    tagUseReports  = db.relationship('tagUseReport',   backref='report', lazy=True)

    def __init__(self, company_id, date_from, date_to, total_cost, total_tax_cost):
        self.company_id     = company_id 
        self.date_from      = date_from 
        self.date_to        = date_to 
        self.total_cost     = total_cost 
        self.total_tax_cost = total_tax_cost 


class TagUseReport(db.Model):
    __tablename__ = 'tagUseReport'
    id         = db.Column(db.Integer,  primary_key=True, autoincrement=True)
    report_id  = db.Column(db.Integer, db.ForeignKey('report.id'), nullable=False)
    tag_id     = db.Column(db.Integer, nullable=False)
    times_used = db.Column(db.Integer, nullable=False)

    def __init__(self, report_id, tag_id):
        self.report_id  = report_id
        self.tag_id     = tag_id