from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/")
def hola_mundo():
    return "Hola mundo"

@app.post("/messages")
def read_messages():
    response = request.json
    message:str = response.get("message", " ")
    return jsonify({"response": "message: "+ message + "\n received sucessfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)