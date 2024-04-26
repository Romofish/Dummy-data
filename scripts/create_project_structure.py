
import os

# Define the directories to be created
directories = [
    'frontend/src',
    'frontend/public',
    'backend/app/api',
    'backend/app/services',
    'backend/app/models',
    'backend/tests',
    'data_generation/generator',
    'data_generation/config',
    'metadata/definitions',
    'docs',
    'scripts'
]

# Base path where the directories will be created
base_path = '.'  # Adjust the base path if necessary

# Create each directory
for dir_path in directories:
    full_path = os.path.join(base_path, dir_path)
    os.makedirs(full_path, exist_ok=True)
    print(f"Created directory: {full_path}")

# Creating files that need to be empty or have specific content
files_with_content = {
    'README.md': 'Project Overview\n================',
    '.gitignore': '*.pyc\n__pycache__/',
    'requirements.txt': '# Add project dependencies here'
}

for file_name, content in files_with_content.items():
    with open(os.path.join(base_path, file_name), 'w') as file:
        file.write(content)
    print(f"Created file: {file_name} with initial content")
