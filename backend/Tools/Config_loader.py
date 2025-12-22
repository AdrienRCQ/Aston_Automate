import yaml

def load_db_config():
    with open("Configurations/Db_manager.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)