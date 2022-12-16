from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calc', methods=['POST'])
def calc_estimation():
    text = request.form['text']
    results = process_text(text)
    return jsonify(results)

def process_text(text: str) -> str:
    return [text.upper()] * 10

if __name__ == '__main__':
    app.run()