# C:\Users\Unisinu\Desktop\RecordApp\backend\app.py

from flask import Flask, render_template, request, jsonify, Blueprint

app = Flask(__name__)

# Configuramos el Blueprint para servir archivos estáticos desde la carpeta 'frontend'
frontend_bp = Blueprint('frontend', __name__, static_folder='../frontend/static', template_folder='../frontend/templates')
app.register_blueprint(frontend_bp)

from calculations import calculate_probable_combinations

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_combinations', methods=['POST'])
def calculate_combinations():
    data = request.json
    numbers_list = data['numbers'].split('-')
    probable_combinations = calculate_probable_combinations(numbers_list)
    return jsonify({'combinations': probable_combinations})

if __name__ == '__main__':
    app.run(debug=True)