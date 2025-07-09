from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)
REST_API_URL = 'http://rest-service:5000/employees'

@app.route('/')
def index():
    response = requests.get(REST_API_URL)
    employees = response.json()
    return render_template('index.html', employees=employees)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'role': request.form['role']
        }
        requests.post(REST_API_URL, json=data)
        return redirect('/')
    return render_template('create.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'role': request.form['role']
        }
        requests.put(f"{REST_API_URL}/{id}", json=data)
        return redirect('/')
    employee = requests.get(f"{REST_API_URL}/{id}").json()
    return render_template('update.html', employee=employee)

@app.route('/delete/<int:id>')
def delete(id):
    requests.delete(f"{REST_API_URL}/{id}")
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
