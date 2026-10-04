from config import DATA_DIR

def initialize_directories() -> None:
    DATA_DIR.mkdir(exist_ok=True)
