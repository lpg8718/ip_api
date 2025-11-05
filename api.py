from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get-ip', methods=['GET'])
def get_ip():
    xff = request.headers.get('X-Forwarded-For')
    if xff:
        user_ip = xff.split(',')[0].strip()
    else:
        user_ip = request.headers.get('X-Real-IP') or request.remote_addr

    return jsonify({
        "client_ip": user_ip,
        "x_forwarded_for": xff,
        "x_real_ip": request.headers.get('X-Real-IP'),
        "remote_addr": request.remote_addr
    })

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
