#!/usr/bin/python3
"""unittest for the Place class"""

from models.place import Place
import unittest


class TestBaseModel(unittest.TestCase):
    """Test the Place class"""

    def test_instantiation(self):
        """Test for correct instantiation"""
        b = Place()
        self.assertEqual(type(b.id), str)
        self.assertEqual(b.city_id, "")
        self.assertEqual(type(b.user_id), str)
        self.assertNotEqual(b.created_at, None)
        self.assertNotEqual(b.updated_at, None)

    def test_unique_id(self):
        """Simple test to show id are different"""
        b1 = Place()
        b2 = Place()
        b3 = Place()
        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b2.id, b3.id)
        self.assertNotEqual(b1.id, b3.id)

    def test_save(self):
        """Test to check instance is upated at each time save() called"""
        b = Place()
        update0 = b.updated_at
        b.save()
        update1 = b.updated_at
        b.save()
        update2 = b.updated_at
        self.assertTrue(update0 < update1)
        self.assertTrue(update1 < update2)
        self.assertTrue(update0 < update2)

    def test_str(self):
        """check for right string representation"""
        b = Place()
        b.name = "2BDRM Seaview"
        string = "[{}] ({}) {}".format(b.__class__.__name__, b.id, b.__dict__)
        self.assertEqual(str(b), string)

    def test_to_dict(self):
        """tests that dict represntation is correct"""
        b = Place()
        b.name = "2BDRM Seaview"
        b.save()
        json_dict = b.to_dict()
        self.assertEqual(len(json_dict), (len(b.__dict__) + 1))
        self.assertEqual(json_dict["id"], b.id)
        self.assertEqual(json_dict["updated_at"], b.updated_at.isoformat())
        self.assertEqual(json_dict["created_at"], b.created_at.isoformat())
        self.assertEqual(json_dict["__class__"], b.__class__.__name__)
        self.assertEqual(json_dict["name"], b.name)

    def test_from_dict(self):
        """Create a Amenity class from a dictionary gotten from to_dict"""
        b = Place()
        b.name = "2BDRM Seaview"
        b.save()
        json_dict = b.to_dict()
        new_b = Place(**json_dict)
        self.assertEqual(b.id, new_b.id)
        self.assertEqual(b.name, new_b.name)
        self.assertTrue(b.created_at == new_b.created_at)
        self.assertTrue(b.updated_at == new_b.updated_at)

    def test_instantiation_with_args(self):
        """Test to ensure args passed on instatntiation are not used"""
        b = Place()
        c = Place(b.id, b.created_at, b.updated_at)
        self.assertNotEqual(b.id, c.id)
        self.assertTrue(b.created_at < c.created_at)
        self.assertTrue(b.updated_at < c.updated_at)
