from flask import Flask, render_template, request
import sys; sys.path.insert(0, './modules')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    word = request.form.get('query')


    # 仮 -------------------------------
    # positions = [[0.2, 0.2], [0.7, 0.7]]
    titles = ['自然言語処理', 'コロナウイルス']
    links = ['http://abehiroshi.la.coocan.jp/']*2
    positions = [[50, 50], [300, 300]]
    colors = [[255, 0, 0], [0, 255, 255]]

    return render_template(
        'results.html',
        word=word,
        data=zip(titles, links),
        positions=positions,
        colors=colors
        )

if __name__ == '__main__':
    app.run(debug=True)