import os

# Caminho absoluto para a pasta src
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Caminho absoluto para os templates
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

def load_template(template_name):
    """
    Carrega um arquivo HTML ou JS localizado na pasta src/templates.
    """
    file_path = os.path.join(TEMPLATE_DIR, template_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Template não encontrado: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
