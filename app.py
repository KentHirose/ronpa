from flask import Flask, render_template, request
import sys; sys.path.insert(0, './modules')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    word = request.form.get('query')
    return render_template('results.html', word=word)

if __name__ == '__main__':
    app.run()