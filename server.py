from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from user_agents import parse
import socket

app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app)

# Obsługa żądania GET dla strony głównej
@app.route('/')
def homepage():
    return app.send_static_file('index.html')

# Obsługa żądania POST na adresie /send_data
@app.route('/send_data', methods=['POST'])
def send_data():
    data = request.get_json()
    
    # Odebranie danych od klienta
    external_ip = request.remote_addr  # Adres IP klienta
    user_agent_string = request.headers.get('User-Agent')
    user_agent = parse(user_agent_string)
    operating_system = user_agent.os.family  # System operacyjny klienta
    
    # Tutaj możesz przetworzyć lub wykorzystać odebrane dane
    print(f"Adres IP klienta: {external_ip}")
    print(f"System operacyjny klienta: {operating_system}")
    
    # Przykładowa odpowiedź
    response_data = {'message': 'Dane odebrane przez serwer A'}

    # Odpowiedź w formacie JSON
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
