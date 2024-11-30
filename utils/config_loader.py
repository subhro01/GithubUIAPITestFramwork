import yaml

def load_config(file_path="config.yaml"):
    """Helper function to load configuration from a YAML file."""
    with open(file_path, "r") as f:
        config = yaml.safe_load(f)
    return config