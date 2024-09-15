from flask import Flask, jsonify

app = Flask(__name__)

# Servicio para obtener usuarios
@app.route('/users')
def get_users():
    users = ['Alice', 'Bob', 'Charlie']
    return jsonify({'users': users})

# Servicio para obtener productos
@app.route('/products')
def get_products():
    products = ['Laptop', 'Phone', 'Tablet']
    return jsonify({'products': products})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
