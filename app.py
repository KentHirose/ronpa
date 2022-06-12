from flask import Flask, render_template, request
import sys; sys.path.insert(0, './modules')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visualization', methods=['POST'])
def results():
    word = request.form.get('query')
    titles = ['自然言語処理', 'コロナウイルス']
    links = ['http://abehiroshi.la.coocan.jp/']*2
    return render_template('visualization.html', word=word, data=zip(titles, links))

if __name__ == '__main__':
    app.run(debug=True)