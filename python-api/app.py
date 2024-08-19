from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
import logging

app = Flask(__name__)

AUTH_TOKEN = "your_auth_token"
ENABLE_AUTH = False

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

def encrypt_message(data, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(data.encode())
    return encrypted_message.decode()

def decrypt_message(data, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(data.encode())
    return decrypted_message.decode()

@app.route('/api/encrypt', methods=['POST'])
def encrypt():
    if ENABLE_AUTH:
        auth_token = request.headers.get('Authorization')
        if auth_token != AUTH_TOKEN:
            logging.warning("Unauthorized access attempt.")
            return jsonify({"error": "Unauthorized"}), 401

    content = request.json
    if not content or 'data' not in content or 'key' not in content:
        logging.error("Invalid request data.")
        return jsonify({"error": "Invalid request data"}), 400

    data = content['data']
    key = content['key']

    try:
        encrypted_message = encrypt_message(data, key)
        logging.info("Message encrypted successfully.")
        return jsonify({"encrypted_message": encrypted_message})
    except Exception as e:
        logging.exception("Encryption failed.")
        return jsonify({"error": str(e)}), 500

@app.route('/api/decrypt', methods=['POST'])
def decrypt():
    if ENABLE_AUTH:
        auth_token = request.headers.get('Authorization')
        if auth_token != AUTH_TOKEN:
            logging.warning("Unauthorized access attempt.")
            return jsonify({"error": "Unauthorized"}), 401

    content = request.json
    if not content or 'data' not in content or 'key' not in content:
        logging.error("Invalid request data.")
        return jsonify({"error": "Invalid request data"}), 400

    data = content['data']
    key = content['key']

    try:
        decrypted_message = decrypt_message(data, key)
        logging.info("Message decrypted successfully.")
        return jsonify({"decrypted_message": decrypted_message})
    except Exception as e:
        logging.exception("Decryption failed.")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
