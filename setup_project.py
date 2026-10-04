from pathlib import Path

folders = [
    "data/raw",
    "data/processed",
    "models",
    "notebooks",
    "src",
    "configs",
    "logs",
]

for f in folders:
    p = Path(f)
    p.mkdir(parents=True, exist_ok=True)
    (p / ".gitkeep").touch()   # lets Git track empty folders

gitignore = """# Python
__pycache__/
*.py[cod]
*.egg-info/
build/
dist/

# Jupyter Notebook checkpoints
.ipynb_checkpoints/

# Virtual environments
.venv/
venv/
aipdd_env/

# Binary model weights
*.pt
*.onnx
*.h5

# OS / editor files
.DS_Store
Thumbs.db
.vscode/
"""

Path(".gitignore").write_text(gitignore)
print("Project structure created.")