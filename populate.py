from project.api.models import Report


def seedReports(db):
    db.session.add(Report(company_id=1, date_from='2018-09-13', date_to='2018-09-21', total_cost='12.23', total_tax_cost=2.33))
    db.session.add(Report(company_id=2, date_from='2018-10-15', date_to='2018-10-22', total_cost='122.23', total_tax_cost=10.53))
    db.session.add(Report(company_id=3, date_from='2018-11-14', date_to='2018-11-23', total_cost='412.30', total_tax_cost=200.13))
    db.session.commit()
