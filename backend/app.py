# pending for module test FC 2024-04-29

# import json

# def link_variable_to_codelist(variables_json_path, codelists_json_path):
#     # Load the variables metadata JSON
#     with open(variables_json_path, 'r') as var_file:
#         variables_metadata = json.load(var_file)['data']

#     # Load the codelists metadata JSON
#     with open(codelists_json_path, 'r') as codelist_file:
#         codelists_metadata = json.load(codelist_file)['data']

#     # Create a dictionary to hold the linked metadata
#     linked_metadata = {}

#     # Iterate over each variable in the variables metadata
#     for domain, variables in variables_metadata.items():
#         linked_metadata[domain] = {}
#         for var_name, var_details in variables.items():
#             # Retrieve the codelist name
#             codelist_name = var_details.get('Controlled Terms, Codelist or Format')
#             if codelist_name:
#                 # If the codelist name exists in the codelists metadata, link it
#                 var_details['Codelist Values'] = codelists_metadata.get(codelist_name, [])
#             linked_metadata[domain][var_name] = var_details

#     # Return or process the linked metadata
#     return linked_metadata

# linked_meta = link_variable_to_codelist('variables_metadata.json', 'codelists_metadata.json')

