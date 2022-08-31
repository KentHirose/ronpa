from flask import Flask, render_template, request
import main_flow

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    params = {}
    params['query'] = request.form['query']
    params['n_papers'] = request.form.get('n_papers', type=int)
    params['option'] = request.form.get('option', type=bool)
    params['doc_type'] = request.form.getlist('doc_types', type=int)
    params['category'] = request.form.getlist('category', type=int)
    params['order_input'] = 0
    titles, links, positions, colors, balloon = main_flow.flow(params)
    return render_template(
        'results.html',
        query=params['query'],
        data=zip(titles, links, balloon),
        positions=[list(map(int, pos)) for pos in positions],
        colors=colors,
        )

if __name__ == '__main__':
    app.run(debug=True)