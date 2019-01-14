from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route(address) - each function here contains the starting point of code for each page

# a sample search page
@app.route('/search')
def search_page():
    return render_template("search.html") # This renders the html page mentioned here

# Another sample request
@app.route('/search_file', methods=['POST'])
def search_file():
	file_name = request.form['query']
	return open('../corpus/' + file_name + '.txt', 'r').read()  # This returns the required result
