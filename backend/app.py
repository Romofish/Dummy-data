from flask import Flask, jsonify
from data_generation.generator.metadata_reader import load_metadata

app = Flask(__name__)

@app.route('/get_metadata', methods=['GET'])
def get_metadata():
    try:
        metadata = load_metadata()
        return jsonify(metadata), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


