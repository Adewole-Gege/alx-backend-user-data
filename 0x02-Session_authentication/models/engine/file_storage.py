#!/usr/bin/env python3
"""FileStorage engine for saving and loading data"""
import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if not os.path.exists(self.__file_path):
            return
        try:
            with open(self.__file_path, 'r') as f:
                from models.base_model import BaseModel  # example base class
                objs = json.load(f)
                for key, val in objs.items():
                    self.__objects[key] = BaseModel(**val)
        except Exception as e:
            print(f"Could not reload storage: {e}")

    def close(self):
        """Placeholder for compatibility"""
        self.save()

