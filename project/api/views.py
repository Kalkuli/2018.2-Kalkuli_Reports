from flask import Blueprint, request, jsonify

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
        sum += report.get('total_price')

    return jsonify({
        'receipts': reports,
        'total_sum': sum
    }), 200
