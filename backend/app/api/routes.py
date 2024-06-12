from flask import Blueprint, jsonify, request
from app.services.config_service import (
    read_config, update_config, get_processed_output, 
    get_domain_config, update_domain_variable_config, 
    read_output, update_output
)

api = Blueprint('api', __name__)

@api.route('/output', methods=['GET'])
def get_output():
    processed_output = get_processed_output()
    return jsonify(processed_output)

@api.route('/output', methods=['POST'])
def update_output_file():
    new_output = request.json
    update_output(new_output)
    return jsonify({"message": "Output updated successfully"})

@api.route('/config', methods=['GET'])
def get_config():
    config = read_config()
    return jsonify(config)

@api.route('/config', methods=['POST'])
def update_config_file():
    new_config = request.json
    update_config(new_config)
    return jsonify({"message": "Config updated successfully"})

@api.route('/config/<domain>', methods=['GET'])
def get_domain_configuration(domain):
    domain_config = get_domain_config(domain)
    return jsonify(domain_config)

@api.route('/config/<domain>/<variable>', methods=['POST'])
def update_domain_variable_configuration(domain, variable):
    updated_config = request.json
    response = update_domain_variable_config(domain, variable, updated_config)
    return jsonify(response)

# 注册Blueprint
from app import app
app.register_blueprint(api, url_prefix='/api')
