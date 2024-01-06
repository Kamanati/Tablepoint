
from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# Function to read data from CSV
def read_csv():
    data = []
    with open('departments.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

# Function to write data to CSV
def write_csv(data):
    fieldnames = ['department', 'sport1', 'sport2', 'sport3']
    with open('departments.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Display the initial point table
initial_data = read_csv()
print(initial_data)

# Routes
@app.route('/')
def index():
    data = read_csv()
    return render_template('user_view.html', data=data)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        department = request.form['department']
        sport = request.form['sport']
        points = request.form['points']

        data = read_csv()
        for row in data:
            if row['department'] == department:
                row[sport] = points

        write_csv(data)
        return redirect(url_for('index'))

    return render_template('admin_view.html')

if __name__ == '__main__':
    app.run()
