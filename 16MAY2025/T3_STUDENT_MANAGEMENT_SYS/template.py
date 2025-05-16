import os
from pathlib import Path

list_of_files = [
    "./github/workflows/.gitkeep",
    f"./src/api/__init__.py",
    f"./src/models/__init__.py",
    f"./src/core/__init__.py",
    f"./src/schemas/__init__.py",
    f"./src/services/__init__.py",
    f"./src/__init__.py",
    f"README.md",
    f"main.py",
    f"schema.sql"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
    
    else:
        print('file already exists')
