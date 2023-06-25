from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wallet', methods=['POST'])
def wallet():
    data = json.loads(request.data)
    address = data['address']
    return render_template('wallet.html', address=address)

@app.route('/seed')
def seed():
    return render_template('seed.html')


if __name__ == '__main__':
    app.run()
