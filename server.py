from flask import Flask, request, jsonify
import os  # Importamos os para leer la variable de entorno PORT

app = Flask(_name)  # CORREGIDO: __name_ con doble guion bajo

# Guardar los últimos datos recibidos
datos_sensores = {"temperatura": None, "humedad": None, "luz": None}

@app.route('/datos', methods=['POST'])
def recibir_datos():
    global datos_sensores
    datos_sensores = request.json
    print("Datos recibidos:", datos_sensores)
    return jsonify({"mensaje": "Datos recibidos correctamente"}), 200

@app.route('/datos', methods=['GET'])
def enviar_datos():
    return jsonify(datos_sensores), 200

if _name_ == '_main':  # CORREGIDO: __name_ con doble guion bajo
    port = int(os.environ.get("PORT", 10000))  # Render asigna el puerto dinámicamente
    app.run(host='0.0.0.0', port=port, debug=True)
