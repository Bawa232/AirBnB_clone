#!/usr/bin/python3
"""This module contains the FileStorage Class which handles serializing and
deserializing the various instances that would be used in the project.
"""

import json


class FileStorage():
    """serializes instances to a JSON file and deserializes JSON
        file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id

        Args:
            obj: object to be added to the __Objects dictionary

        """
        cls_name = obj.__class__.__name__
        key = f"{cls_name}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file __file_path"""
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as json_file:
            json_dict = {}
            for key, obj in FileStorage.__objects.items():
                json_dict[key] = obj.to_dict()
            json.dump(json_dict, json_file)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        from ..base_model import BaseModel
        from ..user import User
        from ..state import State
        from ..city import City
        from ..amenity import Amenity
        from ..place import Place
        from ..review import Review

        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as j_fil:
                json_dict = json.load(j_fil)
                for key, obj_dict in json_dict.items():
                    if obj_dict["__class__"] == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**obj_dict)
                    elif obj_dict["__class__"] == "User":
                        FileStorage.__objects[key] = User(**obj_dict)
                    elif obj_dict["__class__"] == "State":
                        FileStorage.__objects[key] = State(**obj_dict)
                    elif obj_dict["__class__"] == "City":
                        FileStorage.__objects[key] = City(**obj_dict)
                    elif obj_dict["__class__"] == "Amenity":
                        FileStorage.__objects[key] = Amenity(**obj_dict)
                    elif obj_dict["__class__"] == "Place":
                        FileStorage.__objects[key] = Place(**obj_dict)
                    elif obj_dict["___class__"] == "Review":
                        FileStorage.__objects[key] = Review(**obj_dict)
        except Exception:
            return
