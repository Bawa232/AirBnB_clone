#!/usr/bin/python3
"""unittest for the User class"""

from models.user import User
import unittest


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def test_instantiation(self):
        """Test for correct instantiation"""
        b = User()
        self.assertEqual(type(b.id), str)
        self.assertNotEqual(b.created_at, None)
        self.assertNotEqual(b.updated_at, None)

    def test_unique_id(self):
        """Simple test to show id are different"""
        b1 = User()
        b2 = User()
        b3 = User()
        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b2.id, b3.id)
        self.assertNotEqual(b1.id, b3.id)

    def test_save(self):
        """Test to check instance is upated at each time save() called"""
        b = User()
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
        b = User()
        b.First_name = "My First Model"
        b.password = "8952"
        string = "[{}] ({}) {}".format(b.__class__.__name__, b.id, b.__dict__)
        self.assertEqual(str(b), string)

    def test_to_dict(self):
        """tests that dict represntation is correct"""
        b = User()
        b.name = "My First Model"
        b.my_number = 89
        b.save()
        json_dict = b.to_dict()
        self.assertEqual(len(json_dict), (len(b.__dict__) + 1))
        self.assertEqual(json_dict["id"], b.id)
        self.assertEqual(json_dict["updated_at"], b.updated_at.isoformat())
        self.assertEqual(json_dict["created_at"], b.created_at.isoformat())
        self.assertEqual(json_dict["__class__"], b.__class__.__name__)

    def test_from_dict(self):
        """Create a BaseModel class from a dictionary gotten from to_dict"""
        b = User()
        b.first_name = "My First Model"
        b.password = "8952"
        b.save()
        json_dict = b.to_dict()
        new_b = User(**json_dict)
        self.assertEqual(b.id, new_b.id)
        self.assertEqual(b.first_name, new_b.first_name)
        self.assertEqual(b.password, new_b.password)
        self.assertTrue(b.created_at == new_b.created_at)
        self.assertTrue(b.updated_at == new_b.updated_at)

    def test_instantiation_with_args(self):
        """Test to ensure args passed on instatntiation are not used"""
        b = User()
        c = User(b.id, b.created_at, b.updated_at)
        self.assertNotEqual(b.id, c.id)
        self.assertTrue(b.created_at < c.created_at)
        self.assertTrue(b.updated_at < c.updated_at)
