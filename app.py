from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/resultado.txt")
def resultado():
    return send_from_directory(".", "resultado.txt")

if __name__ == "__main__":
    # Ejecutar procesar.py antes de iniciar
    os.system("python procesar.py")
    app.run(host="0.0.0.0", port=5000)

