from flask import Flask, render_template, request
import main_flow

app = Flask(__name__)

colors_rgb = [
    '255, 200, 200',
    '200, 255, 200',
    '200, 200, 255',
    '255, 255, 200',
    '255, 200, 255',
    '200, 255, 255',
    '200, 200, 200',
    '200, 200, 200',
    '200, 200, 200',
    '200, 200, 200']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    query = request.form.get('query')
    n_papers = 20
    titles, links, positions, clusters = main_flow.flow(query, n_papers)
    colors = [colors_rgb[int(c)] for c in clusters]
    return render_template(
        'results.html',
        query=query,
        data=zip(titles, links),
        positions = [list(map(int, pos)) for pos in positions],
        colors=colors
        )

if __name__ == '__main__':
    app.run(debug=True)