from project.api.models import Report
from project import db

def add_report(company_id, tag_id, data_from, data_to):
    report = Report(company_id, tag_id, data_from, data_to)
    db.session.add(report)
    db.session.commit()
    return report