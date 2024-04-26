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
    # Create a .gitkeep file in the directory to ensure Git tracks it
    gitkeep_path = os.path.join(full_path, '.gitkeep')
    with open(gitkeep_path, 'w') as gitkeep:
        pass  # You just need an empty file, so 'pass' will do nothing
    print(f"Created .gitkeep in: {gitkeep_path}")

# Creating files that need to be empty or have specific content
files_with_content = {
    'README.md': 'Project Overview\n================',
    '.gitignore': '*.pyc\n__pycache__/\n*.log\n.env',
    'requirements.txt': '# Add project dependencies here\n'
}

for file_name, content in files_with_content.items():
    file_path = os.path.join(base_path, file_name)
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Created file: {file_name} with initial content")
