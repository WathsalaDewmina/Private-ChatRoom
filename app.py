from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.json
    messages.append(message)
    return jsonify({'status': 'OK'})

@app.route('/get_messages')
def get_messages():
    start_time = time.time()
    while time.time() - start_time < 30:  # Timeout after 30 seconds
        if len(messages) > 0:
            return jsonify(messages)
        time.sleep(1)
    return jsonify([])  # Return empty list if no messages after timeout

if __name__ == '__main__':
    app.run(debug=True)
