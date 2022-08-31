#!/usr/bin/python3
"""Contains the BaseModel class
"""


from models.__init__ import storage
import uuid
import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Class Constructor
        """
        id = uuid.uuid4()
        self.id = str(id)
        now = datetime.datetime.now()
        self.created_at = now
        self.updated_at = now

        storage.new(self)

        if kwargs:
            for k, v in kwargs.items():
                if v is not self.__class__.__name__:
                    self.__dict__[k] = v

        id = uuid.uuid4()
        self.id = str(id)
        now = datetime.datetime.now()
        self.created_at = now
        self.updated_at = now

    def __str__(self):
        """Returns a neatly formated string representation
        """
        str_repr = "[{}] ({}) {}".format(
                                        self.__class__.__name__,
                                        self.id, self.__dict__)
        return str_repr

    def save(self):
        """Updates the public instance attribute updated_at\
            with the current datetime
        """
        now = datetime.datetime.now()
        self.updated_at = now
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values\
            of __dict__ of the instance
        """
        now = datetime.datetime.now()
        self.created_at = now.isoformat()
        self.updated_at = now.isoformat()
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        return (my_dict)
