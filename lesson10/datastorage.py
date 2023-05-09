from dataclasses import dataclass


@dataclass
class DataStorage:
    path_to_storage: str = "database.json"
