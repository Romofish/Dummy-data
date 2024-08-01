from flask import Blueprint, jsonify, request
from app.services.config_service import (
    read_config, update_config, get_processed_output, 
    get_domain_config, update_domain_variable_config, 
    read_output, update_output,read_general_settings, update_general_settings
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


@api.route('/general_settings', methods=['GET'])
def get_general_settings():
    settings = read_general_settings()
    return jsonify(settings)

@api.route('/general_settings', methods=['POST'])
def update_general_settings_file():
    new_settings = request.json

    # Validate new settings
    for key, value in new_settings.items():
        if key == "STUDYID" and "value" not in value:
            return jsonify({"error": f"Missing 'value' for {key}"}), 400
        elif key in ["SITEID", "SUBJID"] and "ranges" not in value:
            return jsonify({"error": f"Missing 'ranges' for {key}"}), 400
        elif key == "USUBJID" and "components" not in value:
            return jsonify({"error": f"Missing 'components' for {key}"}), 400

    update_general_settings(new_settings)
    return jsonify({"message": "General settings updated successfully"})

# 注册Blueprint
from app import app
app.register_blueprint(api, url_prefix='/api')
