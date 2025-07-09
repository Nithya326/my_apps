from flask import Flask, request, jsonify
from db import DB

app = Flask(__name__)
db = DB()

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(db.get_all())

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    return jsonify(db.get(id))

@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.json
    db.create(data['name'], data['role'])
    return jsonify({'status': 'created'})

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.json
    db.update(id, data['name'], data['role'])
    return jsonify({'status': 'updated'})

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    db.delete(id)
    return jsonify({'status': 'deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)