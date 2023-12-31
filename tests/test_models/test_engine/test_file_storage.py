#!/usr/bin/python3
"""This module creates a test class that test the file storage system"""

from models.base_model import BaseModel
from models import storage, FileStorage
import unittest
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place


class TestFileStorage(unittest.TestCase):
    """Tests the file storage system that is employed for serializing
        and deserializing of the various data from the interpreter.
    """

    def test_FileStorage_attributes(self):
        """This checks the private attributes of FileStorage class
            is present and of right type.
        """
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_storage_is_instantiated(self):
        """This tests that the storage instance is instantiated and
        private object dict is available
        """
        self.assertEqual(type(storage.all()), dict)

    def test_storage_dict_contains_correct_objs_values(self):
        """Test that the dictionary values are objects which are subclasses
        of BaseModel."""
        b = BaseModel()
        c = BaseModel()
        d = User()
        e = Amenity()
        f = City()
        g = State()
        h = Review()
        i = Place()
        obj_dict = storage.all()
        for obj_id in obj_dict.keys():
            self.assertTrue(issubclass(type(obj_dict[obj_id]), BaseModel))

    def test_storage_dict_keys_are_in_right_format(self):
        """Check that the object keys for the dictionary are stored in
        appropriate format of `<class name>.id`.
        """
        b = BaseModel()
        c = BaseModel()
        d = User()
        e = Amenity()
        f = City()
        g = State()
        h = Review()
        i = Place()
        obj_dict = storage.all()
        b_key = f"{b.__class__.__name__}.{b.id}"
        c_key = f"{c.__class__.__name__}.{c.id}"
        d_key = f"{d.__class__.__name__}.{d.id}"
        e_key = f"{e.__class__.__name__}.{e.id}"
        f_key = f"{f.__class__.__name__}.{f.id}"
        g_key = f"{g.__class__.__name__}.{g.id}"
        h_key = f"{h.__class__.__name__}.{h.id}"
        i_key = f"{i.__class__.__name__}.{i.id}"
        self.assertTrue(b_key in obj_dict)
        self.assertTrue(c_key in obj_dict)
        self.assertTrue(d_key in obj_dict)
        self.assertTrue(e_key in obj_dict)
        self.assertTrue(f_key in obj_dict)
        self.assertTrue(g_key in obj_dict)
        self.assertTrue(h_key in obj_dict)
        self.assertTrue(i_key in obj_dict)

    def test_Save_and_retrieval(self):
        """Test the serialization and deserialization process"""
        test_storage = FileStorage()
        b = BaseModel()
        c = BaseModel()
        d = User()
        e = Amenity()
        f = City()
        g = State()
        h = Review()
        i = Place()
        storage.save()
        obj_dict = test_storage.all()
        b_key = f"{b.__class__.__name__}.{b.id}"
        c_key = f"{c.__class__.__name__}.{c.id}"
        d_key = f"{d.__class__.__name__}.{d.id}"
        e_key = f"{e.__class__.__name__}.{e.id}"
        f_key = f"{f.__class__.__name__}.{f.id}"
        g_key = f"{g.__class__.__name__}.{g.id}"
        h_key = f"{h.__class__.__name__}.{h.id}"
        i_key = f"{i.__class__.__name__}.{i.id}"
        self.assertTrue(b_key in obj_dict)
        self.assertTrue(c_key in obj_dict)
        self.assertTrue(d_key in obj_dict)
        self.assertTrue(e_key in obj_dict)
        self.assertTrue(f_key in obj_dict)
        self.assertTrue(g_key in obj_dict)
        self.assertTrue(h_key in obj_dict)
        self.assertTrue(i_key in obj_dict)
