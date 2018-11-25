from flask import Blueprint, request, jsonify
from project.api.models import Report

from sqlalchemy import exc
from project import db


reports_blueprint = Blueprint('/report', __name__)

@reports_blueprint.route('/<company_id>/get_reports', methods=['GET'])
def get_all_reports(company_id):
    response = {
        'status': 'success',
        'data': {
            'reports': [reports.to_json() for reports in Report.query.filter_by(company_id=int(company_id))]
        }
    }

    return jsonify(response)


@reports_blueprint.route('/add_report', methods=['POST'])
def add_report():
    data = request.get_json()

    if not data:
        return jsonify({
            'error': 'Report can not be saved'
        }), 400

    company_id = data.get('company_id')
    tag_id = data.get('tag_id')
    data_from = data.get('date_from')
    data_to = data.get('date_to')


    try:
        report = Report(company_id, tag_id, data_from, data_to)
        db.session.add(report)
        db.session.commit()

        return jsonify({
            'status': 'success',
            'data': {
                'message': 'Report was created!'
            }
        }), 200
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify({
            'error': 'Report can not be saved'
        }), 400

@reports_blueprint.route('/<company_id>/report/<report_id>', methods=['DELETE'])
def delete_report(company_id, report_id):
    error_response = {
        'status': 'Fail',
        'message': 'Report not found' 
    }

    report = Report.query.filter_by(id=int(report_id), company_id=int(company_id)).first()

    if not report:
        return jsonify(error_response), 404

    db.session.delete(report)
    db.session.commit()
    
    reponse = {
        'status': 'Success',
        'data': {
            'message': 'Report deleted'
        }
    }

    return jsonify(reponse), 200