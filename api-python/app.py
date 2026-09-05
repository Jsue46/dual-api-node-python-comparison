from flask import Flask, jsonify

app = Flask(__name__)

# Endpoint de verificación de estado
@app.route('/check', methods=['GET'])
def check():
    return "OK", 200

# Endpoint de información
@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        "Instancia": "Instancia-2 - API Python",
        "Curso": "Seminario de Sistemas 1 A",
        "Grupo": "Grupo 11"
    })

if __name__ == '__main__':
    # Escucha en el puerto 80 para acceso directo desde la IP pública
    app.run(host='0.0.0.0', port=80)
