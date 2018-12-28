from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/search')
def search_page():
    return render_template("search.html")


@app.route('/search_file', methods=['POST'])
def search_file():
	file_name = request.form['query']
	return open('../corpus/' + file_name + '.txt', 'r').read()
