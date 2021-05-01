 from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("./index.html")

@app.route('/index.html')
def Home():
    return render_template("./index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# def write_to_data(data):
# 	with open("database.txt", mode= "a") as datastorage:
# 		email = data["email"]
# 		subject = data["text"]
# 		message = data["message"]
# 		data_writer = datastorage.write(f"{email},{subject},{message}")


def write_to_csv(data):
	with open("database.csv", mode= "a", newline='') as datastorage2:
		email = data["email"]
		subject = data["text"]
		message = data["message"]
		csv_writer = csv.writer(datastorage2, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
		return redirect("./thankyou.html")
	else:
		return "something went wrong"

