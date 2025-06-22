from flask import Flask, render_template, request, jsonify
import cohere

app = Flask(__name__)


co = cohere.Client("use your api key ")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    try:
        response = co.chat(message=user_input)
        return jsonify({'reply': response.text})
    except Exception as e:
        return jsonify({'reply': f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
