#!/usr/bin/python3
"""Contains the FileStorage
"""


import json


class FileStorage:
    """Serializes and deserializes instances
    """
    __file_path = "file.json"
    __objects = dict()
    

    def all(self):
        """returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        if obj is not None:
            obj_name = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[obj_name] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        objects = dict()
        for k in self.__objects:
            objects[k] = self.__objects[k].to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as f:
            jsn_file = json.dump(objects, f)

    def reload(self):
        """deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, "r") as f:
                jsn_file = json.load(f)
            
            # for k in jsn_file:
            #     self.__objects[k] = classes[jsn_file[k]["__class__"]](**jsn_file[k])

        except FileNotFoundError:
            pass
