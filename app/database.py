from pathlib import Path
import json

DATA_DIR = Path("/data")
DATA_FILE = DATA_DIR / "todos.json"

DATA_DIR.mkdir(parents=True, exist_ok=True)
if not DATA_FILE.exists():
    DATA_FILE.write_text(json.dumps([]))


def read_todos():
    """Lê todos os to-dos do arquivo."""
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def write_todos(todos):
    """Escreve os to-dos no arquivo."""
    with open(DATA_FILE, "w") as file:
        json.dump(todos, file, indent=4)
