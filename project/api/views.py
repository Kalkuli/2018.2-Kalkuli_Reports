from flask import Blueprint, request, jsonify
from project.api.models import Report

from sqlalchemy import exc
from project import db


reports_blueprint = Blueprint('/report', __name__)


@reports_blueprint.route('/report', methods=['POST'])
def reports():

    data = request.get_json()

    if not data:
        return jsonify({
            'error': 'empty json'
        }), 400

    reports = data.get('receipts')

    sum = 0

    for report in reports:
        if not report.get('total_price'):
            return jsonify({
                'error': 'empty total_price'
            }), 400
        sum += report.get('total_price')

    sum = str(sum)

    return jsonify({
        'receipts': reports,
        'total_cost': sum 
    }), 200

@reports_blueprint.route('/sum_receipts', methods=['GET'])
def sum_receipts():

    sum = 0

    for report in reports:
        if not report.get('total_price'):
            return jsonify({
                'error': 'empty total_price'
            }), 400
        sum += report.get('total_price')

    sum = str(sum)

    response = {
        'status': 'success',
        'sum': sum
    }

    return jsonify(response), 200


@reports_blueprint.route('/add_report', methods=['POST'])
def add_report():
    data = request.get_json()
    
    if not data:
        return jsonify({
            'error': 'Report can not be saved'
        }), 400

    reports = data.get('receipts')

    company_id = None
    data_from = data.get('date_from')
    data_to = data.get('date_to')
    total_cost = data.get('total_cost')
    total_tax_cost = None


    try:
        report = Report(company_id, data_from, data_to, total_cost, total_tax_cost)
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
