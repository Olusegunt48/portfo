from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', 'a') as database:
        name = data['name']
        email = data['email']
        description = data['description']
        data = database.write(f"\n {name}, {email}, {description}")
        
def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database2:
        name = data['name']
        email = data['email']
        description = data['description']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,description])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong!!!'


if __name__ == "__main__":
    app.run(debug=True)