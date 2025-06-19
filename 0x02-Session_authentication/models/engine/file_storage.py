#!/usr/bin/env python3
"""Simple file-based storage engine.
Serializes/deserializes objects to a JSON file on disk."""
import json
import os
from datetime import datetime
import uuid


class FileStorage:
    """FileStorage engine – stores objects in JSON file."""

    __file_path = "file.json"
    __objects = {}

    # ------------------------------ All storage methods -------------------- #
    def all(self, cls=None):
        """Return dict of all objects (optionally filtered by class)."""
        if cls:
            return {k: v for k, v in self.__objects.items()
                    if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Add obj to storage dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        ser_dict = {k: v.to_json(save_to_file=True)
                    for k, v in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(ser_dict, f)

    def reload(self):
        """Deserialize JSON file back into __objects."""
        if not os.path.isfile(self.__file_path):
            return
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                raw = json.load(f)
                for k, v in raw.items():
                    cls_name = v["__class__"]
                    from models.user import User   # only model we need here
                    cls_map = {"User": User}
                    cls = cls_map.get(cls_name)
                    if cls:
                        self.__objects[k] = cls(**v)
        except Exception:
            pass
