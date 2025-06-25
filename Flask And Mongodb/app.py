from flask import Flask, jsonify, request, render_template, redirect, url_for
from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()  # Load environment variables from .env file if present

MONGO_URI = os.getenv('MONGO_URI')

mongoClient = MongoClient(MONGO_URI)
db = mongoClient["mydatabase"]
collection = db["submissions"]

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        try:
            collection.insert_one({'name': name})
            return redirect(url_for('success'))
        except Exception as e:
            return render_template('form.html', error=str(e))
    return render_template('form.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/api', methods=['GET'])
def get_names():
    try:
        with open('names.txt', 'r') as file:
            # Read all lines, strip newlines, and filter out empty lines
            names = [line.strip() for line in file if line.strip()]
        return jsonify(names), 200
    except FileNotFoundError:
        return jsonify({"error": "names.txt file not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(port=8000, debug=True)