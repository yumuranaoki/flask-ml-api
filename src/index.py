from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
  return 'hello world'

@app.route('/register', methods=['POST'])
def register():
  req = request.json
  app.logger.debug('request from %s', req['name'])
  return jsonify({
    'status': 'ok'
  })
  


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)