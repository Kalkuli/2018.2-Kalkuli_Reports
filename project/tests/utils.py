from project.api.models import Report
from project import db

def add_report(company_id, data_from, data_to, total_cost, total_tax_cost):
    report = Report(company_id, data_from, data_to, total_cost, total_tax_cost)
    db.session.add(report)
    db.session.commit()
    return report